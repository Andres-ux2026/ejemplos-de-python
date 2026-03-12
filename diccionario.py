## diccionarios
import os
persona = {
"nombre": "carlos",
"edad": 28,
"direccion": "las gaviotas",
"ciudad": "copiapo",
}

# acceder a los valores de nuestros diccionario con ["keys"]
""" print(persona["ciudad"]) """

# modificar valores en diccionarios 
persona["edad"]= 50  
persona["ciudad"]="Puerto Montt"

""" print(persona)

# agregar un dato nuevo

persona["pais"]= "Chile"
persona["altura"]= 180

print(persona)


# recorrer diccionario solo por keys

for k in persona:
    print(k)

# recorrer el diccionario solo por valores

for v in persona.values():
    print(v)

# recorrer y mostrar todos los datos

for k,v in persona.items():
    print(k,v)
 """

alumnos = [] #lista de diccionario de alumnos

while True:

    print("-----------------menu---------------")
    print("1. agregar alumno")
    print("2. ver alumnos")
    print("3. salir")
    
    opcion = input("elige una opcion: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    if opcion =="1":
        nombre = input("nombre de alumno: ")
        edad = input("edad de alumno: ")

        alumno ={
            "nombre": nombre, 
            "edad": edad
        }

        alumnos.append(alumno)
        print("alumno agregado")

    elif opcion =="2":

        print("--------------lista de alumnos----------")

        for alumno in alumnos:
            print(alumno["nombre"], "--" ,alumno["edad"])
            
    elif opcion =="3":
        print("programa cerrado")  
        break   
    else:
       os.system('cls' if os.name == 'nt' else 'clear')
       print("opcion incorrecta") 
       
               

