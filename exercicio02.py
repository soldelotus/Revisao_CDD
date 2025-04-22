inserir = "S";
while inserir == "S":

    num = float(input("Digite um número: "))

    if num > 0:
        if num % 2 == 0:
            print("O número é positivo e par")
        else:
            print("O número é positivo e ímpar")
    else:
        if num % 2 == 0:
            print("O número é negativo e par")
        else:
            print("O número é negativo e ímpar")

    inserir = input("Deseja inserir um novo valor? Responda com S para sim e N para não: ")