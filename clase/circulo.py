import math


class Circulo:
    def __init__(self, radio=0):
        self.radio = radio if radio > 0 else print(
            "El radio no debe ser negativo.")

    # Getters (metodos GET)
    def get_Radio(self):
        return self.radio

    # Setters (metodos SET)
    def set_Radio(self, radio):
        self.radio = radio if radio > 0 else print(
            "El radio no debe ser negativo.")

    def area(self):
        return math.pi * self.radio**2

    def perimetro(self):
        return math.pi * (2 * self.radio)
