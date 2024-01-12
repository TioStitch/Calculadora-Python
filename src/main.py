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

calc = {
    1: first + second,
    2: first - second,
    3: first * second,
    4: first / second,
    5: first % second
}

print(printar)

equation = int(input("Apenas insira o digito do calculo."))

result = calc[equation]

print(f'Resultado: {result}')