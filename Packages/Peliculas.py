from Packages.Menus import *
from Packages.Funciones import *

import time
import os
import os.path as path

def peliculas(contenidoPeliculas, codigosPeliculas):
    def agregarPelicula(contenidoPeliculas, codigosPeliculas):
        cuantasPeliculasParaAgregar = preguntarNumeroNormal("Cuantas peliculas deseas agregar?", 0)
        for i in range(cuantasPeliculasParaAgregar):
            listaPelicula = []
            while True:
                nombre = input(f"\n───> Digita el nombre de la pelicula #{i+1}: ")
                encontroNombrePelicula = 0
                for j in range(len(contenidoPeliculas)):
                    if nombre == contenidoPeliculas[j][0]:
                        encontroNombrePelicula = 1
                        break
                if encontroNombrePelicula == 1:
                    print(f"\nYa has agregado la pelicula con nombre {nombre}")
                else:
                    break 
            calificacion = preguntarNumeroNormal(f"Digita la calificacion de {nombre}", 1)
            duracion = preguntarNumeroNormal(f"Cuanto es la duracion de {nombre} en minutos?", 0)
            cuantosGenerosTiene = preguntarNumeroNormal(f"Cuantos generos tiene {nombre}?", 0)
            listaGeneros = []
            for j in range(cuantosGenerosTiene):
                generos = input(f"───> Digita el genero #{j+1} de {nombre}: ")
                listaGeneros.append(generos)
            listaGeneros.sort()
            año = preguntarNumeroNormal(f"En que año se estreno {nombre}?", 0)
            if len(codigosPeliculas) == 0:
                codigo = 0
            else:
                codigo = codigosPeliculas[len(codigosPeliculas)-1] + 1
            codigosPeliculas.append(codigo)
            listaPelicula.append(nombre) #0
            listaPelicula.append(calificacion) #1
            listaPelicula.append(duracion) #2
            listaPelicula.append(listaGeneros) #3
            listaPelicula.append(año) #4
            listaPelicula.append(codigo) #5
            contenidoPeliculas.append(listaPelicula)
            print(f"\nLa pelicula con nombre {nombre} ha sido agregada con exito!")
        print("")

    def buscarPeliculaXNombre(contenidoPeliculas, codigosPeliculas):
        encontroPelicula = 0
        nombreParaBuscar = input("───> Digite el nombre a buscar: ")
        print(f"\nPeliculas con la palabra {nombreParaBuscar}:\n")
        for i in range(len(contenidoPeliculas)):
            if contenidoPeliculas[i][0].find(nombreParaBuscar) != -1:
                print(f"""Nombre: {contenidoPeliculas[i][0]}
 Calificacion: {contenidoPeliculas[i][1]}
 Duracion: {contenidoPeliculas[i][2]} minutos""")
                print(" Generos: ", end = '')
                for j in range(len(contenidoPeliculas[i][3])):
                    if len(contenidoPeliculas[i][3])-1 == j:
                        print(f"{contenidoPeliculas[i][3][j]}", end = '')
                    else:
                        print(f"{contenidoPeliculas[i][3][j]} / ", end = '')
                print(f"\n Año: {contenidoPeliculas[i][4]}")
                print(f" Codigo: {contenidoPeliculas[i][5]}\n")
                encontroPelicula = 1
        if encontroPelicula == 0:
            print(f"No se ha encontrado ningun nombre con '{nombreParaBuscar}'\n")

    def buscarPeliculaXGenero(contenidoPeliculas, codigosPeliculas):
        encontroPelicula = 0
        generosDisponibles = []
        for i in range(len(contenidoPeliculas)):
            for j in range(len(contenidoPeliculas[i][3])):
                if contenidoPeliculas[i][3][j] not in generosDisponibles:
                    generosDisponibles.append(contenidoPeliculas[i][3][j])
        generosDisponibles.sort()
        print("Generos Encontrados: \n")
        for i in range(len(generosDisponibles)):
            if len(generosDisponibles)-1 == i:
                print(f"{generosDisponibles[i]}", end = '')
            else:
                print(f"{generosDisponibles[i]}, ", end = '')
        print("\n")
        cuantoGenerosParaBuscar = preguntarNumeroNormal(f"Cuantos generos deseas buscar?", 0)
        generosParaBuscar = []
        for i in range(cuantoGenerosParaBuscar):
            while True:
                generoParaBuscar = input(f"───> Digite el genero #{i+1} a buscar: ")
                if generoParaBuscar in generosDisponibles:
                    generosParaBuscar.append(generoParaBuscar)
                    break
                else:
                    print(f"\nNo se ha encontrado ningun genero con el nombre de {generoParaBuscar}\n")
        print(f"\nPeliculas con generos: ", end = '')
        for i in range(len(generosParaBuscar)):
            if len(generosParaBuscar)-1 == i:
                print(f"{generosParaBuscar[i]}", end = '')
            else:
                print(f"{generosParaBuscar[i]}, ", end = '')
        print("\n")
        for i in range(len(contenidoPeliculas)):
            contenidoGenerosPeliculas = []
            for w in range(len(generosParaBuscar)):
                if generosParaBuscar[w] in contenidoPeliculas[i][3]:
                    contenidoGenerosPeliculas.append(generosParaBuscar[w])
            if generosParaBuscar == contenidoGenerosPeliculas:
                print(f"""Nombre: {contenidoPeliculas[i][0]}
 Calificacion: {contenidoPeliculas[i][1]}
 Duracion: {contenidoPeliculas[i][2]} minutos""")
                print(" Generos: ", end = '')
                for j in range(len(contenidoPeliculas[i][3])):
                    if len(contenidoPeliculas[i][3])-1 == j:
                        print(f"{contenidoPeliculas[i][3][j]}", end = '')
                    else:
                        print(f"{contenidoPeliculas[i][3][j]} / ", end = '')
                print(f"\n Año: {contenidoPeliculas[i][4]}")
                print(f" Codigo: {contenidoPeliculas[i][5]}\n")
                encontroPelicula = 1
        if encontroPelicula == 0:
            print(f"No se ha encontrado ningun genero de los que digistaste\n")
    
    def mostrarPeliculas(contenidoPeliculas, codigosPeliculas):
        print("Peliculas que has visto:\n")
        for i in range(len(contenidoPeliculas)):
            print(f"""Nombre: {contenidoPeliculas[i][0]}
 Calificacion: {contenidoPeliculas[i][1]}
 Duracion: {contenidoPeliculas[i][2]} minutos""")
            print(" Generos: ", end = '')
            for j in range(len(contenidoPeliculas[i][3])):
                if len(contenidoPeliculas[i][3])-1 == j:
                    print(f"{contenidoPeliculas[i][3][j]}", end = '')
                else:
                    print(f"{contenidoPeliculas[i][3][j]} / ", end = '')
            print(f"\n Año: {contenidoPeliculas[i][4]}")
            print(f" Codigo: {contenidoPeliculas[i][5]}\n")

    def editarPelicula(contenidoPeliculas, codigosPeliculas):
        mostrarPeliculas(contenidoPeliculas, codigosPeliculas)
        while True:
            print("Si no deseas editar ninguna pelicula digita -1\n")
            codigoParaEditarPelicula = preguntarNumeroNormal("Digita el codigo de la pelicula que deseas editar", 2)
            if codigoParaEditarPelicula != -1 and codigoParaEditarPelicula >= 0:
                if codigoParaEditarPelicula in codigosPeliculas:
                    print("")
                    break
                else:
                    print("\nEl codigo no se encuentra en nuestra base de datos\n")
            elif codigoParaEditarPelicula == -1:
                print("")
                return
            else:
                print("\nLos codigos empiezan en 0\n")
        while True:
            os.system('cls')
            print(f"""Nombre: {contenidoPeliculas[codigoParaEditarPelicula][0]}
 Calificacion: {contenidoPeliculas[codigoParaEditarPelicula][1]}
 Duracion: {contenidoPeliculas[codigoParaEditarPelicula][2]} minutos""")
            print(" Generos: ", end = '')
            for j in range(len(contenidoPeliculas[codigoParaEditarPelicula][3])):
                if len(contenidoPeliculas[codigoParaEditarPelicula][3])-1 == j:
                    print(f"{contenidoPeliculas[codigoParaEditarPelicula][3][j]}", end = '')
                else:
                    print(f"{contenidoPeliculas[codigoParaEditarPelicula][3][j]} / ", end = '')
            print(f"\n Año: {contenidoPeliculas[codigoParaEditarPelicula][4]}")
            print(f" Codigo: {contenidoPeliculas[codigoParaEditarPelicula][5]}\n")
            menuEditarPelicula()
            opcionMenuEditarPelicula = preguntarNumero(0, 6, "[0,1,2,3,4,5,6]")
            os.system('cls')
            print(f"""Nombre: {contenidoPeliculas[codigoParaEditarPelicula][0]}
 Calificacion: {contenidoPeliculas[codigoParaEditarPelicula][1]}
 Duracion: {contenidoPeliculas[codigoParaEditarPelicula][2]} minutos""")
            print(" Generos: ", end = '')
            for j in range(len(contenidoPeliculas[codigoParaEditarPelicula][3])):
                if len(contenidoPeliculas[codigoParaEditarPelicula][3])-1 == j:
                    print(f"{contenidoPeliculas[codigoParaEditarPelicula][3][j]}", end = '')
                else:
                    print(f"{contenidoPeliculas[codigoParaEditarPelicula][3][j]} / ", end = '')
            print(f"\n Año: {contenidoPeliculas[codigoParaEditarPelicula][4]}")
            print(f" Codigo: {contenidoPeliculas[codigoParaEditarPelicula][5]}\n")
            if opcionMenuEditarPelicula == 0: #Volver
                return
            if opcionMenuEditarPelicula == 1: #Nombre
                nombre = input(f"───> Digita nuevamente el nombre de la pelicula: ")
                contenidoPeliculas[codigoParaEditarPelicula][0] = nombre
            if opcionMenuEditarPelicula == 2: #Calificacion
                calificacion = preguntarNumeroNormal(f"Digita nuevamente la calificacion de {contenidoPeliculas[codigoParaEditarPelicula][0]}", 1)
                contenidoPeliculas[codigoParaEditarPelicula][1] = calificacion
            if opcionMenuEditarPelicula == 3: #Duracion
                duracion = preguntarNumeroNormal(f"Cuanto es la duracion nuevamente de {contenidoPeliculas[codigoParaEditarPelicula][0]} en minutos?", 0)
                contenidoPeliculas[codigoParaEditarPelicula][2] = duracion
            if opcionMenuEditarPelicula == 4: #Generos
                cuantosGenerosTiene = preguntarNumeroNormal(f"Cuantos generos tiene nuevamente {contenidoPeliculas[codigoParaEditarPelicula][0]}?", 0)
                listaGeneros = []
                for i in range(cuantosGenerosTiene):
                    generos = input(f"───> Digita nuevamente el genero #{i+1} de {contenidoPeliculas[codigoParaEditarPelicula][0]}: ")
                    listaGeneros.append(generos)
                listaGeneros.sort()
                contenidoPeliculas[codigoParaEditarPelicula][3] = listaGeneros
            if opcionMenuEditarPelicula == 5: #Año
                año = preguntarNumeroNormal(f"En que año se estreno nuevamente {contenidoPeliculas[codigoParaEditarPelicula][0]}?", 0)
                contenidoPeliculas[codigoParaEditarPelicula][4] = año
            if opcionMenuEditarPelicula == 6: #Todo
                nombre = input(f"───> Digita nuevamente el nombre de la pelicula: ")
                contenidoPeliculas[codigoParaEditarPelicula][0] = nombre
                calificacion = preguntarNumeroNormal(f"Digita nuevamente la calificacion de {nombre}", 1)
                contenidoPeliculas[codigoParaEditarPelicula][1] = calificacion
                duracion = preguntarNumeroNormal(f"Cuanto es la duracion nuevamente de {nombre} en minutos?", 0)
                contenidoPeliculas[codigoParaEditarPelicula][2] = duracion
                cuantosGenerosTiene = preguntarNumeroNormal(f"Cuantos generos tiene nuevamente {nombre}?", 0)
                listaGeneros = []
                for i in range(cuantosGenerosTiene):
                    generos = input(f"───> Digita nuevamente el genero #{i+1} de {nombre}: ")
                    listaGeneros.append(generos)
                listaGeneros.sort()
                contenidoPeliculas[codigoParaEditarPelicula][3] = listaGeneros
                año = preguntarNumeroNormal(f"En que año se estreno nuevamente {nombre}?", 0)
                contenidoPeliculas[codigoParaEditarPelicula][4] = año                       
            guardarArchivoPeliculas(contenidoPeliculas, codigosPeliculas)
            print("")
    
    def borrarPelicula(contenidoPeliculas, codigosPeliculas):
        mostrarPeliculas(contenidoPeliculas, codigosPeliculas)
        while True:
            print("Si no deseas borrar ninguna pelicula digita -1\n")
            codigoParaBorrarPelicula = preguntarNumeroNormal("Digita el codigo de la pelicula que deseas borrar", 2)
            if codigoParaBorrarPelicula != -1 and codigoParaBorrarPelicula >= 0:
                if codigoParaBorrarPelicula in codigosPeliculas:
                    print("")
                    break
                else:
                    print("\nEl codigo no se encuentra en nuestra base de datos\n")
            elif codigoParaBorrarPelicula == -1:
                print("")
                return
            else:
                print("\nLos codigos empiezan en 0\n")
        posicionParaCambiarCodigos = None
        for i in range(len(contenidoPeliculas.copy())):
            if codigoParaBorrarPelicula == contenidoPeliculas[i][5]:
                contenidoPeliculas.pop(i)
                codigosPeliculas.pop(i)
                posicionParaCambiarCodigos = i
                print(f"La pelicula con codigo {codigoParaBorrarPelicula} se ha borrado con exito!\n")
                break
        while posicionParaCambiarCodigos <= len(codigosPeliculas)-1:
            codigosPeliculas[posicionParaCambiarCodigos] -= 1
            posicionParaCambiarCodigos += 1
            
    while True:
        menuPeliculas()
        opcionMenuPeliculas = preguntarNumero(0, 6, "[0,1,2,3,4,5,6]")
        os.system('cls')
        if opcionMenuPeliculas == 0: #Volver
            return
        if opcionMenuPeliculas == 1: #Agregar
            if len(contenidoPeliculas) == 0:
                print("No has colocado ninguna pelicula\n")
            else:
                agregarPelicula(contenidoPeliculas, codigosPeliculas)
        if opcionMenuPeliculas == 2: #Editar
            if len(contenidoPeliculas) == 0:
                print("No has colocado ninguna pelicula\n")
            else:
                editarPelicula(contenidoPeliculas, codigosPeliculas)
        if opcionMenuPeliculas == 3: #Buscar x nombre
            if len(contenidoPeliculas) == 0:
                print("No has colocado ninguna pelicula\n")
            else:
                buscarPeliculaXNombre(contenidoPeliculas, codigosPeliculas)
        if opcionMenuPeliculas == 4: #Buscar x genero
            if len(contenidoPeliculas) == 0:
                print("No has colocado ninguna pelicula\n")
            else:
                buscarPeliculaXGenero(contenidoPeliculas, codigosPeliculas)
        if opcionMenuPeliculas == 5: #Borrar
            if len(contenidoPeliculas) == 0:
                print("No has colocado ninguna pelicula\n")
            else:
                borrarPelicula(contenidoPeliculas, codigosPeliculas)
        if opcionMenuPeliculas == 6: #Mostrar
            if len(contenidoPeliculas) == 0:
                print("No has colocado ninguna pelicula\n")
            else:
                mostrarPeliculas(contenidoPeliculas, codigosPeliculas)
        contenidoPeliculas.sort()
        for i in range(len(contenidoPeliculas)):
            contenidoPeliculas[i][5] = codigosPeliculas[i]
        guardarArchivoPeliculas(contenidoPeliculas, codigosPeliculas)