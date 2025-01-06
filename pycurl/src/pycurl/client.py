import socket
from itertools import chain
from typing import Any, ClassVar
from urllib import parse as urlparse
from urllib.parse import ParseResult

from requests import utils


class BaseClient(object):
    """Simple class to buid path for entities."""

    default_headers: ClassVar[dict[str, str | bytes]] = {
        "User-Agent": utils.default_user_agent(),
        "Content-Type": "application/x-www-form-urlencoded",
    }

    def __init__(self, url: str) -> None:
        """Init the class."""
        self.url = url

    def _build_request_headers(
        self, method: str, urlparsed: ParseResult, header: Any = None, data: Any = None
    ) -> str:
        request_header = f"{method} {urlparsed.path} HTTP/1.1\r\n"
        request_header += f"Host: {urlparsed.hostname}\r\n"
        request_header += "User-Agent: curl/8.1.2\r\n"
        request_header += "Accept: */*\r\n"
        request_header += "Connection: close\r\n"

        if method in ["POST", "PUT", "PATCH"]:
            if header:
                for h in header:
                    request_header += f"{h}\r\n"

            if data:
                request_header += f"Content-Length: {len(data)}\r\n\r\n"
                request_body = f"{data}\r\n\r\n"
        return (
            request_header + request_body
            if method in ["POST", "PUT", "PATCH"]
            else request_header + "\r\n"
        )

    def _parse_response(self, encoded_response: bytes, verbose: bool = False) -> str:
        """Decode the response."""
        response_splited = encoded_response.split(b"\r\n\r\n")
        return response_splited[1].decode()

    def send_request(self, method: str) -> str:
        """Send a request using sockets."""
        parsed_url = urlparse.urlparse(self.url)
        if parsed_url.scheme not in ["http", "https"]:
            error = "URL is incorrect"
            raise ValueError(error)

        port = parsed_url.port if parsed_url.port else 80
        request_header = self._build_request_headers(
            method,
            parsed_url,
        )
        with socket.create_connection((parsed_url.hostname, port)) as sock:
            sock.sendall(request_header.encode())

            response = b""
            while True:
                data = sock.recv(4096)
                if not data:
                    break
                response += data
        print("request_header.encode()", self._parse_response(response))
        return self._parse_response(response)
