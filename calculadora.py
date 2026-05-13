# =================================
#       CALCULADORA EM PYTHON
#         Operações Básicas
# =================================

def soma(a, b):
    return a + b

def subt(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "dev0"
    return a / b

while True:
    print("\n==== Calculadora ====")
    print("1- Soma")
    print("2- Subtração")
    print("3- Multiplicação")
    print("4- Divisão")

    opcao = int(input("Escolha uma opção: "))

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    match opcao:
        case 1:
            resultado = soma(num1, num2)
        case 2:
            resultado = subt(num1, num2)
        case 3:
            resultado = mult(num1, num2)
        case 4:
            resultado = soma(num1, num2)
        case _:
            print("ERRO: opção digitada inválida: ")
            break
    print("Resultado: ", resultado)
    break