#!/usr/bin/env python3

import os
import sys
from rich.console import Console
from rich.style import Style
from rich.text import Text

console = Console()
error_style = Style(color="#fb4934", bold=True)
info_style = Style(color="#fabd2f", bold=True)
header_style = Style(color="#83a598", bold=True)
ascii_style = Style(color="#b8bb26", bold=True)

ASAMBAS_ASCII = r"""
 █████╗ ███████╗ █████╗ ███╗   ███╗██████╗  █████╗ ███████╗
██╔══██╗██╔════╝██╔══██╗████╗ ████║██╔══██╗██╔══██╗██╔════╝
███████║███████╗███████║██╔████╔██║███████║███████║███████╗
██╔══██║╚════██║██╔══██║██║╚██╔╝██║██║  ██║██╔══██║╚════██║
██║  ██║███████║██║  ██║██║ ╚═╝ ██║██████╔╝██║  ██║███████║
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝
"""

def print_ascii_banner():
    """Print the `asambas` banner in ASCII."""
    console.print(ASAMBAS_ASCII, style=ascii_style)

def print_error(message):
    """Pretty print an error message."""
    text = Text("ERROR: ", style=error_style) + Text(message, style=info_style)
    console.print(text)

def print_usage():
    """Pretty print the correct usage instructions."""
    console.print(Text("USAGE:", style=header_style))
    console.print("  ./asambas [input.s] -o [output.o]\n", style=info_style)
    console.print("EXAMPLES:", style=header_style)
    console.print("  ./asambas program.s -o program.o", style=info_style)
    console.print("  ./asambas source.asm -o module.o\n", style=info_style)
    console.print(Text("NOTES:", style=header_style))
    console.print("  - The output file must have a .o extension.", style=info_style)
    console.print("  - The input file must be .s or .asm and exist.", style=info_style)

def lexer(source_code):
    with open(source_code, "r") as f:
        file = f.read()
        for line in file.split("\n"):
            line = line.split(";")[0].strip()
            if line:
                print(line.split())

def main():
    print_ascii_banner()

    if len(sys.argv) != 4:
        print_error("Invalid number of arguments!")
        print_usage()
        exit(1)
    elif (
        os.path.exists(sys.argv[1])
        and sys.argv[1].endswith((".s", ".asm"))
        and sys.argv[2] == "-o"
        and sys.argv[3].endswith(".o")
        and not os.path.exists(sys.argv[3])
    ):
        source_code = sys.argv[1]
        object_file = sys.argv[3]
        lexer(source_code)
    else:
        print_error("Invalid arguments provided!")
        print_usage()
        exit(1)

if __name__ == "__main__":
    main()
