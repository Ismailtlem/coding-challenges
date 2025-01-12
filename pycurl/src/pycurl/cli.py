import click

from .client import BaseClient
from .commons import common_argument, common_options


@click.group(invoke_without_command=True)
@click.option(
    "-X",
    "--x",
    is_flag=True,
    default=False,
    required=False,
    help="Specify the method to use",
)
@click.version_option()
def cli(x: bool) -> None:
    """Welcome to PyCurl."""
    pass


@cli.command("GET")
@common_argument
@common_options
def get_cmd(url: str, verbose: bool) -> None:
    """Define Get command."""
    client = BaseClient(url=url)
    print(client.send_request("GET", verbose))


@cli.command("DELETE")
@common_argument
@common_options
def delete_cmd(url: str, verbose: bool) -> None:
    """Define Delete command."""
    client = BaseClient(url=url)
    print(client.send_request("DELETE", verbose))


@cli.command("POST")
@common_argument
@common_options
@click.option("-d", "--data", type=click.STRING)
@click.option("-h", "--header", type=click.STRING)
def post_cmd(url: str, verbose: bool, data: str, header: str) -> None:
    """Define Post command."""
    client = BaseClient(url=url)
    print("data", data)
    print(client.send_request("POST", verbose, header, data))


@cli.command("PUT")
@common_argument
@common_options
@click.option("-d", "--data", type=click.STRING)
@click.option("-h", "--header", type=click.STRING)
def put_cmd(url: str, verbose: bool, data: str, header: str) -> None:
    """Define Post command."""
    client = BaseClient(url=url)
    print("data", data)
    print(client.send_request("PUT", verbose, header, data))
