import random


def opciones_principales():
    dado = int(input("¿De cuántas caras quieres el dado? "))
    print("\n")
    dados(dado)


def dados(dado):
    while True:
        print("En el dado de " + str(dado) + " caras ha aparecido el número " + str(random.randint(1, dado)))
        opcion = int(input("¿Quieres volver a lanzarlo? 1 para sí, 2 para no."))
        print("\n")
        if opcion == 2:
            break
    opciones_principales()


if __name__ == '__main__':
    opciones_principales()
