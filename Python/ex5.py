def contar_bits_um(numero):
    quantidade = 0
    print(f"Analisando o número {numero} ({bin(numero)})")
    for i in range(numero.bit_length()):
        mascara = 1 << i
        if numero & mascara:
            print(f"Bit {i}: 1")
            quantidade += 1
        else:
            print(f"Bit {i}: 0")
    print(f"Quantidade de bits 1: {quantidade}\n")
    return quantidade

valores = [27, 127, 59, 1005]
for valor in valores: