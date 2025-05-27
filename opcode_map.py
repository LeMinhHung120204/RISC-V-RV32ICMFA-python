# opcode_map.py

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

# Combine all into one
instruction_map = {
    **r_type_instructions,
    **i_type_instructions,
    **s_type_instructions,
    **b_type_instructions,
    **j_type_instructions,
    **jalr_instruction,
    **u_type_instructions,
    **system_instructions
}
