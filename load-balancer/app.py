from fastapi import FastAPI, Request, status

app = FastAPI()


@app.get("/")
def base_route(request: Request):
    """Base Route"""

    return f"this is the server {request.url}"


@app.get("/healthcheck", status_code=status.HTTP_200_OK)
def healthcheck():
    """Health check Route"""

    return "Health check OK"
