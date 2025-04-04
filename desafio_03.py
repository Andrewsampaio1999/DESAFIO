# O Departamento Estadual de Meteorologia solicitou o desenvolvimento de um programa queleia um conjunto indeterminado de temperaturas, ao final informe a menor e a maior temperatura, bem como a média delas.

temperaturas = ("informe a temperatura")
def main():
    temperaturas = []
    
    while True:
        entrada = input("Digite uma temperatura (ou 'sair' para encerrar): ")
        
        if entrada.lower() == 'sair':
            break
        
        try:
            temperatura = float(entrada)
            temperaturas.append(temperatura)
        except ValueError:
            print("Por favor, insira um número válido ou 'sair' para encerrar.")
    
    if temperaturas:
        menor = min(temperaturas)
        maior = max(temperaturas)
        media = sum(temperaturas) / len(temperaturas)
        
        print(f"A menor temperatura é: {menor:.2f}")
        print(f"A maior temperatura é: {maior:.2f}")
        print(f"A média das temperaturas é: {media:.2f}")
    else:
        print("Nenhuma temperatura foi registrada.")

if __name__ == "__main__":
    main()
