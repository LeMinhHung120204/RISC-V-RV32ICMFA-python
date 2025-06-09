# encoder/RV32M.py
from utils.binutils import *
from opcode_map import instruction_map

def encode(instruction_line):
    parts = instruction_line.replace(',', '').split()
    inst = parts[0]
    info = instruction_map.get(inst)

    if not info:
        raise ValueError(f"Unknown instruction: {inst}")

    # RV32M instructions are R-type, opcode is 0110011
    if info["opcode"] == "0110011":
        rd = reg_to_bin(parts[1])    # Destination register
        rs1 = reg_to_bin(parts[2])   # Source register 1
        rs2 = reg_to_bin(parts[3])   # Source register 2
        funct3 = info["funct3"]
        funct7 = info["funct7"]
        return funct7 + rs2 + rs1 + funct3 + rd + info["opcode"]

    raise ValueError(f"Unhandled instruction format for: {inst}")