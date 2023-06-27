print("Calcular média\n")

def calcularMedia(nota):
    somar = sum(nota)
    media = somar / 10
    return media

lista = []

for i in range(10):
    notas = float(input(f"Digite a {i+1}° nota: "))
    lista.append(notas)

resultado = calcularMedia(lista)

print(f"\nA média é: {resultado:.2f}")