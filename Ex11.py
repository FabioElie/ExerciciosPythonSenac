nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))

if idade <= 2:
    tipo = "Bebê"
    print(f"{nome} está com {idade} e pela tabela é considerado um {tipo}.")
elif idade >= 3 and idade <= 11:
    tipo = "Criança"
    print(f"{nome} está com {idade} e pela tabela é considerado uma {tipo}.")
elif idade >= 12 and idade <= 21:
    tipo = "Jovem"
    print(f"{nome} está com {idade} e pela tabela é considerado um {tipo}.")
elif idade >= 22 and idade <= 64:
    tipo = "Adulto"
    print(f"{nome} está com {idade} e pela tabela é considerado um {tipo}.")
elif idade >= 65 and idade <= 100:
    tipo = "Idoso"
    print(f"{nome} está com {idade} e pela tabela é considerado um {tipo}.")
else:
    tipo = "Muito velhinho"
    print(f"{nome} está com {idade} e pela tabela é considerado um {tipo}.")