import httpx


class Server:
    """Class to model the server object"""

    def __init__(self, endpoint: str, path: str = "/healthcheck"):
        self.endpoint = endpoint
        self.path = path
        self.healthy = True
        self.timeout = 1
        self.scheme = "http://"

    def healthcheck(self) -> None:
        """Run healthcheck"""

        try:
            response = httpx.get(self.scheme + self.endpoint + self.path, timeout=self.timeout)
            if response.status_code == httpx.codes.OK:
                self.healthy = True
            else:
                self.healthy = False
        except (httpx.RequestError, httpx.ReadTimeout):
            self.healthy = False

    def __repr__(self) -> str:
        return "<Server: {} {} {}>".format(self.endpoint, self.healthy, self.timeout)
