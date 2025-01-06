import argparse
import socket
from urllib.parse import urlparse


def build_request(method, urlparsed, header=None, data=None) -> str:
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


def send_request(urlparsed, request_header) -> bytes:
    port = urlparsed.port if urlparsed.port else 80

    with socket.create_connection((urlparsed.hostname, port)) as sock:
        sock.sendall(request_header.encode())

        response = b""
        while True:
            data = sock.recv(4096)
            if not data:
                break
            response += data

    return response


def parse_response(request_header, response, verbose=False) -> None:
    response_splited = response.split(b"\r\n\r\n")
    if verbose:
        for line in request_header.splitlines():
            print(f"> {line}")

        for line in response_splited[0].splitlines():
            print(f"< {line}")

        print(f"<\r\n{response_splited[1].decode()}")

    else:
        print(response_splited[1].decode())


def main() -> None:
    parser = argparse.ArgumentParser(description="Curl-like HTTP client")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("-X", "--method", default="GET", help="HTTP method")
    parser.add_argument("url", help="URL to send the request to")
    parser.add_argument("-d", "--data", help="Data to send in the request body")
    parser.add_argument("-H", "--header", action="append", help="Additional headers")

    args = parser.parse_args()

    verbose = args.verbose
    method = args.method
    url = args.url
    data = args.data
    header = args.header

    urlparsed = urlparse(url)

    request_header = build_request(method, urlparsed, header, data)
    response = send_request(urlparsed, request_header)
    parse_response(request_header, response, verbose)


if __name__ == "__main__":
    main()
