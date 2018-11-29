import random

aleatorio = random.randint(0,10)
oportunidad = 5
number=""

print(aleatorio)

"""while oportunidad > 0 and number != aleatorio:
    number = int(input("Por favor escoge un número del 1 al 10: "))
    if number == aleatorio:
        print("¡Has ganado el juego!")
    else:
        oportunidad -= 1
        print("Fallaste, lo siento, te quedan {} oportunidades".format(oportunidad))"""

while oportunidad > 0 and number != aleatorio:
    number = int(input("Por favor escoge un número del 1 al 10: "))
    if number != aleatorio:
        oportunidad -= 1
        print("Fallaste, lo siento, te quedan {} oportunidades".format(oportunidad))
    else:
        print("¡Has ganado el juego!")
        break