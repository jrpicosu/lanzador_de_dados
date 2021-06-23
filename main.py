import random


def opciones_principales():
    print("Se dispone de distintos dados:")
    print("1 - Dado de 4 caras.")
    print("2 - Dado de 6 caras.")
    print("3 - Dado de 8 caras.")
    print("4 - Dado de 10 caras.")
    print("5 - Dado de 12 caras.")
    print("6 - Dado de 20 caras.")
    print("7 - Dado de 120 caras.")
    print("\n")
    dado = int(input("Elige una opción: "))

    if dado == 1:
        while True:
            print("En el dado ha aparecido el número " + str(random.randint(1, 4)))
            opcion = int(input("¿Quieres volver a lanzarlo? 1 para sí, 2 para no."))
            if opcion == 2:
                break
        opciones_principales()

    if dado == 2:
        while True:
            print("En el dado ha aparecido el número " + str(random.randint(1, 6)))
            opcion = int(input("¿Quieres volver a lanzarlo? 1 para sí, 2 para no."))
            if opcion == 2:
                break
        opciones_principales()

    if dado == 3:
        while True:
            print("En el dado ha aparecido el número " + str(random.randint(1, 8)))
            opcion = int(input("¿Quieres volver a lanzarlo? 1 para sí, 2 para no."))
            if opcion == 2:
                break
        opciones_principales()

    if dado == 4:
        while True:
            print("En el dado ha aparecido el número " + str(random.randint(1, 10)))
            opcion = int(input("¿Quieres volver a lanzarlo? 1 para sí, 2 para no."))
            if opcion == 2:
                break
        opciones_principales()

    if dado == 5:
        while True:
            print("En el dado ha aparecido el número " + str(random.randint(1, 12)))
            opcion = int(input("¿Quieres volver a lanzarlo? 1 para sí, 2 para no."))
            if opcion == 2:
                break
        opciones_principales()

    if dado == 6:
        while True:
            print("En el dado ha aparecido el número " + str(random.randint(1, 20)))
            opcion = int(input("¿Quieres volver a lanzarlo? 1 para sí, 2 para no."))
            if opcion == 2:
                break
        opciones_principales()

    if dado == 7:
        while True:
            print("En el dado ha aparecido el número " + str(random.randint(1, 120)))
            opcion = int(input("¿Quieres volver a lanzarlo? 1 para sí, 2 para no."))
            if opcion == 2:
                break
        opciones_principales()


if __name__ == '__main__':
    opciones_principales()
