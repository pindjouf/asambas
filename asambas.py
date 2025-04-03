import sys
from isa import *

def first_pass(input_file: str) -> tuple[list, dict]:
    line_count = 0
    tracker = dict()
    source_code = list()
    symbol_table = dict()
    just_passed_label = bool()

    with open(input_file, "r") as f:
        file = f.read().split("\n")

        for line in file:
            line_count += 1
            if line:
                
                # comment management
                if "//" in line:
                    line = line.split("//")[0].strip()
                elif ";" in line:
                    line = line.split(";")[0].strip()
                elif "@" in line:
                    line = line.split("@")[0].strip()

                # section management & tracker init
                if len(line.split()) == 2:
                    if line.split()[0] == ".section":
                        match line.split()[1]:
                            case ".data":
                                tracker = {'section': ".data", 'current_mode': ".arm", 'address': 0x0, 'line_count': line_count}
                            case ".text":
                                tracker = {'section': ".text", 'current_mode': ".arm", 'address': 0x0, 'line_count': line_count}
                            case ".bss":
                                tracker = {'section': ".bss", 'current_mode': ".arm", 'address': 0x0, 'line_count': line_count}
                            case ".rodata":
                                tracker = {'section': ".rodata", 'current_mode': ".arm", 'address': 0x0, 'line_count': line_count}
                            case _:
                                pass

                # address management
                if tracker:
                    tracker['line_count'] = line_count

                    if tracker['section'] == ".data":
                        if line.split()[1][:1] == "." and line.split()[1] != ".data":
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
                        if ".thumb" in line.split():
                            tracker['current_mode'] = ".thumb"
                        elif ".arm" in line.split():
                            tracker['current_mode'] = ".arm"

                        if ".text" in line.split():
                            pass
                        elif line[-1:] == ":":
                            just_passed_label = True

                            if tracker['current_mode'] == ".thumb":
                                tracker['address'] += 0x2
                            else:
                                tracker['address'] += 0x4
                        else:
                            if line:
                                if just_passed_label == True:
                                    just_passed_label = False
                                else:
                                    if tracker['current_mode'] == ".thumb":
                                        tracker['address'] += 0x2
                                    else:
                                        tracker['address'] += 0x4

                # symbol table management
                if line:
                    if line.split()[0][-1:] == ":":
                        symbol_table.update({f'{line.split()[0][:-1]}': f'{tracker['address']}'})

                # make clean list of vals in line
                line = line.strip().split()
                tracker['line'] = line

                # clean up regs in list
                for i in line:
                    if "r" in i and "," in i:
                        line[line.index(i)] = line[line.index(i)][:-1]

                # add copy of current tracker vals to list
                if line:
                    source_code.append(tracker.copy())

    return source_code, symbol_table

def main():
    source_code, symbol_table = first_pass(sys.argv[1])

    for line in source_code:
        if 'address' in line:
            line['address'] = hex(line['address'])
            print(line)
        else:
            print(line)

    print(f"\nSymbol table: {symbol_table}")

if __name__ == "__main__":
    main()
