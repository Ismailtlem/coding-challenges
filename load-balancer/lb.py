import time
from typing import Any

import httpx
import uvicorn
from dotenv import load_dotenv
from fastapi import BackgroundTasks, FastAPI
from httpx import Response

from server import Server

load_dotenv()

SERVERS: list[Server] = [Server(f"localhost:800{str(number+1)}") for number in range(0, 4)]
HEALTHY_SERVERS: list[Server] = []
DEFAULT_HEALTH_CHECK_PERIOD: int = 5
current_server_index = 0


def run_healthcheck(healthcheck_period: int) -> None:
    """Perform health checks on the servers"""

    while True:
        for server in SERVERS:
            server.healthcheck()
            HEALTHY_SERVERS.append(server)
        time.sleep(float(healthcheck_period))


async def send_request(url: str) -> Response:
    """Send request to backend server"""

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    return response


app = FastAPI()
PORT = "8080"


@app.on_event("startup")
async def init_healthcheck():
    """Initial Health check"""

    for server in SERVERS:
        server.healthcheck()
        HEALTHY_SERVERS.append(server)


@app.get("/")
async def handle_requests(
    background_tasks: BackgroundTasks, healthcheck_period: int = DEFAULT_HEALTH_CHECK_PERIOD
) -> Any:
    """Handle requests coming to the load balancer"""

    global current_server_index
    print("current server index", current_server_index)
    background_tasks.add_task(run_healthcheck, healthcheck_period)
    try:
        await send_request(SERVERS[current_server_index].scheme + SERVERS[current_server_index].endpoint)
    except httpx.RequestError:
        print(f"request unsuccessful to the server {SERVERS[current_server_index].endpoint}")
    current_server_index = (current_server_index + 1) % len(SERVERS)


def main() -> Any:
    """Main function"""

    uvicorn.run("lb:app", host="0.0.0.0", port=int(PORT), log_level="info")


if __name__ == "__main__":
    main()
