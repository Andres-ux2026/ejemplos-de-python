alumnos=[] #lista vacia

""" while True:
    nombre= input("ingresa el nombre de un alumno :")

    if nombre =="salir":
        break 
    alumnos.append(nombre) 
    print(alumnos) """


while True:
    print("--------------MENU")
    print("ingresa opcion 1 agregar ")
    print("ingresa opcion 2: borrar")
    menu=input("Ingresa la opcion:")

    if menu == "1":

        nombre=input("ingresa un nombre:  ")
        alumnos.append(nombre)
        print(alumnos)
    elif menu =="2":
        nombre=input("ingrese nombre a borrar:  ")
        alumnos.remove(nombre)
        print(alumnos)
    else:
        break


    
    
