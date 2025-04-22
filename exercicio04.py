peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura em metros: ").replace(',', '.'))

imc = peso / (altura * altura)

if imc < 18.6:
    print("Você está abaixo do peso")

elif imc >= 18.6 and imc <= 24.9:
    print("Você está no peso ideal")

elif imc > 24.9 and imc <= 29.9:
    print("Você está levemente acima do peso")

elif imc > 29.9 and imc <= 34.9:
    print("Você está com obesidade grau I")

elif imc > 34.9 and imc <= 39.9:
    print("Você está com obesidade grau II (severa)")

else:
    print("Você está com obesidade grau III (mórbida)")