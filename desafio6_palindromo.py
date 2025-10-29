# Recebendo uma palavra
palavra = input("Digite uma palavra: ")

# Removendo espaços e convertendo para minúsculas para melhor comparação
palavra_limpa = palavra.replace(" ", "").lower()

# Invertendo a palavra
palavra_invertida = palavra_limpa[::-1]

# Verificando se é um palíndromo
if palavra_limpa == palavra_invertida:
    print(f"'{palavra}' é um palíndromo!")
else:
    print(f"'{palavra}' não é um palíndromo.")

# Mostrando a palavra original e invertida para comparação
print(f"Original: {palavra_limpa}")
print(f"Invertida: {palavra_invertida}")