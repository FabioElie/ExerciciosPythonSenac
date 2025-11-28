salario = float(input("Digite o salário do funcionário: "))
vendas = float(input("Digite o total de vendas do funcionário no mês: "))

comissao = vendas * 0.04
salario_final = salario + comissao
print(f"O salário final do funcionário, incluindo a comissão de R$ {comissao:.2f}, é R$ {salario_final:.2f}.")