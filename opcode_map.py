# opcode_map.py

#============================================================================================
# RV32IBaseIntegerInstructions
# R-Type instructions
r_type_instructions = {
    "add":   {"opcode": "0110011", "funct3": "000", "funct7": "0000000"},
    "sub":   {"opcode": "0110011", "funct3": "000", "funct7": "0100000"},
    "xor":   {"opcode": "0110011", "funct3": "100", "funct7": "0000000"},
    "or":    {"opcode": "0110011", "funct3": "110", "funct7": "0000000"},
    "and":   {"opcode": "0110011", "funct3": "111", "funct7": "0000000"},
    "sll":   {"opcode": "0110011", "funct3": "001", "funct7": "0000000"},
    "srl":   {"opcode": "0110011", "funct3": "101", "funct7": "0000000"},
    "sra":   {"opcode": "0110011", "funct3": "101", "funct7": "0100000"},
    "slt":   {"opcode": "0110011", "funct3": "010", "funct7": "0000000"},
    "sltu":  {"opcode": "0110011", "funct3": "011", "funct7": "0000000"},
}

# I-Type instructions
i_type_instructions = {
    "addi":  {"opcode": "0010011", "funct3": "000"},
    "xori":  {"opcode": "0010011", "funct3": "100"},
    "ori":   {"opcode": "0010011", "funct3": "110"},
    "andi":  {"opcode": "0010011", "funct3": "111"},
    "slli":  {"opcode": "0010011", "funct3": "001", "funct7": "0000000"},
    "srli":  {"opcode": "0010011", "funct3": "101", "funct7": "0000000"},
    "srai":  {"opcode": "0010011", "funct3": "101", "funct7": "0100000"},
    "slti":  {"opcode": "0010011", "funct3": "010"},
    "sltiu": {"opcode": "0010011", "funct3": "011"},

    "lb":    {"opcode": "0000011", "funct3": "000"},
    "lh":    {"opcode": "0000011", "funct3": "001"},
    "lw":    {"opcode": "0000011", "funct3": "010"},
    "lbu":   {"opcode": "0000011", "funct3": "100"},
    "lhu":   {"opcode": "0000011", "funct3": "101"},
}

# S-Type instructions
s_type_instructions = {
    "sb":    {"opcode": "0100011", "funct3": "000"},
    "sh":    {"opcode": "0100011", "funct3": "001"},
    "sw":    {"opcode": "0100011", "funct3": "010"},
}

# B-Type instructions
b_type_instructions = {
    "beq":   {"opcode": "1100011", "funct3": "000"},
    "bne":   {"opcode": "1100011", "funct3": "001"},
    "blt":   {"opcode": "1100011", "funct3": "100"},
    "bge":   {"opcode": "1100011", "funct3": "101"},
    "bltu":  {"opcode": "1100011", "funct3": "110"},
    "bgeu":  {"opcode": "1100011", "funct3": "111"},
}

# J-Type instructions
j_type_instructions = {
    "jal":   {"opcode": "1101111"},
}

# I-Type (special) instructions
jalr_instruction = {
    "jalr":  {"opcode": "1100111", "funct3": "000"},
}

# U-Type instructions
u_type_instructions = {
    "lui":   {"opcode": "0110111"},
    "auipc": {"opcode": "0010111"},
}

# System instructions (ecall, ebreak)
system_instructions = {
    "ecall":  {"opcode": "1110011", "funct3": "000", "imm": "000000000000"},
    "ebreak": {"opcode": "1110011", "funct3": "000", "imm": "000000000001"},
}

#============================================================================================
# RV32M Multiply Extension
m_type_instructions = {
    "mul":    {"opcode": "0110011", "funct3": "000", "funct7": "0000001"},
    "mulh":   {"opcode": "0110011", "funct3": "001", "funct7": "0000001"},
    "mulhsu": {"opcode": "0110011", "funct3": "010", "funct7": "0000001"},
    "mulhu":  {"opcode": "0110011", "funct3": "011", "funct7": "0000001"},
    "div":    {"opcode": "0110011", "funct3": "100", "funct7": "0000001"},
    "divu":   {"opcode": "0110011", "funct3": "101", "funct7": "0000001"},
    "rem":    {"opcode": "0110011", "funct3": "110", "funct7": "0000001"},
    "remu":   {"opcode": "0110011", "funct3": "111", "funct7": "0000001"},
}

#============================================================================================
# RV32A Atomic Extension
a_type_instructions = {
    "lr.w":     {"opcode": "0101111", "funct3": "010", "funct5": "00010"},
    "sc.w":     {"opcode": "0101111", "funct3": "010", "funct5": "00011"},
    "amoswap.w": {"opcode": "0101111", "funct3": "010", "funct5": "00001"},
    "amoadd.w":  {"opcode": "0101111", "funct3": "010", "funct5": "00000"},
    "amoand.w":  {"opcode": "0101111", "funct3": "010", "funct5": "01100"},
    "amoor.w":   {"opcode": "0101111", "funct3": "010", "funct5": "01000"},
    "amoxor.w":  {"opcode": "0101111", "funct3": "010", "funct5": "00100"},
    "amomax.w":  {"opcode": "0101111", "funct3": "010", "funct5": "10100"},
    "amomin.w":  {"opcode": "0101111", "funct3": "010", "funct5": "10000"},
}


