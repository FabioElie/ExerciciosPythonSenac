nome = str(input("Digite seu nome: "))

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"O/A Aluno/a Nome: {nome}")
print(f"Teve a média anual de: {media:.2f} com as notas: {nota1}, {nota2}, {nota3}, {nota4}")

