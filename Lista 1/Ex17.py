salario =float(input("Digite o salário do funcionário: "))

if salario <= 280:
    reajuste = salario * 0.20
elif salario >= 280.01 and salario <= 700:
    reajuste = salario * 0.15
elif salario >= 700.01 and salario <= 1500:
    reajuste = salario * 0.10
else:
    reajuste = salario * 0.05

novo_salario = salario + reajuste

print(f"Salário antes do reajuste: R$ {salario:.2f}")
print(f"Percentual de aumento aplicado: { (reajuste / salario) * 100 :.0f}%")
print(f"Valor do reajuste: R$ {reajuste:.2f}")
print(f"Novo salário após o reajuste: R$ {novo_salario:.2f}")