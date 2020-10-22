NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'
class Motor:
    def __init__(self, velocidade=0):
        self.__velocidade = velocidade

    @property
    def velocidade(self):
        return self.__velocidade

    def acelerar(self):
        self.__velocidade += 1
        print(f'Velocidade: {self.__velocidade}')
    def frear(self):
        self.__velocidade -= 2
        self.__velocidade = max(0, self.__velocidade)
        print(f'Velocidade: {self.__velocidade}')

class Direcao:
    rotacao_a_direita = {
        NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE
    }
    rotacao_a_esquerda = {
        NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: NORTE
    }
    def __init__(self):
        self.__direcao = NORTE

    def mover_direita(self):
        self.__direcao = self.rotacao_a_direita[self.__direcao]

    def mover_esquerda(self):
        self.__direcao = self.rotacao_a_esquerda[self.__direcao]

    def mostrar_direcao(self):
        print(f'Direção: {self.__direcao}')

class Carro:
    def __init__(self, motor, direcao):
        self.__motor = motor
        self.__direcao = direcao

    @property
    def motor(self):
        return self.__motor
    @property
    def direcao(self):
        return self.__direcao

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def mover_a_direita(self):
        self.direcao.mover_direita()

    def mover_a_esquerda(self):
        self.direcao.mover_esquerda()

    def mostar_direcao(self):
        self.direcao.mostrar_direcao()

if __name__ == '__main__':
    def iniciar_carro():
        motor = Motor()
        direcao = Direcao()
        carro = Carro(motor, direcao)

        while True:
            op = str(input('5- Acelerar | 6- Frear | A- Esquerda | D- Direita | 0- Desligar e sair: '))
            if op == '5':
                carro.acelerar()
            elif op == '6':
                carro.frear()
            elif op in 'Aa':
                carro.mover_a_esquerda()
                carro.mostar_direcao()
            elif op in 'Dd':
                carro.mover_a_direita()
                carro.mostar_direcao()
            elif op == '0':
                break
            else:
                print('Escolha uma opção válida.')


    iniciar_carro()