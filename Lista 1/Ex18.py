horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
salario_hora = float(input("Digite o valor do salário por hora: "))

salario_bruto = horas_trabalhadas * salario_hora
desconto_sindicato = salario_bruto * 0.03
desconto_fgts = salario_bruto * 0.11
desconto_inss = salario_bruto * 0.10

if salario_bruto <= 900:
    desconto_ir = 0
    porcentagem_desconto_ir = "0%"
elif salario_bruto <= 1500:
    desconto_ir = salario_bruto * 0.05
    porcentagem_desconto_ir = "5%"
elif salario_bruto <= 2500:
    desconto_ir = salario_bruto * 0.10
    porcentagem_desconto_ir = "10%"
else:
    desconto_ir = salario_bruto * 0.20
    porcentagem_desconto_ir = "20%"

total_descontos = desconto_ir + desconto_inss + desconto_sindicato

print(f"Salário Bruto: R$ {salario_hora:.2f} por hora * {horas_trabalhadas} horas:  R$ {salario_bruto:.2f}")
print(f"(-) IR ({porcentagem_desconto_ir}): R$ {desconto_ir:.2f}")
print(f"(-) INSS (10%): R$ {desconto_inss:.2f}")
print(f"(-) Sindicato (3%): R$ {desconto_sindicato:.2f}")
print(f"FGTS (11%): R$ {desconto_fgts:.2f}")
print(f"Total de descontos: R$ {total_descontos:.2f}")
print(f"Salário Líquido: R$ {salario_bruto - total_descontos:.2f}")

