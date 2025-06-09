# R-type
add x1, x2, x3
sub x4, x5, x6
xor x7, x8, x9
or x10, x11, x12
and x13, x14, x15
sll x16, x17, x18
srl x19, x20, x21
sra x22, x23, x24
slt x25, x26, x27
sltu x28, x29, x30

# I-type (Immediate)
addi x1, x2, 10
xori x3, x4, 15
ori x5, x6, 20
andi x7, x8, 25
slli x9, x10, 2
srli x11, x12, 3
srai x13, x14, 1
slti x15, x16, -5
sltiu x17, x18, 30

# I-type (Load)
lb x1, 0(x2)
lh x3, 2(x4)
lw x5, 4(x6)
lbu x7, 6(x8)
lhu x9, 8(x10)

# S-type (Store)
sb x11, 0(x12)
sh x13, 2(x14)
sw x15, 4(x16)

# B-type (Branch)
beq x1, x2, 8
bne x3, x4, 12
blt x5, x6, 16
bge x7, x8, 20
bltu x9, x10, 24
bgeu x11, x12, 28

# J-type
jal x1, 100
jalr x2, x3, 4

# U-type
lui x4, 4096       # = 0x1000
auipc x5, 8192     # = 0x2000

# System
ecall
ebreak

fadd.s f1, f2, f3       # f1 = f2 + f3
fsub.s f4, f5, f6       # f4 = f5 - f6
fmul.s f7, f8, f9       # f7 = f8 * f9
fdiv.s f10, f11, f12    # f10 = f11 / f12