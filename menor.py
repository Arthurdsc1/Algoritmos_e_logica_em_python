A = int(input("Primeiro valor: "))
B = int(input("Segundo valor: "))
C = int(input("Terceiro valor: "))

if (A < B) and (A < C):
    menor = A
elif B < C:
    menor = B
else:
    menor = C

print(f"Menor valor: {menor}")