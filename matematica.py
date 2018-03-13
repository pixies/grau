def soma(x,y):
    return x+y

def divisao(x,y):
    if y == 0:
        return 'impossivel dividir um numero por ZERO'
    else:
        return x/y

valor1 = float(input("Digite um Valor: "))
operacao = raw_input("Digite a sua operacao: ( + ou /) " )
valor2 = float(input("Digite outro Valor: "))

if operacao == '+':
    print(soma(valor1, valor2))
elif operacao == '/':
    print(divisao(valor1, valor2))
else:
    print('Operacao nao encontrada')
