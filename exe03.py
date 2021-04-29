'''
Progressão geométrica crescente com o primeiro elemento valendo 2,
a razão é crescente, sendo razão = n*n,
o número de elementos da pg é informado pelo usuário ex: {2,4,16...}
'''

def pg():
        while True:
            try:
                loop = int(input("Quantos elementos você deseja imprimir? "))
                mult = 2
                cont = 0
                all = []
                while cont < loop:
                    all.append(mult)
                    mult = mult * mult
                    cont += 1
                print(all)

                break
            except ValueError:
                print("OPS! Esse valor não é válido!\nDigite um número inteiro")


if __name__ == '__main__':
    pg()