print("Os livros mais vendidos do mês")

def rakingLivros():
    lista = []

    quant = int(input("\nQuantos livros deseja adicionar ao ranking? "))
    for i in range(quant):
        livro = input(f"\nDigite o título do {i+1}° livro: ")
        posicao = int(input("Informe a posição do livro: "))
        print("\n\tLivro adicionado ao ranking!")
        lista.append((posicao,livro))

    novaLista = sorted(lista)
    
    print("\nRanking de Mais Vendidos:")
    for pos, lvr in novaLista: 
        print(pos, "-", lvr)
        
rakingLivros()