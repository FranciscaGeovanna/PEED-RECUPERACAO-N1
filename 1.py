print("Verificar se o cupom é válido\n")

cupom = int(input("Digite o seu cupom: "))

if cupom >= 75 and cupom <= 208:
    print("\nCupom válido!")
else:
    print("\nErro: Cupom inválido!")