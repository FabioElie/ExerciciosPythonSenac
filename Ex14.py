num_conta = str(input("Digite o número da conta: "))
saldo = float(input("Digite o saldo da conta: "))
debito = float(input("Digite o valor do débito: "))
credito = float(input("Digite o valor do crédito: "))

saldo_atual= saldo - debito + credito

if saldo_atual >=0:
    print(f"O saldo atual da conta {num_conta} é de: R$ {saldo_atual:.2f}. \n Saldo Positivo.")
else:
    print(f"O saldo atual da conta {num_conta} é de: R$ {saldo_atual:.2f}. \n Saldo Negativo.")