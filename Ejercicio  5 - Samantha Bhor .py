# PANDAS
# Ejercicio #5
# Persistencia de datos con pandas
# Videojuegos que puedes comprar
# Audrey Samantha Bhor López
# Carné no. 22545

import pandas as pd
import numpy as np

print("***************************************************************************************************************************************************")
print("         Bienvenido, con ayuda de este programa lograrás encontrar los mejore videojuegos que puedes comprar y divertirte al máximo                ")
print("***************************************************************************************************************************************************")

videojuegos_arch= pd.read_csv("Video_Games_Sales.csv", encoding="latin")

def menudeopciones():
    opciones = '\n1: Visualizar los videojuegos  \n2: Top de ventas por región \n3: Top de ventas globales \n4: Puntaje por un crítico \n5: Puntaje por un usuario \n6: Rating de los videojuegos \n7: Salir'
    op = 0
    print(opciones)
    op = input('Seleccione una opción: ')
    print("---------------------------------------------------------------------------------------------------------------------------------------")
    bandera = False
    while not bandera:
        if op.isdigit():
            op = int(op)
            if op>0 and op<=7:
                 bandera = True
            else:
                print("Error, Ingrese una opción correcta de las que está en el menú")
                op = input('Seleccione una opción: ')
        else:
            print("Error, Debe ingresar un número de los que están en el menú: ")
            op = input('Seleccione una opción: \n')
    return op

opcion_usu = menudeopciones()

while opcion_usu != 7 : ### si se cumple se sale del while

    if opcion_usu == 1 :
        print ("Bienvenido, en este apartado lograrás ver  100 videojuegos seleccionados de muchos años con toda su información, se muestran 50 ya que son demasiados\n")
        print(videojuegos_arch[["Name", "Platform","Year_of_Release", "Genre", "Developer"]].head(100))
        opcion_usu=menudeopciones()

    if opcion_usu == 2:
        print ("Bienvenido, en este apartado lograrás ver el top 10 de ventas de videojuegos según la región que elijas junto con el rating dado de ventas \n")

        opciones3 = '\n1: Top Europa \n2: Top Norte América \n3: Top Japón \n4: Top de Otros'
        op3=0
        print (opciones3)
        op3 = input('Seleccione una opción: ')

        if op3 == "1":
                print(videojuegos_arch.groupby("Name")["EU_Sales"].mean().sort_values(ascending=False).head(10)) # se le puede asignar a head un valor para mostrar la cantidad de valores
        elif op3 == "2":
                print(videojuegos_arch.groupby("Name")["EU_Sales"].mean().sort_values(ascending=False).head(10))
        elif op3 == "3":
               print(videojuegos_arch.groupby("Name")["JP_Sales"].mean().sort_values(ascending=False).head(10))
        elif op3 == "4":
             print(videojuegos_arch.groupby("Name")["Other_Sales"].mean().sort_values(ascending=False).head(10))

        opcion_usu=menudeopciones()

    if opcion_usu == 3:
        print ("Bienvenido, en este apartado lograrás ver el top 50 de ventas globales de los videojuegos \n")
        print(videojuegos_arch.groupby("Name")["Global_Sales"].mean().sort_values(ascending=False).head(50))
        opcion_usu=menudeopciones()

    if opcion_usu == 4:
         print ("Bienvenido, en este apartado lograrás ver un top por puntaje dado según un crítico de videojuegos\n")
         print(videojuegos_arch[["Name","Critic_Score", "Critic_Count"]].head(50).dropna()) # el dropna se utiliza para quitar datos nulos
         opcion_usu=menudeopciones()

    if opcion_usu == 5:
         print ("Bienvenido, en este apartado lograrás ver un top por puntaje dado según un usuario/s de los mismos\n")
         print(videojuegos_arch[["Name","User_Score", "User_Count"]].head(50).dropna())
         opcion_usu=menudeopciones()

    if opcion_usu == 6:
         print ("Bienvenido, en este apartado lograrás ver un top 50 de rating de los videojuegos siendo E : excelente, M: medio y T: terrible\n")
         print(videojuegos_arch[["Name","Rating"]].head(50).dropna()) # el dropna se utiliza para quitar datos nulos
         opcion_usu=menudeopciones()

    if opcion_usu == 7:
        print("Muchas gracias por usar este programa espero que te fuera de ayuda, te esperamos pronto")
        exit()

   
menudeopciones()
