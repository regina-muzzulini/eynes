# del modulo circulo (circulo.py) importamos la clase Circulo
from circulo import Circulo


def main():
    radio = Circulo(float(input("Ingrese el radio del circulo: ")))

    print("\n P (calcula el perimetro) \n A (calcula el area) \n M (modifica el radio del circulo) \n V (Visualiza el radio actual) \n S para salir")
    res = input(" Ingrese la opcion: ")

    while res.upper() != "S":
        if res.upper() == "P":
            print(f' Perimetro = {radio.perimetro():.2f}')

        elif res.upper() == "A":
            print(f' Area = {radio.area():.2f}')

        elif res.upper() == "M":
            radio.set_Radio(float(input("Ingrese el radio: ")))

        elif res.upper() == "V":
            print(f' Radio = {radio.get_Radio():.2f}')

        print("\n P (calcula el perimetro) \n A (calcula el area) \n M-8 (modifica el radio del circulo) \n V (Visualiza el radio actual) \n S para salir")
        res = input(" Ingrese la opcion: ")


if __name__ == '__main__':
    main()
