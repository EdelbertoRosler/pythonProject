'''
Crie um programa que cadastre informações de várias pessoas
(nome, idade e cpf) e depois coloque em um dicionário. Depois
remova todas as pessoas menores de 18 anos do dicionário e
coloque em outro dicionário.
'''

def cadastro():
    usuarios = list()
    usuarios_menores = list()
    dados = dict()


    for i in range(0, 3):  # Cadastra 3 usuários
        dados["nome"] = input("Diga seu nome: ")
        while True:
            try:
                dados["idade"] = int(input("Diga sua idade: "))
                break
            except ValueError:
                print("OPS! Esse valor não é válido! Digite uma idade válida")
        while True:
            try:
                dados["cpf"] = int(input("Diga seu cpf: "))
                break
            except ValueError:
                print("OPS! Esse valor não é válido! Digite um cpf válido")
        usuarios.append(dados.copy())

    for i in usuarios:
        if i['idade'] < 18:
            usuarios_menores.append(i)
            usuarios.remove(i)

    print(usuarios)
    print(usuarios_menores)

if __name__ == '__main__':
    cadastro()