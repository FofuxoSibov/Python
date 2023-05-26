numero = int(input("Digite um número para exibir a tabuada: "))

# Exibir a tabuada
print("Tabuada de", numero, ":")

# Loop de 1 a 10 para multiplicar o número digitado
for contador in range(1, 11):
    resultado = numero * contador  # Multiplica o número pelo iterador do loop
    print(numero, "x", contador, "=", resultado)  # Exibe a multiplicação na forma "num x i = resultado"