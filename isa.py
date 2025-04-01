instruction_class = {
    "dp": {
        "reg": 0,
        "imm": 1
    }
}

registers = {
    "r0": "0000",
    "r1": "0001",
    "r2": "0010",
    "r3": "0011",
    "r4": "0100",
    "r5": "0101",
    "r6": "0110",
    "r7": "0111",
    "r8": "1000",
    "r9": "1001",
    "r10": "1010",
    "r11": "1011",  # frame pointer
    "r12": "1100",  # intra procedural call
    "r13": "1101",  # stack pointer
    "r14": "1110",  # link register
    "r15": "1111"  # program counter
}

opcodes = {
    "add": "1010"
}

cond = {
    "eq": "0000",
    "ne": "0001",
    "cs": "0010",
    "cc": "0011",
    "mi": "0100",
    "pl": "0101",
    "vs": "0110",
    "vc": "0111",
    "hi": "1000",
    "ls": "1001",
    "ge": "1010",
    "lt": "1011",
    "gt": "1100",
    "le": "1101"
    # "al": 0b1110, # default
}
