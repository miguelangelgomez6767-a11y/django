from figura import Figura
import math


class Cilindro(Figura):

    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura

    def calcular_volumen(self):
        return math.pi * (self.radio ** 2) * self.altura