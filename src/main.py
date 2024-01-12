first = int(input("Insira o valor do primeiro número:"))
second = int(input("Insira o valor do segundo número:"))

print("Por favor, escolha o calculo realizado: " )
printar = [
    "1. +"
    "2. -"
    "3. *"
    "4. /"
    "5. %"
]
print(printar)
equation = int(input("Apenas insira o digito do calculo."))
match(equation):
    case 1:
        print("Resultado: " + str(first+second))
        breakpoint
    case 2:
        print("Resultado: " + str(first-second))
        breakpoint
    case 3:
        print("Resultado: " + str(first*second))
        breakpoint
    case 4:
        print("Resultado: " + str(first/second))
        breakpoint
    case 5:
        print("Resultado: " + str(first%second))
        breakpoint