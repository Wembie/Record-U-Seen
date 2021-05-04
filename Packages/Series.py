from Packages.Menus import *
from Packages.Funciones import *

import time
import os
import os.path as path

def series(contenidoSeries, codigosSeries):
    def agregarSerie(contenidoSeries, codigosSeries):
        cuantasSeriesParaAgregar = preguntarNumeroNormal("Cuantas series deseas agregar?", 0)
        for i in range(cuantasSeriesParaAgregar):
            listaSerie = []
            while True:
                nombre = input(f"\n───> Digita el nombre de la serie #{i+1}: ")
                encontroNombreSerie = 0
                for j in range(len(contenidoSeries)):
                    if nombre == contenidoSeries[j][0]:
                        encontroNombreSerie = 1
                        break
                if encontroNombreSerie == 1:
                    print(f"\nYa has agregado la serie con nombre {nombre}")
                else:
                    break   
            calificacion = preguntarNumeroNormal(f"Digita la calificacion de {nombre}", 1)
            temporadas = preguntarNumeroNormal(f"Cuantas temporadas tiene {nombre}?", 0)
            cuantosGenerosTiene = preguntarNumeroNormal(f"Cuantos generos tiene {nombre}?", 0)
            listaGeneros = []
            for j in range(cuantosGenerosTiene):
                generos = input(f"───> Digita el genero #{j+1} de {nombre}: ")
                listaGeneros.append(generos)
            listaGeneros.sort()
            año = preguntarNumeroNormal(f"En que año se estreno {nombre}?", 0)
            if len(codigosSeries) == 0:
                codigo = 0
            else:
                codigo = codigosSeries[len(codigosSeries)-1] + 1
            codigosSeries.append(codigo)
            listaSerie.append(nombre) #0
            listaSerie.append(calificacion) #1
            listaSerie.append(temporadas) #2
            listaSerie.append(listaGeneros) #3
            listaSerie.append(año) #4
            listaSerie.append(codigo) #5
            contenidoSeries.append(listaSerie)
            print(f"\nLa serie con nombre {nombre} ha sido agregado con exito!")
        print("")

    def buscarSerieXNombre(contenidoSeries, codigosSeries):
        encontroSerie = 0
        nombreParaBuscar = input("───> Digite el nombre a buscar: ")
        print(f"\nAnimes con la palabra {nombreParaBuscar}:\n")
        for i in range(len(contenidoSeries)):
            if contenidoSeries[i][0].find(nombreParaBuscar) != -1:
                print(f"""Nombre: {contenidoSeries[i][0]}
 Calificacion: {contenidoSeries[i][1]}
 Temporadas: {contenidoSeries[i][2]}""")
                print(" Generos: ", end = '')
                for j in range(len(contenidoSeries[i][3])):
                    if len(contenidoSeries[i][3])-1 == j:
                        print(f"{contenidoSeries[i][3][j]}", end = '')
                    else:
                        print(f"{contenidoSeries[i][3][j]} / ", end = '')
                print(f"\n Año: {contenidoSeries[i][4]}")
                print(f" Codigo: {contenidoSeries[i][5]}\n")
                encontroSerie = 1
        if encontroSerie == 0:
            print(f"No se ha encontrado ningun nombre con '{nombreParaBuscar}'\n")

    def buscarSerieXGenero(contenidoSeries, codigosSeries):
        encontroSerie = 0
        generosDisponibles = []
        for i in range(len(contenidoSeries)):
            for j in range(len(contenidoSeries[i][3])):
                if contenidoSeries[i][3][j] not in generosDisponibles:
                    generosDisponibles.append(contenidoSeries[i][3][j])
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
        print(f"\nSeries con generos: ", end = '')
        for i in range(len(generosParaBuscar)):
            if len(generosParaBuscar)-1 == i:
                print(f"{generosParaBuscar[i]}", end = '')
            else:
                print(f"{generosParaBuscar[i]}, ", end = '')
        print("\n")
        for i in range(len(contenidoSeries)):
            contenidoGenerosSeries = []
            for w in range(len(generosParaBuscar)):
                if generosParaBuscar[w] in contenidoSeries[i][3]:
                    contenidoGenerosSeries.append(generosParaBuscar[w])
            if generosParaBuscar == contenidoGenerosSeries:
                print(f"""Nombre: {contenidoSeries[i][0]}
 Calificacion: {contenidoSeries[i][1]}
 Temporadas: {contenidoSeries[i][2]}""")
                print(" Generos: ", end = '')
                for j in range(len(contenidoSeries[i][3])):
                    if len(contenidoSeries[i][3])-1 == j:
                        print(f"{contenidoSeries[i][3][j]}", end = '')
                    else:
                        print(f"{contenidoSeries[i][3][j]} / ", end = '')
                print(f"\n Año: {contenidoSeries[i][4]}")
                print(f" Codigo: {contenidoSeries[i][5]}\n")
                encontroSerie = 1
        if encontroSerie == 0:
            print(f"No se ha encontrado ningun genero de los que digistaste\n")
    
    def mostrarSeries(contenidoSeries, codigosSeries):
        print("Series que has visto:\n")
        for i in range(len(contenidoSeries)):
            print(f"""Nombre: {contenidoSeries[i][0]}
 Calificacion: {contenidoSeries[i][1]}
 Temporadas: {contenidoSeries[i][2]}""")
            print(" Generos: ", end = '')
            for j in range(len(contenidoSeries[i][3])):
                if len(contenidoSeries[i][3])-1 == j:
                    print(f"{contenidoSeries[i][3][j]}", end = '')
                else:
                    print(f"{contenidoSeries[i][3][j]} / ", end = '')
            print(f"\n Año: {contenidoSeries[i][4]}")
            print(f" Codigo: {contenidoSeries[i][5]}\n")

    def editarSerie(contenidoSeries, codigosSeries):
        mostrarSeries(contenidoSeries, codigosSeries)
        while True:
            print("Si no deseas editar ninguna serie digita -1\n")
            codigoParaEditarSerie = preguntarNumeroNormal("Digita el codigo de la serie que deseas editar", 2)
            if codigoParaEditarSerie != -1 and codigoParaEditarSerie >= 0:
                if codigoParaEditarSerie in codigosSeries:
                    print("")
                    break
                else:
                    print("\nEl codigo no se encuentra en nuestra base de datos\n")
            elif codigoParaEditarSerie == -1:
                print("")
                return
            else:
                print("\nLos codigos empiezan en 0\n")
        while True:
            os.system('cls')
            print(f"""Nombre: {contenidoSeries[codigoParaEditarSerie][0]}
 Calificacion: {contenidoSeries[codigoParaEditarSerie][1]}
 Temporadas: {contenidoSeries[codigoParaEditarSerie][2]}""")
            print(" Generos: ", end = '')
            for j in range(len(contenidoSeries[codigoParaEditarSerie][3])):
                if len(contenidoSeries[codigoParaEditarSerie][3])-1 == j:
                    print(f"{contenidoSeries[codigoParaEditarSerie][3][j]}", end = '')
                else:
                    print(f"{contenidoSeries[codigoParaEditarSerie][3][j]} / ", end = '')
            print(f"\n Año: {contenidoSeries[codigoParaEditarSerie][4]}")
            print(f" Codigo: {contenidoSeries[codigoParaEditarSerie][5]}\n")
            menuEditarSerie()
            opcionMenuEditarSerie = preguntarNumero(0, 6, "[0,1,2,3,4,5,6]")
            os.system('cls')
            print(f"""Nombre: {contenidoSeries[codigoParaEditarSerie][0]}
 Calificacion: {contenidoSeries[codigoParaEditarSerie][1]}
 Temporadas: {contenidoSeries[codigoParaEditarSerie][2]}""")
            print(" Generos: ", end = '')
            for j in range(len(contenidoSeries[codigoParaEditarSerie][3])):
                if len(contenidoSeries[codigoParaEditarSerie][3])-1 == j:
                    print(f"{contenidoSeries[codigoParaEditarSerie][3][j]}", end = '')
                else:
                    print(f"{contenidoSeries[codigoParaEditarSerie][3][j]} / ", end = '')
            print(f"\n Año: {contenidoSeries[codigoParaEditarSerie][4]}")
            print(f" Codigo: {contenidoSeries[codigoParaEditarSerie][5]}\n")
            if opcionMenuEditarSerie == 0: #Volver
                return
            if opcionMenuEditarSerie == 1: #Nombre
                nombre = input(f"───> Digita nuevamente el nombre de la serie: ")
                contenidoSeries[codigoParaEditarSerie][0] = nombre
            if opcionMenuEditarSerie == 2: #Calificacion
                calificacion = preguntarNumeroNormal(f"Digita nuevamente la calificacion de {contenidoSeries[codigoParaEditarSerie][0]}", 1)
                contenidoSeries[codigoParaEditarSerie][1] = calificacion
            if opcionMenuEditarSerie == 3: #Temporadas
                temporadas = preguntarNumeroNormal(f"Cuantas temporadas tiene nuevamente {contenidoSeries[codigoParaEditarSerie][0]}?", 0)
                contenidoSeries[codigoParaEditarSerie][2] = temporadas
            if opcionMenuEditarSerie == 4: #Generos
                cuantosGenerosTiene = preguntarNumeroNormal(f"Cuantos generos tiene nuevamente {contenidoSeries[codigoParaEditarSerie][0]}?", 0)
                listaGeneros = []
                for i in range(cuantosGenerosTiene):
                    generos = input(f"───> Digita nuevamente el genero #{i+1} de {contenidoSeries[codigoParaEditarSerie][0]}: ")
                    listaGeneros.append(generos)
                listaGeneros.sort()
                contenidoSeries[codigoParaEditarSerie][3] = listaGeneros
            if opcionMenuEditarSerie == 5: #Año
                año = preguntarNumeroNormal(f"En que año se estreno nuevamente {contenidoSeries[codigoParaEditarSerie][0]}?", 0)
                contenidoSeries[codigoParaEditarSerie][4] = año
            if opcionMenuEditarSerie == 6: #Todo
                nombre = input(f"───> Digita nuevamente el nombre de la serie: ")
                contenidoSeries[codigoParaEditarSerie][0] = nombre
                calificacion = preguntarNumeroNormal(f"Digita nuevamente la calificacion de {nombre}", 1)
                contenidoSeries[codigoParaEditarSerie][1] = calificacion
                temporadas = preguntarNumeroNormal(f"Cuantas temporadas tiene nuevamente {nombre}?", 0)
                contenidoSeries[codigoParaEditarSerie][2] = temporadas
                cuantosGenerosTiene = preguntarNumeroNormal(f"Cuantos generos tiene nuevamente {nombre}?", 0)
                listaGeneros = []
                for i in range(cuantosGenerosTiene):
                    generos = input(f"───> Digita nuevamente el genero #{i+1} de {nombre}: ")
                    listaGeneros.append(generos)
                listaGeneros.sort()
                contenidoSeries[codigoParaEditarSerie][3] = listaGeneros
                año = preguntarNumeroNormal(f"En que año se estreno nuevamente {nombre}?", 0)
                contenidoSeries[codigoParaEditarSerie][4] = año
            guardarArchivoSeries(contenidoSeries, codigosSeries)
            print("")
    
    def borrarSerie(contenidoSeries, codigosSeries):
        mostrarSeries(contenidoSeries, codigosSeries)
        while True:
            print("Si no deseas borrar ninguna serie digita -1\n")
            codigoParaBorrarSerie = preguntarNumeroNormal("Digita el codigo de la serie que deseas borrar", 2)
            if codigoParaBorrarSerie != -1 and codigoParaBorrarSerie >= 0:
                if codigoParaBorrarSerie in codigosSeries:
                    print("")
                    break
                else:
                    print("\nEl codigo no se encuentra en nuestra base de datos\n")
            elif codigoParaBorrarSerie == -1:
                print("")
                return
            else:
                print("\nLos codigos empiezan en 0\n")
        posicionParaCambiarCodigos = None
        for i in range(len(contenidoSeries.copy())):
            if codigoParaBorrarSerie == contenidoSeries[i][5]:
                contenidoSeries.pop(i)
                codigosSeries.pop(i)
                posicionParaCambiarCodigos = i
                print(f"La serie con codigo {codigoParaBorrarSerie} se ha borrado con exito!\n")
                break
        while posicionParaCambiarCodigos <= len(codigosSeries)-1:
            codigosSeries[posicionParaCambiarCodigos] -= 1
            posicionParaCambiarCodigos += 1
    
    while True:
        menuSeries()
        opcionMenuSeries = preguntarNumero(0, 6, "[0,1,2,3,4,5,6]")
        os.system('cls')
        if opcionMenuSeries == 0: #Volver
            return
        if opcionMenuSeries == 1: #Agregar
            agregarSerie(contenidoSeries, codigosSeries)
        if opcionMenuSeries == 2: #Editar
            editarSerie(contenidoSeries, codigosSeries)
        if opcionMenuSeries == 3: #Buscar x nombre
            buscarSerieXNombre(contenidoSeries, codigosSeries)
        if opcionMenuSeries == 4: #Buscar x genero
            buscarSerieXGenero(contenidoSeries, codigosSeries)
        if opcionMenuSeries == 5: #Borrar
            borrarSerie(contenidoSeries, codigosSeries)
        if opcionMenuSeries == 6: #Mostrar
            if len(contenidoSeries) == 0:
                print("No has colocado ninguna serie\n")
            else:
                mostrarSeries(contenidoSeries, codigosSeries)
        contenidoSeries.sort()
        for i in range(len(contenidoSeries)):
            contenidoSeries[i][5] = codigosSeries[i]
        guardarArchivoSeries(contenidoSeries, codigosSeries)