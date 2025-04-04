# Foi realizada uma pesquisa de algumas características físicas da população de uma certa região, aqual coletaram os seguintes dados referentes a cada habitante para serem analisados:
#- sexo (masculino e feminino)
#- cor dos olhos (azuis, verdes ou castanhos)
#- cor dos cabelos (louros, castanhos, pretos)
#- idade
#Faça um programa que determine e escreva:
#a) a maior idade dos habitantes;
#b) a quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos, inclusive;
#c) a quantidade de indivíduos que tenham olhos verdes e cabelos louros

habitantes = []

def coletar_dados():
    while True:
        sexo = input("Digite o sexo (masculino/feminino) ou 'sair' para encerrar: ").strip().lower()
        if sexo == 'sair':
            break
        cor_olhos = input("Digite a cor dos olhos (azuis/ verdes/ castanhos): ").strip().lower()
        cor_cabelos = input("Digite a cor dos cabelos (louros/ castanhos/ pretos): ").strip().lower()
        idade = int(input("Digite a idade: "))
        
        habitantes.append({
            'sexo': sexo,
            'cor_olhos': cor_olhos,
            'cor_cabelos': cor_cabelos,
            'idade': idade
        })

def analisar_dados():
    if not habitantes:
        print("Nenhum dado foi coletado.")
        return

    maior_idade = max(habitante['idade'] for habitante in habitantes)
    print(f"A maior idade dos habitantes é: {maior_idade}")

    quantidade_femininos_18_35 = sum(1 for habitante in habitantes if habitante['sexo'] == 'feminino' and 18 <= habitante['idade'] <= 35)
    print(f"A quantidade de indivíduos do sexo feminino entre 18 e 35 anos é: {quantidade_femininos_18_35}")

    quantidade_olhos_verdes_cabelos_louros = sum(1 for habitante in habitantes if habitante['cor_olhos'] == 'verdes' and habitante['cor_cabelos'] == 'louros')
    print(f"A quantidade de indivíduos com olhos verdes e cabelos louros é: {quantidade_olhos_verdes_cabelos_louros}")

coletar_dados()
analisar_dados()
