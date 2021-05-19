'''
imprime os primeiros números ímpares conforme o valor digitado
exemplo: Digite um número: 5 = 1 3 5 7 9
'''
def valoresImpares():
    n = int(input("Digite um número: "))
    soma = 1
    for i in range(1, n+1):
            print(soma)
            soma += 2


if __name__ == '__main__':
    valoresImpares()