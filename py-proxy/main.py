import json
import socket
from urllib import parse as urlparse

import httpx
from aiohttp import web


async def proxy_handler(request):
    # Extract the destination URL from the request
    print("requeeest", request.remote)
    print("requeeest", request.url)
    # breakpoint()
    full_target_url = str(request.url)

    print("taaarget url", full_target_url)

    # Extract the method, headers, and body of the incoming request
    method = request.method
    headers = dict(request.headers)
    headers["X-Forwarded-For"] = f"{request.remote}"
    banned_list = []
    banned_words = []

    with open("banned-words.txt", "r") as file:
        content = file.read()
        banned_words = [banned_word for banned_word in content.splitlines()]
        # for banned_word in content.splitlines():
        #     banned_words.append(banned_word)

    with open("banned-list.txt", "r") as file:
        content = file.read()
        for banned_url in content.splitlines():
            banned_list.append(urlparse.urlparse(banned_url).netloc)
    # try:
    if full_target_url not in banned_list:
        # make a socket connection
        async with httpx.AsyncClient() as client:
            response = await client.request(
                method,
                full_target_url,
                headers=headers,
            )
        for banned_word in banned_words:
            if banned_word in response.text:
                print("banned wwwwwwwword")
                return
        return web.Response(text="Hello, world")

        # print("booooody", response.content)
    else:
        # except web.HTTPClientError as e:
        print("HTTPClientError ")

    # Return the response back to the client


# Create the web application and add a wildcard route
app = web.Application()
app.router.add_route("*", "/{url:.*}", proxy_handler)

# Run the application on port 8080
web.run_app(app, port=8080)
