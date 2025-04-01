import sys
from isa import *

def first_pass(input_file: str) -> tuple[list, dict]:
    line_count = 0
    tracker = dict()
    source_code = list()
    symbol_table = dict()

    with open(input_file, "r") as f:
        file = f.read().split("\n")

        for line in file:
            line_count += 1
            if line:
                if "//" in line:
                    line = line.split("//")[0].strip()
                elif ";" in line:
                    line = line.split(";")[0].strip()

                if line[:1] == ".":
                    match line.split()[1]:
                        case ".data":
                            tracker = {'section': ".data", 'address': 0x0, 'line_count': line_count}
                        case ".text":
                            tracker = {'section': ".text", 'address': 0x0, 'line_count': line_count}
                        case _:
                            pass

                elif line[-1:] == ":":
                    symbol_table.update({f'{line[:-1]}': f'{hex(tracker['address'])}'})

                if tracker:
                    if tracker['section'] == ".data":
                        if line.split()[1][:1] == "." and line.split()[1] != ".text" and line.split()[1] != ".data":
                            tracker['line_count'] = line_count
                            match line.split()[1]:
                                case ".byte":
                                    tracker['address'] += 0x1
                                case ".hword" | ".short":
                                    tracker['address'] += 0x2
                                case ".word":
                                    tracker['address'] += 0x4
                                case ".ascii":
                                    string = line.split()[2][1:-1]
                                    if "\\n" in string or "\\t" in string or "\\r" in string:
                                        str_len = len(string) - 1
                                        tracker['address'] += str_len
                                case ".space" | ".skip":
                                    pass
                                case _:
                                    pass

                    elif tracker['section'] == ".text":
                        tracker['line_count'] = line_count
                        if not ".text" in line.split() and line[-1:] != ":":
                            tracker['address'] += 0x4

                line = line.strip().split()
                tracker['line'] = line

                for i in line:
                    if "r" in i and "," in i:
                        line[line.index(i)] = line[line.index(i)][:-1]
                source_code.append(tracker.copy())

    return source_code, symbol_table

def main():
    source_code, symbol_table = first_pass(sys.argv[1])

    for line in source_code:
        print(line)

    print(f"\nSymbol table: {symbol_table}")

if __name__ == "__main__":
    main()

