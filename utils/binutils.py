# utils/binutils.py

def reg_to_bin(reg_name):
    """Convert register name like 'x1' or 'x10' to 5-bit binary string."""
    reg_num = int(reg_name[1:])
    return format(reg_num, '05b')


def imm_to_bin(imm, bits):
    """Convert immediate value to 2's complement binary string of 'bits' length."""
    if imm < 0:
        imm = (1 << bits) + imm
    return format(imm & ((1 << bits) - 1), f'0{bits}b')


def split_imm_s_type(imm):
    """Split 12-bit immediate into imm[11:5] and imm[4:0] for S-type."""
    imm_bin = imm_to_bin(imm, 12)
    return imm_bin[:7], imm_bin[7:]


def split_imm_b_type(imm):
    """Split 13-bit immediate into fields for B-type encoding."""
    imm_bin = imm_to_bin(imm, 13)  # B-type uses bits [12|10:5|4:1|11]
    return imm_bin[0], imm_bin[2:8], imm_bin[8:12], imm_bin[1]


def split_imm_j_type(imm):
    """Reorder immediate bits for J-type instruction (20 bits)."""
    imm_bin = imm_to_bin(imm, 21)  # 21-bit for alignment and sign
    return (
        imm_bin[0] +        # imm[20]
        imm_bin[10:20] +    # imm[10:1]
        imm_bin[9] +        # imm[11]
        imm_bin[1:9]        # imm[19:12]
    )


def split_imm_u_type(imm):
    """Get upper 20 bits for U-type instructions (lui/auipc)."""
    return imm_to_bin(imm >> 12, 20)

#=========================================================================================
# Ho tro cho RV32C
def split_imm_ci_type(imm):
    """Immediate field for CI-type (used in c.addi, c.li, c.lui, etc)."""
    return imm_to_bin(imm, 6)  # CI-type immediate is usually 6 bits

def split_imm_cb_type(imm):
    """Split for CB-type (used in c.beqz, c.bnez)."""
    imm_bin = imm_to_bin(imm, 9)  # 9-bit for branching
    # Mapping: [8|4:3|7:6|2:1|5]
    return imm_bin[0] + imm_bin[4:6] + imm_bin[1:3] + imm_bin[6:8] + imm_bin[3]

def split_imm_cj_type(imm):
    """Split for CJ-type (used in c.j, c.jal)."""
    imm_bin = imm_to_bin(imm, 12)
    # Mapping: [11|4|9:8|10|6|7|3:1|5]
    return (
        imm_bin[0] +      # 11
        imm_bin[5] +      # 4
        imm_bin[1:3] +    # 9:8
        imm_bin[3] +      # 10
        imm_bin[6] +      # 6
        imm_bin[7] +      # 7
        imm_bin[8:11] +   # 3:1
        imm_bin[4]        # 5
    )

def split_imm_ciw_type(imm):
    """Used in c.addi4spn (non-zero unsigned immediate)."""
    imm_bin = imm_to_bin(imm, 10)
    # Mapping: [5|4|9:6|2|3]
    return imm_bin[4] + imm_bin[3] + imm_bin[0:3] + imm_bin[7] + imm_bin[6]

def split_imm_css_type(imm):
    """Used in c.swsp immediate."""
    return imm_to_bin(imm, 8)  # usually 7-8 bits

def split_imm_cl_type(imm):
    """Used in c.lw, etc."""
    return imm_to_bin(imm, 7)  # CL-type 7-bit load/store offset

def split_imm_cs_type(imm):
    """Used in c.sw, etc."""
    return imm_to_bin(imm, 7)  # CS-type store

#=========================================================================================
# Ho tro cho RV32F
def float_reg_to_bin(reg_name):
    """Convert floating-point register like f0–f31 to binary."""
    reg_num = int(reg_name[1:])
    return format(reg_num, '05b')
