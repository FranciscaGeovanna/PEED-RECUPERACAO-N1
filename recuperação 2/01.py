print("Verificar se o cupom é válido\n")

def verificaCupom(cupom):
    cupomInicial = 75
    cupomFinal = 208
    if cupom >= cupomInicial and cupom <= cupomFinal:
        print("\nCupom válido!")
    else:
        print("\nErro: Cupom inválido!")

cupom = int(input("Digite o seu cupom: "))

verificaCupom(cupom)