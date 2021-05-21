"""
Você deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classes:

    1.Motor
    2.Direção

O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:

    1.Atributo de dado velocidade
    2.Método acelerar, que deverá incremetar a velocidade de uma unidade
    3.Método frear que deverá decrementar a velocidade em duas unidades

A Direção terá a responsabilidade de controlar a direção. Ela oferece
os seguintes atributos:

    1.Valor de diração com valores possíveis: Norte, Sul, Leste, Oeste.
    2.Método girar_a_direita
    3.Método girar_a_esquerda

       N
    O     L
       S

Exemplo:
    >>> # Testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # Testando Direcao
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste
"""
class Motor():
    def __init__(self, velocidade = 0):
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade +=1

    def frear(self):
        self.velocidade -=2
        if self.velocidade<0:
            self.velocidade == 0

class Direcao():
    def __init__(self, posicao='norte'):
        self.posicao = posicao

    def girar_a_direita(self):
        if self.posicao == 'norte':
            self.posicao ='leste'
        elif self.posicao == 'leste':
            self.posicao = 'sul'
        elif self.posicao == 'sul':
            self.posicao = 'oeste'
        elif self.posicao == 'oeste':
            self.posicao = 'norte'

    def girar_a_esquerda(self):
        if self.posicao == 'norte':
            self.posicao = 'oeste'
        elif self.posicao == 'oeste':
            self.posicao = 'sul'
        elif self.posicao == 'sul':
            self.posicao = 'leste'
        elif self.posicao == 'leste':
            self.posicao = 'norte'

class Carro():

    def __init__(self, motor, direcao):
        self.motor = motor
        self.direcao = direcao
    def velocidade(self):
        return self.motor.velocidade()
    def acelerar(self):
        self.motor.acelerar()
    def frear(self):
        self.motor.frear()
    def direcao(self):
        return self.direcao.posicao
    def girar_a_direita(self):
        self.girar_a_direita()
    def girar_a_esquerda(self):
        self.girar_a_esquerda()




motor = Motor()
print(motor.velocidade)
motor.acelerar()
print(motor.velocidade)
motor.acelerar()
motor.acelerar()
motor.acelerar()
print(motor.velocidade)
motor.frear()
print(motor.velocidade)
motor.frear()
motor.frear()
print(motor.velocidade)

direcao = Direcao()
print(direcao.posicao)
direcao.girar_a_direita()
print(direcao.posicao)
direcao.girar_a_direita()
direcao.girar_a_direita()
print(direcao.posicao)
direcao.girar_a_esquerda()
print(direcao.posicao)
direcao.girar_a_esquerda()
direcao.girar_a_esquerda()
print(direcao.posicao)

carro = Carro(motor, direcao)
print(carro.motor.velocidade)
print(carro.direcao.posicao)

