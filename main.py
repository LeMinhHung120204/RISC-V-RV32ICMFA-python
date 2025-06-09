# main.py
from encoder import RV32I, RV32M, RV32C, RV32F, RV32A 

def read_assembly_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return [line.strip() for line in lines if line.strip() and not line.startswith('#')]

def write_machine_code(filename, binary_lines):
    with open(filename, 'w') as f:
        for bin_line in binary_lines:
            f.write(bin_line + '\n')


def dispatch_encoder(mnemonic):
    """Trả về module encode phù hợp với từng loại instruction."""
    if mnemonic in RV32I.instruction_map:
        return RV32I.encode
    if mnemonic in RV32F.instruction_map:
        return RV32F.encode
    # if mnemonic in RV32A.instruction_map:
    #     return RV32A.encode
    # if mnemonic in RV32M.instruction_map:
    #     return RV32M.encode
    # if mnemonic in RV32C.instruction_map:
    #     return RV32C.encode
    raise ValueError(f"Unsupported instruction: {mnemonic}")


def assemble():
    asm_lines = read_assembly_file("input.asm")
    machine_code = []

    for line in asm_lines:
        try:
            mnemonic = line.split()[0].lower()  # Tách từ đầu tiên trong dòng (add, lw) viet thuong    
            encoder = dispatch_encoder(mnemonic)
            binary = encoder(line)
            hex_code = hex(int(binary, 2))[2:].zfill(8)
            machine_code.append(f"{binary}    # 0x{hex_code}")

        # debug
        except Exception as e:
            print(f"Error at line: '{line}' -> {e}")

    write_machine_code("output.txt", machine_code)

if __name__ == "__main__":
    assemble()
