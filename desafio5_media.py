# Recebendo três notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calculando a média
media = (nota1 + nota2 + nota3) / 3

# Exibindo o resultado
print(f"A média das notas é: {media:.2f}")

# Verificando se foi aprovado (considerando média 7)
if media >= 7:
    print("Situação: Aprovado!")
else:
    print("Situação: Reprovado")