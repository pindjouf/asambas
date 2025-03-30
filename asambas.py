from isa import *

# go to A5.2.3 for Data-processing (immediate) documentation
with open("test.s", "r") as f:
    line = f.read().split(";")[0].split()

    for mnemonic in line:
        line[line.index(mnemonic)] = mnemonic.lower()

    opcode = line[0]
    second_op = line[1].split(",")[0]
    imm = line[2][1:]

    # Data-processing (immediate) & MOV in encoding A2
    if opcode[-2:] in list(cond.keys()):
        cond_field = cond.get(opcode[-2:])
        category = "001"
        encoding_type = "1101"
        s_bit = "0"
        first_op = "0000"
        second_op = registers.get(second_op)
        imm = str(bin(int(imm)))[2:]

        if 12 - len(imm) != 0:
            difference = "0" * (12 - len(imm))
            output = int(cond_field + category + encoding_type + s_bit + first_op + second_op + difference + imm, 2).to_bytes(4, byteorder='big')
            print(f"{line} = {cond_field + category + encoding_type + s_bit + first_op + second_op + difference + imm}")
            # with open("test.bin", "wb") as f:
            #     f.write(output)
        else:
            print(f"{line} = {cond_field + category + encoding_type + s_bit + first_op + second_op + imm}")
    else:
        print(f"{opcode} doesn't have any conditions therefore it's AL or 0b1110")
