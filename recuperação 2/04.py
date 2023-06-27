import random

print("Adivinhe o número de 1 à 50")

def sortearNum():
    sorteado = random.randint(1, 50) # gera um número inteiro aleatório entre 1 e 50

    while True:
        palpite = int(input("\nQual número você acha que é? "))
        if palpite == sorteado:
            print("\nParabéns, você ganhou! O número era", sorteado)
            break
        elif palpite > sorteado:
            print("\nNão foi dessa vez, tente um número mais baixo")
        else:
            print("\nNão foi dessa vez, tente um número mais alto")

sortearNum()