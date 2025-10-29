# Recebendo dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Realizando operações
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2

# Verificando divisão por zero antes de dividir
if num2 != 0:
    divisao = num1 / num2
else:
    divisao = "Não é possível dividir por zero"

# Exibindo resultados
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")