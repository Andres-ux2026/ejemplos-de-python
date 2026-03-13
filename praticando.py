# proyecto de lista de peliculas de netflix
#generar lista vacia
#int() consultar o pedir datos
#agregar peliculas
#lborrar  peliculas
#ver peliculas

peliculas= []

while True:

    print("---------- MENU------------")
    print("1 - Agregar peliculas  ")
    print("2 - Ver lista de peliculas")
    print("3- Borrar peliculas ")
    print("4- Salir")

    opcion= input("Selecciona una opcion: ")

    if opcion == "1":

        nombre_pelicula= input("Ingrese el nombre de la pelicula: ") 
        anio= input("Ingrese el año: ")
        genero= input("Ingrese genero: ")


        pelicula ={
        "nombre":nombre_pelicula,
        "anio": anio,
        "genero":genero,    

        }   
        peliculas.append(pelicula)
    
    elif opcion == "2":
        print(pelicula["nombre"], "-",pelicula["anio"], "-",pelicula["genero"])

    elif opcion =="3":

        print(pelicula["nombre"], "-",pelicula["anio"], "-",pelicula["genero"])
        elimi_peli=input(" Escriba el nombre de la pelicula a eliminar: ")

        for peli in peliculas:

            if peli["nombre"] == elimi_peli:

                peliculas.remove(peli)
                print("Pelicula Borrada")
                

    




 
