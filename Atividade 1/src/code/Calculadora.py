#menu que será utilizado para a escolha do usuário quanto a operação que deseja efetuar
itens = """
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão 
"""

i = 's'
while (i == 's'):
    #Números que serão utilizados
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))

    print(itens)
    escolha = int(input("Qual operação você gostaria de efetuar? "))

    if (escolha == 1):
        
        
    elif (escolha == 2):
        

    elif (escolha == 3):
        
        
    elif (escolha == 4):
        
        
    else:
        print("Inválido")

    #Pergunta que, caso a resposta seja 'n', poderá quebrar o laço de repetição
    i = input("Quer continuar calculando? (s/n)")
