'''
Recebe um número inteiro e calcula a soma de seus algarismos.
exemplo: Digite um número inteiro: 12587
soma : 23

'''
def somaDealgarismos():
    n = int(input("Digite um número inteiro: "))
    soma = 0
    while n > 0:
        inteiro = n // 10
        resto = n % 10
        soma += resto
        n = inteiro
    print('soma: ', soma)

if __name__ == '__main__':
    somaDealgarismos()