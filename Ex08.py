distancia_km = float(input("Digite a distância a ser percorrida em km: "))
consumo_km_por_litro = float(input("Digite o consumo do veículo em km/l: "))
preco_litro = float(input("Digite o preço do litro de combustível: "))

litros_necessarios = distancia_km / consumo_km_por_litro
custo_total = litros_necessarios * preco_litro
custo_por_km = custo_total / distancia_km

print(f"Distância: {distancia_km} km")
print(f"Consumo: {consumo_km_por_litro} km/l")
print(f"Preço do litro: R$ {preco_litro:.2f}")
print(f"Litros necessários: {litros_necessarios:.2f} L")
print(f"Custo total estimado: R$ {custo_total:.2f}")
print(f"Custo por km: R$ {custo_por_km:.3f}")