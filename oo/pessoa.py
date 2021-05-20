class Pessoa:
    def __init__(self, nome=None, idade = 35, *filhos):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

if __name__ == '__main__':
    renzo = Pessoa(nome = 'Renzo')
    luciano = Pessoa('Luciano', 49, renzo)
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)