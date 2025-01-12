from typing import Any

import click


_global_argument = [
    click.argument("url", type=click.STRING),
]


def common_argument(func) -> Any:
    """Define Common arguments in Pycurl."""
    for argument in _global_argument:
        func = argument(func)
    return func


_global_options = [
    click.option("-v", "--verbose", is_flag=True, default=False, help="Verbose mode")
]


def common_options(func) -> Any:
    """Define Common Options in Pycurl."""
    for option in _global_options:
        func = option(func)
    return func
