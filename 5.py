print("Calcular média\n")

lista = []

for i in range(10):
    notas = float(input(f"Digite a {i+1}° nota: "))
    lista.append(notas)

somar = sum(lista)
media = somar / 10

print(f"\nA média é: {media:.2f}")