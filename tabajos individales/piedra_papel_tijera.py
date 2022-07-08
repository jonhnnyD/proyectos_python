import random


def jugar():
    usuario = input("Escoje una opcion, Piedra, Papel o Tijera:\n").lower()
    computadora= random.choice(['piedra','papel','tiejra'])

    if usuario == computadora:
        print("¡Empataron!")
    elif gano_el_jugador(usuario, computadora):
        print(f"¡Ganaste!, la computadora escopgio {computadora}")
    else:
        print(f"¡Perdiste!, la computadora escogio {computadora}")


def gano_el_jugador(jugador, oponente):
    #retornar true (verdadero) si gana el jugador.
    #piedra gana a tijera(piedra > tijera)
    #tijera gana a pápel (papel<tijera)
    #papel gana a piedra (piedra< papel)
    if ((jugador== 'piedra' and oponente=='tijera' )
        or(jugador== 'tijera' and oponente=='papel')
        or(jugador=='papel' and oponente=='piedra')):
        return True  
    else:
        return False


print(jugar())

