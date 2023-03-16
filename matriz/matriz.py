import numpy as np


def search_consecutive(matriz):
    matriz_resta = np.zeros((4, 5))
    matriz_booleana = np.zeros((3, 3))

    for i in range(0, 4):
        matriz_resta[i] = np.subtract(
            matriz[i:i+1], matriz[i+1:i+2])

    for i in range(0, 5):
        vector_a_analizar = matriz_resta[:, i]

        for n in [-1, 1]:
            if np.count_nonzero(vector_a_analizar == n) >= 3:
                # zip crea pares del primer elemento con el resto del arreglo
                matriz_booleana = [i2 == j2 for i2, j2 in zip(
                    vector_a_analizar, vector_a_analizar[1:])]

    return matriz_booleana


def main():
    matriz = np.random.randint(-32655, 32655, size=(5, 5))

    print(search_consecutive(matriz))
    search_consecutive(matriz.T)


if __name__ == '__main__':
    main()
