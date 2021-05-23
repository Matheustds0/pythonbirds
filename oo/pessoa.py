class Pessoa:
    olhos = 2

    def __init__(self, nome=None, idade = 35, *filhos):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42
    @classmethod
    def nome_atributos_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_classe_pai = super().cumprimentar()
        return f'{cumprimentar_classe_pai}. Aperto de mão'

class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    renzo = Mutante(nome = 'Renzo')
    luciano = Homem('Luciano', 49, renzo)
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Ramalho'
    del luciano.filhos
    luciano.olhos = 1
    del luciano.olhos
    print(luciano.__dict__)
    print(renzo.__dict__)
    print(Pessoa.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(renzo.olhos))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_atributos_classe(), luciano.nome_atributos_classe())
    pessoa = Pessoa('Anônimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa,Homem))
    print(isinstance(renzo, Pessoa))
    print(isinstance(renzo, Homem))
    print(renzo.olhos)
    print(luciano.cumprimentar())
    print(renzo.cumprimentar())