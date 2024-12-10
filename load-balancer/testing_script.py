import asyncio
import os
import sys
from argparse import ArgumentParser

import httpx
from dotenv import load_dotenv

load_dotenv()


def send_request(endpoint: str, port: str, health_check: int) -> httpx.Response:
    """Send a request to the load balancer"""

    response = httpx.get(f"{endpoint}:{port}", params={"healthcheck_period": health_check})
    return response


def main():
    """Main Cli function"""

    if sys.stdout.isatty():
        print("\t" + "Testing script")

    parser = ArgumentParser(prog="cli for testing the lb")
    parser.add_argument(
        "--health-check",
        "--h-c",
        type=int,
        help="The health check period to check for servers",
        # required=True,
    )
    args = parser.parse_args()
    lb_host = os.getenv("LB_HOST", "localhost")
    lb_port = os.getenv("LB_PORT", "8080")

    for _ in range(1, 4):
        send_request("http://" + lb_host, lb_port, args.health_check)


if __name__ == "__main__":
    main()
