qtd_sanduiche = int(input("Digite a quantidade de sanduíches a serem feitos: "))

fatia_queijo = 0.050 * 2
fatia_presunto = 0.050
hamburguer = 0.100

peso_total_presunto = qtd_sanduiche * fatia_presunto
peso_total_queijo = qtd_sanduiche * fatia_queijo
peso_total_hamburguer = qtd_sanduiche * hamburguer

print("Para fazer", qtd_sanduiche, "sanduíches, você precisará de:")
print(f"O peso total de presunto necessário é {peso_total_presunto:.2f} kg.")
print(f"O peso total de queijo necessário é {peso_total_queijo:.2f} kg.")
print(f"O peso total de hambúrguer necessário é {peso_total_hamburguer:.2f} kg.")