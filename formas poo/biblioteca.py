class Forma():
    def __init__(self, area, perimetro):
        self.area = area
        self.perimetro = perimetro
class Retangulo(Forma):
    def __init__(self, base, altura,):
        self.base = base
        self.altura = altura
        super().__init__(base * altura, 2 * (base + altura))
    def calcularArea(self):
        print(f"a área do retangulo é igual a: {self.area}")

    def calcularPerimetro(self):
        print(f"o perímetro do retângulo é igual a: {self.perimetro}")