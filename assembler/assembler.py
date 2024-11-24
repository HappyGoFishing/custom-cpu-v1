import sys, os

instruction_lengths = {
    "H": 5,              # Only the opcode (5 bits).
    "LI": 42,            # Opcode (5) + $DR (5) + Immediate (32).
    "LR": 15,            # Opcode (5) + $DR (5) + RX (5).
    "J": 37,             # Opcode (5) + $LINE (32).
    "JE": 47,            # Opcode (5) + $LINE (32) + RX(5) + RY(5)
    "JNE": 47,           # Opcode (5) + $LINE (32) + RX(5) + RY(5)
    "JL": 47,            # Opcode (5) + $LINE (32) + RX(5) + RY(5)
    "JG": 47,            # Opcode (5) + $LINE (32) + RX(5) + RY(5)
    "ADDR": 20,          # Opcode (5) + $DR (5) + RX (5) + RY (5).
    "ADDI": 47,          # Opcode (5) + $DR (5) + RX (5) + Immediate (32).
    "SUBR": 20,          # Opcode (5) + $DR (5) + RX (5) + RY (5).
    "SUBI": 47,          # Opcode (5) + $DR (5) + RX (5) + Immediate (32).
    "MULR": 20,          # Opcode (5) + $DR (5) + RX (5) + RY (5).
    "MULI": 47,          # Opcode (5) + $DR (5) + RX (5) + Immediate (32).
    "DIVR": 20,          # Opcode (5) + $DR (5) + RX (5) + RY (5).
    "DIVI": 47,          # Opcode (5) + $DR (5) + RX (5) + Immediate (32).
}

op_codes = {
    "H"    : "00000",
    "LI"   : "00001",
    "LR"   : "00010",
    "J"    : "00011",
    "JE"   : "00100",
    "JNE"  : "00101",
    "JL"   : "00110",
    "JG"   : "00111",
    "ADDR" : "01000",
    "ADDI" : "01001",
    "SUBR" : "01010",
    "SUBI" : "01011",
    "MULR" : "01100",
    "MULI" : "01101",
    "DIVR" : "01110",
    "DIVI" : "01111",
}

reg_codes = {
    "PC": "00000", 
    "R0": "00001",
    "R1": "00010",
    "R2": "00011",
    "R3": "00100",
    "R4": "00101",
    "R5": "00110",
    "R6": "00111",
    "R7": "01000",
}

def int_to_le_32(num, sign) -> str: #turn regular int into a little endian s32 binary string
    # make sure number is valid s32 or u32
    if sign:
        if not (-2147483648 <= num <= 2147483647):
            raise ValueError(f"{num} out of range for s32")
    else:
        if not (0 <= num <= 4294967295):
            raise ValueError(f"{num} out of range for u32")
    
    little_endian_bytes = num.to_bytes(4, byteorder='little', signed=sign)
    binary_string = ''.join(f'{byte:08b}' for byte in little_endian_bytes)
    return binary_string


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as sourcefile:
            sourcecode = sourcefile.read().strip()
    else:
        print("no source file provided")
        sys.exit(0)
    instructions = sourcecode.split("\n")
    outbuffer = []

    for line_num, line in enumerate(instructions):
        tokens = line.split()
        opcode = tokens[0].upper()  

        match opcode:
            case "H": 
                outbuffer.append(op_codes["H"])
            
            case "LI":
                if len(tokens) == 3:
                    reg_code = reg_codes[tokens[1].upper()]
                    imval = int_to_le_32(int(tokens[2]), sign=True) 
                    outbuffer.append(f"{op_codes[opcode]}{reg_code}{imval}")
                    
                    
            case "LR":
                if len(tokens) == 3:
                    destreg = reg_codes[tokens[1].upper()]
                    srcreg = reg_codes[tokens[2].upper()]
                    outbuffer.append(f"{op_codes[opcode]}{destreg}{srcreg}")
                
            case "J":
                if len(tokens) == 2:
                    ln = int_to_le_32(int(tokens[1]), sign=False)
                    outbuffer.append(f"{op_codes[opcode]}{ln}")

            case "JE": 
                if len(tokens) == 4:
                    ln = int_to_le_32(int(tokens[1]), sign=False)
                    rx = reg_codes[tokens[2].upper()]
                    ry = reg_codes[tokens[3].upper()]
                    outbuffer.append(f"{op_codes[opcode]}{rx}{ry}")
            case "JNE":
                if len(tokens) == 4:
                    ln = int_to_le_32(int(tokens[1]), sign=False)
                    rx = reg_codes[tokens[2].upper()]
                    ry = reg_codes[tokens[3].upper()]
                    outbuffer.append(f"{op_codes[opcode]}{rx}{ry}")                
            case "JL": 
                if len(tokens) == 4:
                    ln = int_to_le_32(int(tokens[1]), sign=False)
                    rx = reg_codes[tokens[2].upper()]
                    ry = reg_codes[tokens[3].upper()]
                    outbuffer.append(f"{op_codes[opcode]}{rx}{ry}")
            case "JG": 
                if len(tokens) == 4:
                    ln = int_to_le_32(int(tokens[1]), sign=False)
                    rx = reg_codes[tokens[2].upper()]
                    ry = reg_codes[tokens[3].upper()]
                    outbuffer.append(f"{op_codes[opcode]}{rx}{ry}")
            case "ADDR": 
                pass
            case "ADDI": 
                pass
            case "SUBR": 
                pass
            case "SUBI": 
                pass
            case "MULR": 
                pass
            case "MULI": 
                pass
            case "DIVR": 
                pass
            case "DIVI": 
                pass
            
            case _:
                print(f"ERROR: unknown opcode \"{opcode}\", failed to assemble (line {line_num + 1})")
                sys.exit(1)

    for line_num, line in enumerate(outbuffer):
        print(f"(line {line_num + 1}): {line}: \"{instructions[line_num].upper()}\"")


if len(sys.argv) > 2: 
    output_bintxt_name = os.path.splitext(sys.argv[2])[0] + ".bin.txt"
    output_bin_name = os.path.splitext(sys.argv[2])[0] + ".bin"
else:
    output_bintxt_name = os.path.splitext(sys.argv[1])[0] + ".bin.txt"
    output_bin_name = os.path.splitext(sys.argv[1])[0] + ".bin"
    
print(f"output file (text-readable) {output_bintxt_name}")
with open(output_bintxt_name, "w") as fb:
    fb.write("".join(outbuffer))
