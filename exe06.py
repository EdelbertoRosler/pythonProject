'''
Encontra os dois maiores valores dentro de uma lista, e soma esses valores
Duas listas para testar
'''

def valor_em_lista():
    list_one = [1, 4, 1, 8, 5]
    list_two = [1, 1, 50, 2, -12, 7, -1, 0]
    list_one_copy = list_one.copy()
    list_two_copy = list_two.copy()

    maximo_one = list()
    maximo_two = list()

    soma_one = 0
    soma_two = 0
    for i in range(0, 2):
        maximo_one.append(max(list_one_copy))
        maximo_two.append(max(list_two_copy))
        list_one_copy.remove(max(list_one_copy))
        list_two_copy.remove(max(list_two_copy))
    soma_one = sum(maximo_one)
    soma_two = sum(maximo_two)

    print(list_one, '--> ', maximo_one[0], ' + ', maximo_one[1], ' = ', soma_one)
    print(list_two, '--> ', maximo_two[0], ' + ', maximo_two[1], ' = ', soma_two)

if __name__ == '__main__':
    valor_em_lista()