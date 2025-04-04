# Crie um programa que:
# 1- Peça ao usuário para digitar dez números inteiros e os armazene em uma lista.
# 2- Exiba a lista completa.
# 3- Exiba o maior e o menor número da lista.
# 4- Exiba a soma e a média de todos os números.

numeros =[]
for i in range (10):
    numero = int(input(f'digite o {i+1}° numero:'))
    numeros.append(numero)
# Dados
print("\nLista completa:")
print(numeros)

print(f"\nMaior numero: {max(numeros)}")
print(f"Menor mumero:{min(numeros)}")

soma = sum (numeros)
media = soma / len(numeros)
print(f"\nMaior mumero: {min(numeros)}")