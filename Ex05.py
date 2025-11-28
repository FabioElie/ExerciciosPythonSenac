nome = str(input("Digite o nome do aluno: "))
displina = str(input("Digite a disciplina: "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3

print(f"O/A Aluno/a {nome} \nobteve a média {media:.2f}  \nna disciplina de {displina}, \ncom as notas: {nota1}, {nota2}, {nota3}")
