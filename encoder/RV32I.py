# encoder/RV32I.py
from utils.binutils import *
from opcode_map import instruction_map

def encode(instruction_line):
    parts = instruction_line.replace(',', '').split()
    inst = parts[0]
    info = instruction_map.get(inst)

    if not info:
        raise ValueError(f"Unknown instruction: {inst}")

    opcode = info["opcode"]

    if opcode == "0110011":  # R-type: add, sub, ...
        rd = reg_to_bin(parts[1])
        rs1 = reg_to_bin(parts[2])
        rs2 = reg_to_bin(parts[3])
        funct3 = info["funct3"]
        funct7 = info["funct7"]
        return funct7 + rs2 + rs1 + funct3 + rd + opcode

    elif opcode == "0010011":  # I-type: addi, ori, ...
        rd = reg_to_bin(parts[1])
        rs1 = reg_to_bin(parts[2])
        imm = imm_to_bin(int(parts[3]), 12)
        funct3 = info["funct3"]
        funct7 = info.get("funct7", None)
        if funct7:  # slli, srli, srai
            shamt = imm[-5:]
            return funct7 + shamt + rs1 + funct3 + rd + opcode
        return imm + rs1 + funct3 + rd + opcode

    elif opcode == "0000011":  # I-type load
        rd = reg_to_bin(parts[1])
        offset, base = parts[2].split('(')
        rs1 = reg_to_bin(base[:-1])
        imm = imm_to_bin(int(offset), 12)
        funct3 = info["funct3"]
        return imm + rs1 + funct3 + rd + opcode

    elif opcode == "0100011":  # S-type: sw, sb, ...
        rs2 = reg_to_bin(parts[1])
        offset, base = parts[2].split('(')
        rs1 = reg_to_bin(base[:-1])
        imm11_5, imm4_0 = split_imm_s_type(int(offset))
        funct3 = info["funct3"]
        return imm11_5 + rs2 + rs1 + funct3 + imm4_0 + opcode

    elif opcode == "1100011":  # B-type: beq, bne, ...
        rs1 = reg_to_bin(parts[1])
        rs2 = reg_to_bin(parts[2])
        imm = int(parts[3])
        b12, b10_5, b4_1, b11 = split_imm_b_type(imm)
        funct3 = info["funct3"]
        return b12 + b10_5 + rs2 + rs1 + funct3 + b4_1 + b11 + opcode

    elif opcode == "1101111":  # J-type: jal
        rd = reg_to_bin(parts[1])
        imm = split_imm_j_type(int(parts[2]))
        return imm + rd + opcode

    elif opcode == "1100111":  # I-type: jalr
        rd = reg_to_bin(parts[1])
        rs1 = reg_to_bin(parts[2])
        imm = imm_to_bin(int(parts[3]), 12)
        funct3 = info["funct3"]
        return imm + rs1 + funct3 + rd + opcode

    elif opcode == "0110111" or opcode == "0010111":  # U-type: lui, auipc
        rd = reg_to_bin(parts[1])
        imm = split_imm_u_type(int(parts[2]))
        return imm + rd + opcode

    elif inst == "ecall" or inst == "ebreak":
        return instruction_map[inst]["imm"] + "0" * 5 + "000" + "0" * 5 + instruction_map[inst]["opcode"]

    else:
        raise ValueError(f"Unhandled instruction format for: {inst}")
