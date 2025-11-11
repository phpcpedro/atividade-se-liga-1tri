# Declaração das variáveis
idade = 20           # variável inteira
nome = "Ana"         # variável string
ativo = True         # variável booleana

# Impressão dos valores
print("Idade:", idade)
print("Nome:", nome)
print("Está ativo:", ativo)
def verificar_idade():
    idade = int(input("Digite sua idade: "))

    if idade >= 18:
        print("Você é maior de idade.")
    else:
        print("Você é menor de idade.")

# Chamada da função
verificar_idade()
# Solicita dois valores ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Realiza soma e subtração
soma = num1 + num2
subtracao = num1 - num2

# Exibe os resultados
print("Soma:", soma)
print("Subtração:", subtracao)
# Exemplo de loop for: imprimir números de 1 a 5
for i in range(1, 6):
    print("Número:", i)
