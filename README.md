# Asambas

### **"As on both sides, with samba in between."**

A slick ARMv7 assembler built for functionality, precision, and a nod to the colleagues from "Waiting For Samba." Written in Python.

## 📖 **Usage**

### **Basic Syntax**

```bash
./asambas [input.s] -o [output.o]
```

### **Examples**

1. Assemble a file named `program.s` into an object file `program.o`:
   ```bash
   ./asambas program.s -o program.o
   ```

2. Assemble a `.asm` file:
   ```bash
   ./asambas source.asm -o module.o 
   ```

### **Notes**

- The **output file** must have a `.o` extension.
- The **input file** must be an existing `.s` or `.asm` file.
- If the arguments or files are incorrect, `asambas` will let you know in style. 🛑

---

## 🔧 **Installation**

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/asambas.git
   cd asambas
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the assembler:
   ```bash
   ./asambas input.s -o output.o
   ```

---

## 🏆 **Contributions**

Got ideas to make `asambas` even better? Open an issue or submit a PR on GitHub! Contributions are always welcome!

---

## ✨ **Future Plans**

- Introduce a disassembler to reverse `.o` files back to `.s`.

---

## License

This project is licensed under the WTFPL License - see the [LICENSE](LICENSE) file for details.
