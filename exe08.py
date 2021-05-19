def fatorial():
    fator = numero = n = int(input("Digite um número: "))
    for i in range(1, n+1):
        if n >= 2:
            fator = fator * (n-1)
            n -= 1
    print(f'O fatorial de {numero} é: {fator}'.format(numero, fator))

if __name__ == '__main__':
    fatorial()