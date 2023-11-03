class Animal():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f"o {self.nome} foi comer...")

    def emitirSom(self):
        print(f"o {self.nome} emitiu som...")
class Gato(Animal):
    def _init__(self, nome, cor):
        super().__init__(nome, cor)
    def emitirSom(self):
        print(f"o gato {self.nome} está miando...")

class Cachorro(Animal):
    def _init__(self, nome, cor):
        super().__init__(nome, cor)
    def emitirSom(self):
        print(f"o cachorro {self.nome} está latindo...")

class Vaca(Animal):
    def _init__(self, nome, cor):
        super().__init__(nome, cor)
    def emitirSom(self):
        print(f"a vaca {self.nome} está mugindo...")





