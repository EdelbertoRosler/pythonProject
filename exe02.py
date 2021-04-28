'''
a soma de quatro algarismos menores que um algarismo máximo deve dar 21.
ex: maximo 6 = 3666, 4566, 5466 etc...
'''
def transformar_m_em_cm():
    algarismos = [0,1,2,3,4,5,6,7,8,9]
    for i in algarismos:
        for j in algarismos:
            for k in algarismos:
                for l in algarismos:
                    if ((i+j+k+l) == 21) and (l>=k) and (l>=j) and(l>=i):
                        print(i,j,k,l)


if __name__ == '__main__':
    transformar_m_em_cm()