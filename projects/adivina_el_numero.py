import random


def adivina_el_numero(x):
    print("""
      =======================
        Bienvenido al Juego  
      =======================
      Tienes que adivinar el numero el numero que la computadora esta pensando.
    """)

    numero_aleatorio = random.randint(1, x)

    prediccion = 0

    while prediccion != numero_aleatorio:
        prediccion = int(input(f"Adivina el numero entre 1 y {x}: "))

        if prediccion < numero_aleatorio:
            print("Intenta de nuevo. Este número es muy pequeño.")
        elif prediccion > numero_aleatorio:
            print("Intenta de nuevo. Este número es muy grande")

    print(f"{prediccion} es el número que estoy pensando")
    print("Felicidades, Ganaste!!!")


adivina_el_numero(2)
adivina_el_numero(5)
adivina_el_numero(10)
