class Animal():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f"o {self.nome} foi comer...")

class Gato(Animal):
    def _init__(self, nome, cor):
        super().__init__(nome, cor)

    def miar(self):
        print(f"o {self.nome} foi miando...")