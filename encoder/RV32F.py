from opcode_map import f_type_instructions
from utils.binutils import reg_to_bin, float_reg_to_bin, imm_to_bin

instruction_map = f_type_instructions  # cho main.py gọi

def encode(line):
    tokens = line.replace(",", "").split()
    mnemonic = tokens[0]
    inst = instruction_map[mnemonic]
    opcode = inst["opcode"]

    # Fused multiply-add (4 operands)
    if mnemonic in ["fmadd.s", "fmsub.s", "fnmadd.s", "fnmsub.s"]:
        rd = float_reg_to_bin(tokens[1])
        rs1 = float_reg_to_bin(tokens[2])
        rs2 = float_reg_to_bin(tokens[3])
        rs3 = float_reg_to_bin(tokens[4])
        funct2 = inst["funct2"]
        # Format: rs3 | funct2 | rs2 | rs1 | funct3 | rd | opcode
        return rs3 + funct2 + rs2 + rs1 + "000" + rd + opcode

    # Load/store (flw/fsw)
    elif mnemonic in ["flw", "fsw"]:
        rd_or_rs2 = reg_to_bin(tokens[1])
        imm_part, rs1 = tokens[2].split("(")
        rs1 = rs1.strip(")")
        rs1_bin = reg_to_bin(rs1)
        imm_bin = imm_to_bin(int(imm_part), 12)
        funct3 = inst["funct3"]

        if mnemonic == "flw":  # I-type
            return imm_bin + rs1_bin + funct3 + rd_or_rs2 + opcode
        else:  # fsw - S-type
            imm_hi, imm_lo = imm_bin[:7], imm_bin[7:]
            return imm_hi + rd_or_rs2 + rs1_bin + funct3 + imm_lo + opcode

    # R-type floating point (3 operands, all float)
    elif mnemonic in ["fadd.s", "fsub.s", "fmul.s", "fdiv.s", "fsqrt.s", 
                      "fsgnj.s", "fsgnjn.s", "fsgnjx.s", "fmin.s", "fmax.s"]:
        rd = float_reg_to_bin(tokens[1])
        rs1 = float_reg_to_bin(tokens[2])
        rs2 = float_reg_to_bin(tokens[3])
        funct3 = inst["funct3"]
        funct7 = inst["funct7"]
        return funct7 + rs2 + rs1 + funct3 + rd + opcode

    # Compare or classify (rd = x, rs1 = float)
    elif mnemonic in ["feq.s", "flt.s", "fle.s", "fclass.s"]:
        rd = reg_to_bin(tokens[1])
        rs1 = float_reg_to_bin(tokens[2])
        funct3 = inst["funct3"]
        funct7 = inst["funct7"]
        rs2 = "00000"  # unused
        return funct7 + rs2 + rs1 + funct3 + rd + opcode

    # Conversion (float <-> int)
    elif mnemonic.startswith("fcvt."):
        rd = float_reg_to_bin(tokens[1]) if mnemonic.startswith("fcvt.s") else reg_to_bin(tokens[1])
        rs1 = reg_to_bin(tokens[2]) if mnemonic.startswith("fcvt.s") else float_reg_to_bin(tokens[2])
        funct3 = inst["funct3"]
        funct7 = inst["funct7"]
        rs2 = "00000"  # always 0
        return funct7 + rs2 + rs1 + funct3 + rd + opcode

    else:
        raise ValueError(f"Unhandled instruction format for: {mnemonic}")
