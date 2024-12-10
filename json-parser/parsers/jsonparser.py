import re

from parsers.exceptions import JsonException


class JsonParser(object):
    def __init__(self) -> None:
        self.input = ""
        self.index = 0

    def remove_spaces_from_input(self) -> str:
        """Remove spaces from the input data"""

        return self.input.strip().replace(" ", "").replace("\n", "")

    def check_n_2_character(self, input_to_check: str) -> bool:
        """Check the n-2 character"""

        pattern = r'[:"]'

        parsed_input = re.split(pattern, input_to_check)
        print("parsed_input", parsed_input)
        if len(parsed_input) > 1 and parsed_input[-2] and not parsed_input[-2].isalnum():
            raise JsonException("Input data cannot be parsed, the last element is invalid")
        return True

    def check_invalid_characters(self) -> bool:
        """Check for any invalid character"""

        input_without_spaces = self.remove_spaces_from_input()
        print(input_without_spaces, "input")
        if input_without_spaces[0] != "{":
            raise JsonException("Input data is invalid, the first character should be {")
        if input_without_spaces[1] != "}":
            if input_without_spaces[1] != '"':
                raise JsonException('Input data is invalid, the first key should be "')

        pattern = r'^[A-Za-z0-9{}"[\]:,]+$'
        print("maatch", re.match(pattern, input_without_spaces))
        breakpoint()
        # if not re.match(pattern, input_without_spaces):
        #     raise JsonException("The data contains invalid data")
        return True

    def check_character_after_commas(self) -> bool:
        """Check if there is any invalid character after the comma"""

        input_without_spaces = self.remove_spaces_from_input()
        comma_occurences = [i for i, letter in enumerate(input_without_spaces) if letter == ","]
        if comma_occurences:
            for index in comma_occurences:
                if input_without_spaces[index + 1] != '"':
                    raise JsonException("Input data cannot be parsed, there is an error after the ,")
        return True

    def check_character_after_colon(self) -> bool:
        """Check the character after colon"""

        formatted_input = self.remove_spaces_from_input().strip("{}").split(",")
        print("formatted input", formatted_input)
        # result_list = [substring.split(":")[1] for substring in input_without_spaces if len(substring.split(":")) > 1]
        for element in formatted_input:
            if element and element.split(":")[1]:
                element_value = element.split(":")[1]
                if (
                    not element_value.isnumeric()
                    and '"' not in element_value
                    and element_value not in ["true", "false", "null"]
                ):
                    raise JsonException("Input data cannot be parsed, there is an incorrect value in the json after :")
        return True

    def parse_input(self) -> str:
        """Parse the json input"""

        input_without_spaces = self.remove_spaces_from_input()
        conditions = [
            self.check_invalid_characters(),
            self.check_character_after_commas(),
            self.check_character_after_colon(),
        ]
        if all(conditions):
            print("true")
        return input_without_spaces
