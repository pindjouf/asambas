#!/usr/bin/env python3

import os
import sys
from enums import *


def lexer(source_code):
    tokens = list()
    opcodes = [str(op) for op in OPCODE]
    directives = [str(directive) for directive in Directive]
    registers = [reg.value[0] for reg in REG]

    with open(source_code, "r") as f:
        file = f.read()
        for line in file.split("\n"):
            line = line.split(";")[0].strip().lower()
            if line:
                line_tokens = list()
                for item in line.split():
                    if item in opcodes or item in directives:
                        line_tokens.append(item)
                    if item.endswith(","):
                        item = item[:-1]
                        if item in registers:
                            line_tokens.append(item)
                tokens.extend(line_tokens)

    return tokens


def args_check(arguments):
    if len(arguments) != 4:
        print("Invalid number of arguments!")
        exit(1)
    elif (
        os.path.exists(arguments[1])
        and arguments[1].endswith((".s", ".asm"))
        and arguments[2] == "-o"
        and arguments[3].endswith(".o")
        and not os.path.exists(arguments[3])
    ):
        return True


def main():
    if (args_check(sys.argv)):
        source_code = sys.argv[1]
        # object_file = sys.argv[3]
        print(lexer(source_code))
    else:
        print("Invalid arguments provided!")
        exit(1)


if __name__ == "__main__":
    main()
