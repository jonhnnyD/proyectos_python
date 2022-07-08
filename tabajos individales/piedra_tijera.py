import random


print("=======================================")
print("=¡Vamos a jugar Piedra, Papel o tiejra=")
print("=======================================")

def jugar ():
    usuario=input("escoje una opcion: 'piedra', 'papel', 'tijera'.\n").lower()
    comp= random.choice(['piedra', 'papel', 'tijera'])
    
    if usuario == comp:
        print(f"¡Empataron")
    elif ((usuario == 'tijera' and comp == 'papel')
         or(usuario == 'piedra' and comp == 'tijera')
         or(usuario == 'papel' and comp == 'piedra')):
         print(f"¡Ganaste! la computadora escogio {comp}")
    elif((comp == 'tijera' and usuario == 'papel')
         or(comp == 'piedra' and usuario == 'tijera')
         or(comp == 'papel' and usuario == 'piedra')):
         print(f"¡Perdiste! la computadora escogio {comp}")
    

jugar()