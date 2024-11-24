import sys

op_codes = {
    "h"    : "00000",
    "li"   : "00001",
    "lr"   : "00010",
    "j"    : "00011",
    "je"   : "00100",
    "jne"  : "00101",
    "jl"   : "00110",
    "jg"   : "00111",
    "addr" : "01000",
    "addi" : "01001",
    "subr" : "01010",
    "subi" : "01011",
    "mulr" : "01100",
    "muli" : "01101",
    "divr" : "01110",
    "divi" : "01111",
}

reg_codes = {
    "PC": "00000", 
    "r0": "00001",
    "r1": "00010",
    "r2": "00011",
    "r3": "00100",
    "r4": "00101",
    "r5": "00110",
    "r6": "00111",
    "r7": "01000",
}

if __name__ == "__main__":

    with open(sys.argv[1], "r") as sourcefile:
        sourcecode = sourcefile.read().lower().strip()

    instructions = sourcecode.split("\n")
    outbuffer = []

    for line_num, line in enumerate(instructions):
        tokens = line.split()
        opcode = tokens[0]

        outbuffer.append(op_codes[opcode])
        
        match opcode:
            case "h": pass
            
            case "li":
                if len(tokens) == 3:
                    dest = tokens[1]
                    outbuffer[line_num] += reg_codes[dest]
            case "lr":
                if len(tokens) == 3:
                    dest = tokens[1]
                    reg = tokens[2]
                    outbuffer[line_num] += reg_codes[dest] + reg_codes[reg]
                    
            case "j":
                pass
            case "je":
                pass
            case "jne":
                pass
            case "jl":
                pass
            case "jg":
                pass
            case "addr":
                pass
            case "addi":
                pass
            case "subr":
                pass
            case "subi":
                pass
            case "mulr":
                pass
            case "muli":
                pass
            case "divr":
                pass
            case "divi":
                pass
            case _:
                print(f"ERROR: unknown opcode \"{opcode}\", failed to assemble (line {line_num + 1})")
                sys.exit(1)

    for line_num, line in enumerate(outbuffer):
        print(f"(line {line_num + 1}): {line}")
