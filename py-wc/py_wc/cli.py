import os
import sys
from argparse import ArgumentParser
from typing import Any, TextIO


def get_words_number(file: TextIO) -> int:
    """Get the number of words in the file"""

    return len(file.read().split())


def read_lines(file: TextIO) -> list[str]:
    """Read the file in lines"""

    return file.readlines()


def handle_commands(args: Any) -> str:
    """Handle the output of the different commands"""

    output = ""
    if args.path:
        with open(args.path, "r", encoding="utf-8") as file:
            if args.word:
                output = str(get_words_number(file)) + " " + args.path
            elif args.lines:
                output = str(len(read_lines(file))) + " " + args.path
            elif args.characters:
                if args.path:
                    output = str(os.path.getsize(args.path)) + " " + args.path
                else:
                    output = str(len(file.read().encode("utf-8"))) + " " + args.path
            else:
                if args.path:
                    lines = read_lines(file)

                    words = len("".join(lines).split())
                    bytes_number = os.path.getsize(args.path)
                    output = (
                        str(len(lines))
                        + " "
                        + str(words)
                        + " "
                        + str(bytes_number)
                        + " "
                        + args.path
                    )
    elif sys.stdin:
        file = sys.stdin
        content = file.read()
        words = len(content.split())
        lines = content.count("\n") + 1
        bytes_number = len(content.encode("utf-8"))
        output = str(lines) + " " + str(words) + " " + str(bytes_number)
    return output


def cli() -> None:
    """Main Cli function"""

    parser = ArgumentParser(prog="cli that is like the unix command wc")
    parser.add_argument(
        "-path",
        help="The path of the file to parse",
        type=str,
    )
    parser.add_argument(
        "-w",
        "--word",
        action="store_true",
        help="print the word counts",
    )
    parser.add_argument(
        "-l",
        "--lines",
        action="store_true",
        help="print the number of lines",
    )
    parser.add_argument(
        "-m",
        "--characters",
        action="store_true",
        help="print the number of characters",
    )
    args = parser.parse_args()
    if args.path:
        print(handle_commands(args))

    elif sys.stdin:
        print(handle_commands(args))

