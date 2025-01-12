import json
import socket
from itertools import chain
from typing import Any, ClassVar
from urllib import parse as urlparse
from urllib.parse import ParseResult

from requests import utils


class BaseClient(object):
    """Simple class to send requests."""

    default_headers: ClassVar[dict[str, str | bytes]] = {
        "User-Agent": utils.default_user_agent(),
        "Content-Type": "application/x-www-form-urlencoded",
    }

    def __init__(self, url: str) -> None:
        """Init the class."""
        self.url = url

    def _build_request(
        self, method: str, urlparsed: ParseResult, header: Any = None, data: Any = None
    ) -> str:
        request_header = f"{method} {urlparsed.path} HTTP/1.1\r\n"
        request_header += f"Host: {urlparsed.hostname}\r\n"
        request_header += "User-Agent: curl/8.1.2\r\n"
        request_header += "Accept: */*\r\n"
        request_header += "Connection: close\r\n"
        request_body = ""
        print("daaata", data)
        if method in ["POST", "PUT", "PATCH"]:
            if header:
                request_header += f"{header}\r\n"
            if data:
                print("typppe", type(data))
                request_header += f"Content-Length: {len(data)}\r\n\r\n"
                request_body = f"{data}"
        print("requesst header", request_header)
        return (
            request_header + request_body
            if method in ["POST", "PUT", "PATCH"]
            else request_header + "\r\n"
        )

    # def _build_request_body(self, data: Any) -> None | str:
    #     """Build the request body."""
    #     if not data:
    #         return None
    #     return f"{data}\r\n\r\n"

    def _parse_response(self, encoded_response: bytes) -> str:
        """Decode the response."""
        response_splited = encoded_response.split(b"\r\n\r\n")
        return response_splited[1].decode()

    def send_request(self, method: str, verbose: bool, header: Any = None, data: Any = None) -> str:
        """Send a request using sockets."""
        parsed_url = urlparse.urlparse(self.url)
        if parsed_url.scheme not in ["http", "https"]:
            error = "URL is incorrect"
            raise ValueError(error)

        port = parsed_url.port if parsed_url.port else 80
        request_params = self._build_request(method, parsed_url, header, data)
        if verbose:
            print("Connecting to %s", self.url)
            print(f"Sending request {method} {parsed_url.path} {parsed_url.scheme}/1.1")
            print(f"Host: {parsed_url.netloc}")
            print("Accept: */*\n")
        with socket.create_connection((parsed_url.hostname, port)) as sock:
            sock.sendall(request_params.encode())

            response = b""
            while True:
                b_data = sock.recv(4096)
                if not b_data:
                    break
                response += b_data
        if verbose:
            print(response.decode())
        return self._parse_response(response)
