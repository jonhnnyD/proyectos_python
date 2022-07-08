import random


def adivina_el_numero_computadora(x):

    print("******************************")
    print("***¡Bienvenido(a) al juego!***")
    print("******************************")
    print(f"\nSelecciona un número entre 1 y {x} para que la PC intente avidinar")

    limite_inferior = 1
    limite_superior = x

    respuesta = ""
    while respuesta != "c":
        #generar prediccion
        if limite_inferior != limite_superior: #[1,10]
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion=limite_inferior #También podria ser el limite_superior proque ambos son iguales

        #obtener respuesta del usuario
        respuesta=input(f"Mi prediccion es {prediccion}. Sies muy alta presiona (A) y si es muy baja presiona (B), si es correcta presiona (C): ").lower()

        if respuesta == "a":
            limite_superior = prediccion-1
        elif respuesta == "b" :
            limite_inferior = prediccion+1

    print(f"¡ Siiii la mamalona lo consiguio!, adivino tu numero correctametne: {prediccion}")   


adivina_el_numero_computadora(15)

    