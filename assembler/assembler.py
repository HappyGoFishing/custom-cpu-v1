import sys

# Capitalized opcodes and regcodes
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

if __name__ == "__main__":

    with open(sys.argv[1], "r") as sourcefile:
        sourcecode = sourcefile.read().strip()

    instructions = sourcecode.split("\n")
    outbuffer = []

    for line_num, line in enumerate(instructions):
        tokens = line.split()
        opcode = tokens[0].upper()  # Convert opcode to uppercase to match the dictionary

        if opcode in op_codes:
            outbuffer.append(op_codes[opcode])
        else:
            print(f"ERROR: unknown opcode \"{opcode}\", failed to assemble (line {line_num + 1})")
            sys.exit(1)
        
        match opcode:
            case "H": 
                pass
            
            case "LI":
                if len(tokens) == 3:
                    dest = tokens[1].upper()  # Convert register to uppercase
                    outbuffer[line_num] += reg_codes[dest]
            
            case "LR":
                if len(tokens) == 3:
                    dest = tokens[1].upper()
                    reg = tokens[2].upper()
                    outbuffer[line_num] += reg_codes[dest] + reg_codes[reg]
                    
            case "J": 
                pass
            case "JE": 
                pass
            case "JNE": 
                pass
            case "JL": 
                pass
            case "JG": 
                pass
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

outfile = str()

if len(sys.argv) > 2: 
    outfile = sys.argv[2]
else:
    outfile = "as_out"

with open(outfile, "w") as fb:
    fb.write("".join(outbuffer))
