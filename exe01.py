'''
#4) Receba um vetor e inverta a ordem dos elementos (Sem usar a função reverse)
'''
def inverter_vetor():
    vetor1 = []
    vetor2 = []

    qnt = int(input("Quantos valores irá informar? "));
    for i in range(qnt):
        vetor1.append(int(input("Diga o valor: ")));
    for i in range(qnt):
        vetor2.append(vetor1[qnt - 1]);
        qnt = qnt - 1

    print("Esta é sua lista: ", vetor1)
    print("Esta é a lista com os valores invertidos: ", vetor2)


if __name__ == '__main__':
    inverter_vetor()