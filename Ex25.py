qtd_camisetas_pequenas = int(input("Digite a quantidade de camisetas pequenas a serem compradas: "))
qtd_camisetas_medias = int(input("Digite a quantidade de camisetas médias a serem compradas: "))
qtd_camisetas_grandes = int(input("Digite a quantidade de camisetas grandes a serem compradas: "))

valor_total = (qtd_camisetas_pequenas * 10) + (qtd_camisetas_medias * 12) + (qtd_camisetas_grandes * 15)
print(f"Camisetas pequenas: {qtd_camisetas_pequenas} unidades, com o valor total de R$ {qtd_camisetas_pequenas * 10:.2f}")
print(f"Camisetas médias: {qtd_camisetas_medias} unidades com o valor total de R$ {qtd_camisetas_medias * 12:.2f}")
print(f"Camisetas grandes: {qtd_camisetas_grandes} unidades com o valor total de R$ {qtd_camisetas_grandes * 15:.2f}")
print(f"O valor total da compra é R$ {valor_total:.2f}.")