'''
Receba um vetor e inverta a ordem dos elementos (Sem usar a função reverse)
'''
def vetores():
    vet = []
    vet2 = []
    while True:
        try:
            qnt = int(input("Quantos valores irá informar? "))
            for i in range(qnt):
                vet.append(int(input("Diga o valor: ")))
            for i in range(qnt):
                vet2.append(vet[qnt - 1])
                qnt = qnt - 1
            break
        except ValueError:
            print("OPS! Esse valor não é válido!\nDigite um número inteiro")


    print("Esta é sua lista: ", vet)
    print("Esta é a lista com os valores invertidos: ", vet2)



    # 2) Selecione o maior e o menor elemento de um vetor
    print("O maior valor da lista é: ",max(vet))
    print("O menor valor da lista é: ",min(vet))
    print("*" * 50)


    # 3) Calcule a média aritmética dos elementos de um vetor
    media = sum(vet) / len(vet)
    print("A média do vetor é: ",media)
    print("*" * 50)

if __name__ == '__main__':
    vetores()