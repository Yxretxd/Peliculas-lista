def peliculas_3():                  # en esta funcion sera para que la persona ingrese las 3 peliculas
    peliculas = []

    for i in range(3):
        pelicula = input(f"Ingrese el nombre de la pelicula #{i+1}: ")
        peliculas.append(pelicula)

    print("\nMas favorita:", peliculas[0])
    print("\nMenos favorita:", peliculas[-1])


def peliculas_5():                 # en esta otra funcion sirve para poder ingresar 5 peliculas utilizando el mismo algoritmo
    peliculas = []

    for i in range(5):
        pelicula = input(f"Ingrese el nombre de la pelicula # {i+1}: ")
        peliculas.append(pelicula)

    print("Mas favorita:", peliculas[0])
    print("Menos favorita:", peliculas[-1])


def contar_letras():
    palabras = []
    cantidades = []

    n = int(input("Cuantas palabras desea ingresar? "))

    for i in range(n):
        palabra = input(f"Ingrese la palabra #{i+1}: ")
        palabras.append(palabra)
        cantidades.append(len(palabra))

    print("Cantidad de letras:", cantidades)

peliculas_3()
peliculas_5()
contar_letras()
 


