from enum import Enum, auto

class OPCODE(Enum):
    # Arithmetic operations
    ADD = auto()     # Add
    ADC = auto()     # Add with Carry
    SUB = auto()     # Subtract
    SBC = auto()     # Subtract with Carry
    RSB = auto()     # Reverse Subtract
    RSC = auto()     # Reverse Subtract with Carry
    MUL = auto()     # Multiply
    MLA = auto()     # Multiply Accumulate
    
    # Logiauto()perations
    AND = auto()     # Bitwise AND
    EOR = auto()     # Bitwise XOR
    ORR = auto()     # Bitwise OR
    BIC = auto()     # Bit Clear
    
    # Compauto()n operations
    CMP = auto()     # Compare
    CMN = auto()     # Compare Negative
    TST = auto()     # Test bits
    TEQ = auto()     # Test Equivalence
    
    # Move operations
    MOV = auto()     # Move
    MVN = auto()     # Move Not (bitwise NOT)
    
    # Memory operations
    LDR = auto()     # Load Register
    LDRB = auto()   # Load Register Byte
    LDRH = auto()   # Load Register Halfword
    STR = auto()   # Store Register
    STRB = auto()   # Store Register Byte
    STRH = auto()   # Store Register Halfword
    
    # Multiple register transfer
    LDM = auto()     # Load Multiple
    STM = auto()     # Store Multiple
    PUSH = auto()   # Push registers
    POP = auto()     # Pop registers
    
    # Branch instructions
    B = auto()         # Branch
    BL = auto()       # Branch with Link
    BX = auto()       # Branch and Exchange
    BLX = auto()     # Branch with Link and Exchange
    
    # Status register access
    MRS = auto()     # Move from Status Register
    MSR = auto()     # Move to Status Register
    
    # Barrel shifter operations
    LSL = auto()     # Logical Shift Left
    LSR = auto()     # Logical Shift Right
    ASR = auto()     # Arithmetic Shift Right
    ROR = auto()     # Rotate Right
    RRX = auto()     # Rotate Right with Extend
    
    # System and coprocessor
    SVC = auto()     # Supervisor Call (formerly SWI)
    CDP = auto()     # Coprocessor Data Processing
    LDC = auto()     # Load Coprocessor
    STC = auto()     # Store Coprocessor
    MCR = auto()     # Move to Coprocessor from ARM Register
    MRC = auto()     # Move to ARM Register from Coprocessor
    
    def __str__(self):
        return self.name.lower()

class COND(Enum):
    # Basic equality conditions
    EQ = ('eq', 0b0000)    # Equal (Z=1)
    NE = ('ne', 0b0001)    # Not Equal (Z=0)
    
    # Carry flag conditions
    CS = ('cs', 0b0010)    # Carry Set (C=1), also known as HS (Higher or Same)
    CC = ('cc', 0b0011)    # Carry Clear (C=0), also known as LO (Lower)
    
    # Negative flag conditions
    MI = ('mi', 0b0100)    # Minus/Negative (N=1)
    PL = ('pl', 0b0101)    # Plus/Positive or Zero (N=0)
    
    # Overflow flag conditions
    VS = ('vs', 0b0110)    # Overflow Set (V=1)
    VC = ('vc', 0b0111)    # Overflow Clear (V=0)
    
    # Unsigned comparison conditions
    HI = ('hi', 0b1000)    # Higher (C=1 and Z=0)
    LS = ('ls', 0b1001)    # Lower or Same (C=0 or Z=1)
    
    # Signed comparison conditions
    GE = ('ge', 0b1010)    # Greater than or Equal (N=V)
    LT = ('lt', 0b1011)    # Less Than (N≠V)
    GT = ('gt', 0b1100)    # Greater Than (Z=0 and N=V)
    LE = ('le', 0b1101)    # Less than or Equal (Z=1 or N≠V)
    
    # Always/Never conditions
    AL = ('al', 0b1110)    # Always (default)
    NV = ('nv', 0b1111)    # Never (reserved)

class REG(Enum):
    # General purpose registers
    R0 = ('r0', 0b0000)     # First param/result
    R1 = ('r1', 0b0001)     # Second param
    R2 = ('r2', 0b0010)     # Third param
    R3 = ('r3', 0b0011)     # Fourth param
    R4 = ('r4', 0b0100)     # Variable 1
    R5 = ('r5', 0b0101)     # Variable 2
    R6 = ('r6', 0b0110)     # Variable 3
    R7 = ('r7', 0b0111)     # Variable 4 or Syscall number
    R8 = ('r8', 0b1000)     # Variable 5
    R9 = ('r9', 0b1001)     # Platform register/Variable 6
    R10 = ('r10', 0b1010)   # Variable 7
    
    # Special purpose registers
    R11 = ('r11', 0b1011, 'fp')   # Frame Pointer
    R12 = ('r12', 0b1100, 'ip')   # Intra-Procedure scratch
    R13 = ('r13', 0b1101, 'sp')   # Stack Pointer
    R14 = ('r14', 0b1110, 'lr')   # Link Register
    R15 = ('r15', 0b1111, 'pc')   # Program Counter
    
    # Status registers
    CPSR = ('cpsr', None)    # Current Program Status Register
    SPSR = ('spsr', None)    # Saved Program Status Register

class Directive(Enum):
    ARM = auto()
    THUMB = auto()
    CODE_32 = auto()
    AREA = auto()
    SPACE = auto()
    ALIGN = auto()
    BYTE = auto()
    WORD = auto()
    ASCII = auto()
    ASCIZ = auto()
    EQU = auto()
    GLOBAL = auto()
    MACRO = auto()
    ENDM = auto()
    IF = auto()
    ELSE = auto()
    ENDIF = auto()
    REPT = auto()
    ENDR = auto()
    ENTRY = auto()
    END = auto()
    INCLUDE = auto()
    SECTION = auto()

    def __str__(self):
        return f".{self.name.lower()}"


class TokenType(Enum):
    Im = 1
    Label = 2
    Pointer = 3
    Register = 4
    Directive = 5
    Instruction = 6
