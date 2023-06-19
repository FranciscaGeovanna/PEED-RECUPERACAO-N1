print("Os livros mais vendidos do mês")

quant = int(input("\nQuantos livros deseja adicionar ao ranking? "))

lista = []

for i in range(quant):
    livro = input(f"\nDigite o título do {i+1}° livro: ")
    posicao = int(input("Informe a posição do livro: "))
    print("\n\tLivro adicionado ao ranking!")
    lista.append((posicao,livro))

print("\nRanking de Mais Vendidos:")
for posicao, livro in lista:
    print(posicao, "-", livro)