#============================================================================================
# Floating-Point Instructions (RV32F)
f_type_instructions = {
    # Load/Store
    "flw":       {"opcode": "0000111", "funct3": "010"},
    "fsw":       {"opcode": "0100111", "funct3": "010"},

    # Fused multiply-add
    "fmadd.s":   {"opcode": "1000011", "funct2": "00"},
    "fmsub.s":   {"opcode": "1000111", "funct2": "00"},
    "fnmadd.s":  {"opcode": "1001011", "funct2": "00"},
    "fnmsub.s":  {"opcode": "1001111", "funct2": "00"},

    # Basic FP arithmetic
    "fadd.s":    {"opcode": "1010011", "funct7": "0000000", "funct3": "000"},
    "fsub.s":    {"opcode": "1010011", "funct7": "0000100", "funct3": "000"},
    "fmul.s":    {"opcode": "1010011", "funct7": "0001000", "funct3": "000"},
    "fdiv.s":    {"opcode": "1010011", "funct7": "0001100", "funct3": "000"},
    "fsqrt.s":   {"opcode": "1010011", "funct7": "0101100", "funct3": "000"},

    # Sign manipulation
    "fsgnj.s":   {"opcode": "1010011", "funct7": "0010000", "funct3": "000"},
    "fsgnjn.s":  {"opcode": "1010011", "funct7": "0010000", "funct3": "001"},
    "fsgnjx.s":  {"opcode": "1010011", "funct7": "0010000", "funct3": "010"},

    # Min/Max
    "fmin.s":    {"opcode": "1010011", "funct7": "0010100", "funct3": "000"},
    "fmax.s":    {"opcode": "1010011", "funct7": "0010100", "funct3": "001"},

    # Integer <-> Float
    "fcvt.s.w":   {"opcode": "1010011", "funct7": "1100000", "funct3": "000"},
    "fcvt.s.wu":  {"opcode": "1010011", "funct7": "1100000", "funct3": "001"},
    "fcvt.w.s":   {"opcode": "1010011", "funct7": "1101000", "funct3": "000"},
    "fcvt.wu.s":  {"opcode": "1010011", "funct7": "1101000", "funct3": "001"},

    # Moves
    "fmv.x.w":    {"opcode": "1010011", "funct7": "1110000", "funct3": "000"},
    "fmv.w.x":    {"opcode": "1010011", "funct7": "1111000", "funct3": "000"},

    # Comparisons
    "feq.s":      {"opcode": "1010011", "funct7": "1010000", "funct3": "010"},
    "flt.s":      {"opcode": "1010011", "funct7": "1010000", "funct3": "001"},
    "fle.s":      {"opcode": "1010011", "funct7": "1010000", "funct3": "000"},

    # Classification
    "fclass.s":   {"opcode": "1010011", "funct7": "1110000", "funct3": "001"},
}

#============================================================================================
# RV32C Compressed Extension
compressed_instructions = {
    "c.lwsp":      {"opcode": "10", "funct3": "010", "format": "CI"},
    "c.swsp":      {"opcode": "10", "funct3": "110", "format": "CSS"},
    "c.lw":        {"opcode": "00", "funct3": "010", "format": "CL"},
    "c.sw":        {"opcode": "00", "funct3": "110", "format": "CS"},
    "c.j":         {"opcode": "01", "funct3": "101", "format": "CJ"},
    "c.jal":       {"opcode": "01", "funct3": "001", "format": "CJ"},
    "c.jr":        {"opcode": "10", "funct3": "000", "format": "CR"},
    "c.jalr":      {"opcode": "10", "funct3": "001", "format": "CR"},
    "c.beqz":      {"opcode": "01", "funct3": "110", "format": "CB"},
    "c.bnez":      {"opcode": "01", "funct3": "111", "format": "CB"},
    "c.li":        {"opcode": "01", "funct3": "010", "format": "CI"},
    "c.lui":       {"opcode": "01", "funct3": "011", "format": "CI"},
    "c.addi":      {"opcode": "01", "funct3": "000", "format": "CI"},
    "c.addi16sp":  {"opcode": "01", "funct3": "011", "format": "CI"},
    "c.addi4spn":  {"opcode": "00", "funct3": "000", "format": "CIW"},
    "c.slli":      {"opcode": "10", "funct3": "000", "format": "CI"},
    "c.srli":      {"opcode": "01", "funct3": "100", "format": "CB"},
    "c.srai":      {"opcode": "01", "funct3": "100", "format": "CB"},
    "c.andi":      {"opcode": "01", "funct3": "100", "format": "CB"},
    "c.mv":        {"opcode": "10", "funct3": "100", "format": "CR"},
    "c.add":       {"opcode": "10", "funct3": "100", "format": "CR"},
    "c.and":       {"opcode": "01", "funct3": "100", "funct2": "11", "format": "CS"},
    "c.or":        {"opcode": "01", "funct3": "100", "funct2": "10", "format": "CS"},
    "c.xor":       {"opcode": "01", "funct3": "100", "funct2": "01", "format": "CS"},
    "c.sub":       {"opcode": "01", "funct3": "100", "funct2": "00", "format": "CS"},
    "c.nop":       {"opcode": "01", "funct3": "000", "format": "CI"},
    "c.ebreak":    {"opcode": "10", "funct3": "100", "format": "CR"},
}

#============================================================================================
# Combine all into one
instruction_map = {
    **r_type_instructions,
    **i_type_instructions,
    **s_type_instructions,
    **b_type_instructions,
    **j_type_instructions,
    **jalr_instruction,
    **u_type_instructions,
    **system_instructions,
    **f_type_instructions,
    **m_type_instructions,
    **a_type_instructions,
}
