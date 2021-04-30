'''
Faço um programa que encontre a raiz quadrada de um número, sem O método sqrt()
'''


def mysqrt():
    teste = False
    # Return the sqrt value of numbers 0 to 3
    while True:
        try:
            number = int(input('what number? '))
            break
        except ValueError:
            print('Enter a valid value!')

    AAA = {0: 0, 1: 1, 2: 1.414, 3: 1.732}
    if number in AAA.keys():
        root = AAA[number]
        teste = True
        print('The square root of ', number, ' is: ', root)

    #  checks if it is a perfect sqrt
    if number > 3:
        n = number // 2
        for i in range(1, n + 1):
            if (i * i) == number:
                root = i
                print('The square root of {} is: {:.0f}'.format(number, root))
                teste = True

    # If it is not a perfect sqrt, look for the nearest sqrt
    if teste == False:
        num_copy = number
        n = number // 2
        for j in range(1, n + 1):
            for i in range(1, n + 1):
                if (i * i) == num_copy:
                    n_small = i
                    n_large = i + 1
                    break
                if (i * i) > num_copy:
                    break
            if (i * i) == num_copy:
                break
            num_copy -= 1
        # Uses this calculation to find the approximate sqrt
        if (number - (n_small * n_small)) < ((n_large * n_large) - number):
            nearest_root = (n_small * n_small)
            root = (number + nearest_root) / (2 * n_small)
            teste = True
        else:
            nearest_root = (n_large * n_large)
            root = (number + nearest_root) / (2 * n_large)
            teste = True
        print('The square root of {} is: {:.3f}'.format(number, root))

# !!! Não está fncionando para os valores 7 e 8


if __name__ == '__main__':
    mysqrt()