# Solicita que o usuário digite um número e converte para ponto flutuante
numero1 = float(input("Digite o seu salário: "))

# Calcula a media de tres numero
novoSalario = numero1 * 1.12

numeroArredondado = round (novoSalario, 2)

# Exibe o dobro do número
print("Seu salário é R$", numero1, "com aumento ficará R$", numeroArredondado)
