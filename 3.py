def calcular_desconto(cliente):
    if cliente < 21:
        print ("\nSeu desconto é de 15%")
    else:
        print("\nSeu desconto é de 10%")

idade = int(input("Digite sua idade para saber a porcentagem do seu desconto: "))
calcular_desconto(idade)