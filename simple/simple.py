import random


def simple():
    id = [n for n in range(1, 11)]
    edad = [random.randint(1, 100) for n in id]
    return [{"id": n, "edad": m} for n, m in zip(id, edad)]


def workin_with_list(lista):
    # Vamos a ordenar la lista de mayor a menor segun la edad
    list_sorted = sorted(lista, key=lambda k: k['edad'], reverse=True)

    print(list_sorted[0]["id"])
    print(list_sorted[len(list_sorted)-1]["id"])
    return (list_sorted)


def main():
    workin_with_list(simple())


if __name__ == '__main__':
    main()
