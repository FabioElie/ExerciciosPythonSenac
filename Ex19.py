ladoA = float(input("Digite o tamanho do lado A do triângulo: "))
ladoB = float(input("Digite o tamanho do lado B do triângulo: "))
ladoC = float(input("Digite o tamanho do lado C do triângulo: "))

if (ladoA < ladoB + ladoC) and (ladoB < ladoA + ladoC) and (ladoC < ladoA + ladoB):
    if ladoA == ladoB == ladoC:
        tipo = "equilátero"
    elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
        tipo = "isósceles"
    else:
        tipo = "escaleno"
    print(f"O triângulo é válido e do tipo {tipo}.")
else:
    print("O triângulo não é válido.")
