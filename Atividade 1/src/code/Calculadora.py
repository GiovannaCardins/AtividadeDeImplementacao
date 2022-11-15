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
    
        #Após o usuário digitar os números que deseja usar na equação, irá escolher qual tipo de operação deseja executar

    if (escolha == 1):
        print(n1, "+", n2, "=", n1 + n2)
        
        #Ao escolher o numero um, será efetuada a adição dos dois termos
        
    elif (escolha == 2):
        print(n1, "-", n2, "=", n1 - n2)
        
        #Ao escolher o numero dois, será efetuada a subtração dos dois termos

    elif (escolha == 3):
        print(n1, "*", n2, "=", n1*n2)
        
        #Ao escolher o numero três, será feito o produto dos dois termos
        
        
    elif (escolha == 4):
        print(n1, "/", n2, "=", n1/n2)
        
        #Ao escolher o numero quatro, será efetuada a divisão dos dois termos
        
    else:
        print("Inválido")
        
        #Caso o usuário cometa algum erro esse mensagem aparecerá. Caso a resposta seja 'n', o laço de repetição será quebrado
    i = input("Quer continuar calculando? (s/n)")
