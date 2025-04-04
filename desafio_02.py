# Faça um programa para uma loja de tintas, que solicite o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 130,00.Informe ao usuário a quantidade de latas de tinta a serem compradas e o valor a ser pago.

area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

cobertura_por_litro = 3  # metros quadrados por litro
litros_por_lata = 18      # litros por lata
preco_por_lata = 130.00   # preço de cada lata

litros_necessarios = area / cobertura_por_litro

latas_necessarias = -(-litros_necessarios // litros_por_lata) 

custo_total = latas_necessarias * preco_por_lata

# Saida de dados
print(f"Quantidade de latas de tinta a serem compradas: {int(latas_necessarias)}")
print('-------------------------------------------------------------------------')
print(f"Valor total a ser pago: R$ {custo_total:.2f}")