def metros_para_centimetros(metros):
    """
    Função que converte metros para centímetros.
    """
    return metros * 100

# Solicita ao usuário que digite o valor em metros
valor_metros = float (input("Digite o valor em metros: "))

# Chama a função metros_para_centimetros() passando o valor digitado e atribui o resultado a valor_centimetros
valor_centimetros = metros_para_centimetros (valor_metros)

# Exibe o resultado da conversão na tela
print(f"{valor_metros} metros equivalem a {valor_centimetros} centímetros.")
