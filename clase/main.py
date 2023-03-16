# del modulo circulo (circulo.py) importamos la clase Circulo
from circulo import Circulo


def main():
    r = input("Ingrese el radio del circulo: ")
    radio = Circulo(float(r))

    print("\n P (calcula el perimetro) \n A (calcula el area) \n R (modifica el radio del circulo) \n V (Visualiza el radio actual) \n S para salir")
    res = input(" Ingrese la opcion: ")

    while res.upper() != "S":
        if res.upper() == "P":
            print(f' Perimetro = {radio.perimetro():.2f}')

        elif res.upper() == "A":
            print(f' Area = {radio.area():.2f}')

        elif res.upper() == "R":
            radio.set_Radio(float(input("Ingrese el radio: ")))

        elif res.upper() == "V":
            print(f' Radio = {radio.get_Radio():.2f}')

        print("\n P (calcula el perimetro) \n A (calcula el area) \n R (modifica el radio del circulo) \n V (Visualiza el radio actual) \n S para salir")
        res = input(" Ingrese la opcion: ")


if __name__ == '__main__':
    main()
