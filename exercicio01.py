valorA = float(input("Digite o valor de A: "))
valorB = float(input("Digite o valor de B: "))
valorC = float(input("Digite o valor de C: "))

soma = valorA + valorB
print(f"A soma entre A e B é {soma}")

if soma < valorC:
    print(f"A soma é menor que C")
elif soma > valorC:
    print(f"A soma é maior que C")
else:
    print("A soma é igual a C")

