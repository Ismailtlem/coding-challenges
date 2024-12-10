from typing import Any

from parsers.constants import JsonConstants


class lexer(object):
    def __init__(self, input) -> None:
        self.input = ""
        self.index = 0

    def lex_string(string):
        json_string = ""

        if string[0] == JsonConstants.JSON_QUOTE:
            string = string[1:]
        else:
            return None, string

        for c in string:
            if c == JsonConstants.JSON_QUOTE:
                return json_string, string[len(json_string) + 1 :]
            else:
                json_string += c

        raise Exception("Expected end-of-string quote")

    def lex(string):
        tokens = []

        while len(string):
            json_string, string = lex_string(string)
            if json_string is not None:
                tokens.append(json_string)
                continue

            json_number, string = lex_number(string)
            if json_number is not None:
                tokens.append(json_number)
                continue

            json_bool, string = lex_bool(string)
            if json_bool is not None:
                tokens.append(json_bool)
                continue

            json_null, string = lex_null(string)
            if json_null is not None:
                tokens.append(None)
                continue

            if string[0] in JSON_WHITESPACE:
                string = string[1:]
            elif string[0] in JSON_SYNTAX:
                tokens.append(string[0])
                string = string[1:]
            else:
                raise Exception("Unexpected character: {}".format(string[0]))

        return tokens
