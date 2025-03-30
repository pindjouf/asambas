with open("test.bin", "rb") as f:
    file = f.read()
    print(''.join(format(byte, '08b') for byte in file))
