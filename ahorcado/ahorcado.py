import random
import string

from vidas_ahorcado import vidas_dicionario_visual
from palabras import palabras


def obtener_palabra_valida(palbras):
    #seleccion palabra al azar 
    palabra=random.choice(palabras)
    while '-' in palabra or ' ' in palabra:
        palabra=random.choice(palabra)
    
    return palabra.upper()

def ahorcado():

    nombre = input("Hola, dime tu nombre: ").title()

    print("============================================================")
    print(f"Bienvenido {nombre} al juego del ahorcado¿Estas preparado? ")
    print("============================================================")

    palabra = obtener_palabra_valida(palabras)

    letras_por_avivinar = set(palabra)
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase)

    vidas = 7

    while len(letras_por_avivinar)>0 and vidas > 0:
        print(f"te quedan {vidas} vidas y has usado estas letras:{' '.join(letras_adivinadas)}")

        #mostrar el estado actual de la palabra 
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra ]
        print(vidas_dicionario_visual[vidas])
        #mostrar letras separadas por un espacio.
        print(f"Palabra:{' '.join(palabra_lista)}")

        letra_usuario = input(f"{nombre}, escoje una letra: ").upper()
        #si la letra escogida por el usuario esta en el abecedario y no esta en el conjunto de letras que ya se han ingrsado, se añade la letra al conjunto de letras ingresadas.
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)
            #si la letra esta en la palbra, remover la letra del conjunto pendiente por adivinar, si no estar restare una vida.
            if letra_usuario in letras_por_avivinar:
                letras_por_avivinar.remove(letra_usuario)
                print('')
            else:
                vidas -= 1 
                print(f"\nTu letra {letra_usuario} no esta en la palabra, jaja sigue intentando!")
        #si la letra escogida por el usuario ya fue ingresada
        elif letra_usuario in letras_adivinadas:
            print(f"Ya escogiste esa letra. Por favor escoge una letra nueva, tienes escristas las que ya elegiste!")
        else:
            print("\nEsta letra no es valida")
    #el juego llega a esta linea cuando se adivina todas las letras de la palabra o cuando se agotan las vidas del jugador 
    if vidas == 0:
        print(vidas_dicionario_visual[vidas])
        print(f"¡Ahorcado! Jajajaja! Perdiste {nombre}. La palabra era: {palabra} ")
    else:
        print(f"¡Diablos! adivinaste la palabra {palabra}, la proxima no sera tan sencillo {nombre}!")

ahorcado()