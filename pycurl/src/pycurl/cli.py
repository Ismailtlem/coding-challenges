import argparse
import os
import sys
from pathlib import Path
from typing import Literal, TextIO

import click

# from pygit.commands import cat_file_cmd, hash_git_cmd, init_repo_cmd
# from pygit.commands.helpers import is_file_ignored
# from . import base, data


@click.group()
@click.version_option()
def cli() -> None:
    """Welcome to PuCurl."""
    pass

