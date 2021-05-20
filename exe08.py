'''
Encontra o fatorial de um número
exemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120
'''

def fatorial():
    fator = numero = n = int(input("Digite um número: "))
    if n == 0 or n == 1:
        fator = 1
    else:
        for i in range(1, n+1):
            if n >= 2:
                fator = fator * (n-1)
                n -= 1
    print('O fatorial de {} é: {}'.format(numero, fator))

if __name__ == '__main__':
    fatorial()
