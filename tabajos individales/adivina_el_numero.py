import random


def adivina_el_numero(x):
    print("*********************")
    print("*Bienvebido al juego*")
    print("*********************")
    print("\nTu meta es adivinar el numero creado por la 'PC'\n")
    numero_aleatorio=random.randint(1,x)#numero aleatorio entre 1 y x.
    
    prediccion=0 # definimos numero cero para que este no sea igual al primero y de simpre bien 
    while prediccion != numero_aleatorio: #el ciclo va continuar siempre y cuando el valor prediccion no sea igual al aleatorio.
        prediccion=int(input(f"Adivina un numero entre 1 y {x}: "))#f-string.
        if prediccion < numero_aleatorio:
            print("Intenta otra vez, el numero es muy pequeño")
        elif prediccion > numero_aleatorio:
            print("Intenta otra vez, el numero es muy grande")
    print(f"¡Felicitaviones adivinaste el numero {numero_aleatorio} correctamente")

adivina_el_numero(15)