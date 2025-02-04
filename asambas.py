#!/usr/bin/env python3

import os
import sys
from enums import *


def lexer(source_code):
    op_names = [op.value for op in OP]
    with open(source_code, "r") as f:
        file = f.read()
        for line in file.split("\n"):
            line = line.split(";")[0].strip().lower()
            if line:
                if any(line.startswith(op) for op in op_names):
                    line = line.split()
                    print(f"Found {line[0]} in line: '{line}'")

def instruction_decoder(instruction):


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
        lexer(source_code)
    else:
        print("Invalid arguments provided!")
        exit(1)


if __name__ == "__main__":
    main()
