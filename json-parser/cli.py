import json
import re
import sys
from argparse import ArgumentParser
from typing import Any

from parsers.exceptions import JsonException
from parsers.jsonparser import JsonParser


def remove_spaces_from_input(input_data: str) -> str:
    """Remove spaces from the input data"""

    input_without_spaces = input_data.strip().replace(" ", "").replace("\n", "")
    if input_without_spaces[0] != "{":
        raise JsonException("Input data is invalid, the first character should be {")
    if input_without_spaces[1] != "}":
        if input_without_spaces[1] != '"':
            raise JsonException("Input data is invalid, the first key is invalid")
    return input_without_spaces


def parse_input(input_data: str) -> str:
    """Parse the json input"""

    first_result = remove_spaces_from_input(input_data)

    # check that there is only numbers, letters and braces
    first_pattern = r'^[A-Za-z0-9{}":]'
    if not re.match(first_pattern, first_result):
        raise JsonException("Input data contains invalid data")

    # check for the n-2 character : not valid if it contains something not alphanumeric,
    second_pattern = r'[:"]'
    parsed_input = re.split(second_pattern, first_result)
    if len(parsed_input) > 1 and parsed_input[-2] and not parsed_input[-2].isalnum():
        raise JsonException("Input data cannot be parsed, the last element is invalid")

    # after a , we must have "
    comma_occurences = [i for i, letter in enumerate(first_result) if letter == ","]
    if comma_occurences:
        for index in comma_occurences:
            if first_result[index + 1] != '"':
                raise JsonException("Input data cannot be parsed, there is an error after the ,")

    # after a : we must have VALID character
    colon_occurences = [i for i, letter in enumerate(first_result) if letter == ":"]
    if colon_occurences:
        for index in colon_occurences:
            if (
                not first_result[index + 1 : index + 5] != "true"
                and not first_result[index + 1 : index + 6] != "false"
                and not first_result[index + 1 : index + 5] != "null"
                and first_result[index + 1] not in ["{", '"']
            ):
                raise JsonException("Input data cannot be parsed, there is an error after the :")
    # check for boolean
    colon_regex = r"[:,\"]"
    third_input = re.split(colon_regex, first_result)
    for element in third_input:
        if element.lower() == "false" or element.lower() == "true":
            print("eleeeemennnnt", element)
            if element != "false" and element != "true":
                raise JsonException("There is an error in a boolean value")
    pattern = r"[:{}]"
    parsed_input = re.split(pattern, first_result)
    for element in parsed_input:
        if "[" in element:
            splitted_elmt = re.split(r"[[]", element)
            if "'" in splitted_elmt[1]:
                raise JsonException("There is an error after the [")
            if '"' == splitted_elmt[1][0]:
                if splitted_elmt[1][-2] != '"':
                    raise JsonException("There is an error at the end of the string. There is a double quotes missing")
            split_first_elmt = "".join(re.split(r"[]]", "".join(splitted_elmt)))
            if (
                '"' not in split_first_elmt
                and split_first_elmt != "false"
                and split_first_elmt != "true"
                and split_first_elmt != "null"
            ):
                raise JsonException("There is an invalid value inside []")
    print("final")
    return first_result


def main() -> None:
    """Main Cli function"""

    parser = ArgumentParser(prog="cli for parsing json")
    parser.add_argument("--path", help="The path of the file to parse")

    args = parser.parse_args()
    with open(args.path, "r", encoding="utf-8") as file:
        data = file.read()
        if not data:
            print("the data is empty")
            sys.exit(1)
        json_object = JsonParser()
        json_object.input = data
        parsed_input = json_object.parse_input()
    print(parsed_input)


if __name__ == "__main__":
    main()
