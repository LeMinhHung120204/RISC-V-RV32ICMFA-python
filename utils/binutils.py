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
