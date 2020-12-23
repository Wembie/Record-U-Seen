from Packages.Menus import *
from Packages.Funciones import *

import time
import os
import os.path as path

def animes(contenidoAnimes, codigosAnimes):
    def agregarAnime(contenidoAnimes, codigosAnimes):
        cuantosAnimesParaAgregar = preguntarNumeroNormal("Cuantos animes deseas agregar?", 0)
        for i in range(cuantosAnimesParaAgregar):
            listaAnime = []
            while True:
                nombre = input(f"\n───> Digita el nombre del anime #{i+1}: ")
                encontroNombreAnime = 0
                for j in range(len(contenidoAnimes)):
                    if nombre == contenidoAnimes[j][0]:
                        encontroNombreAnime = 1
                        break
                if encontroNombreAnime == 1:
                    print(f"\nYa has agregado el anime con nombre {nombre}")
                else:
                    break   
            capitulos = preguntarNumeroNormal(f"Cuantos capitulos tiene {nombre}?", 0)
            calificacion = preguntarNumeroNormal(f"Digita la calificacion de {nombre}", 1)
            while True:
                estado =  input(f"───> Digita el estado de {nombre} [Emision = 1 / Finalizado = 0]: ")
                if estado == "1":
                    estado = "Emision"
                    break
                elif estado == "0":
                    estado = "Finalizado"
                    break
                else:
                    print("\nNumero invalido")
                    print("Por favor digitelo nuevamente\n")
            cuantosGenerosTiene = preguntarNumeroNormal(f"Cuantos generos tiene {nombre}?", 0)
            listaGeneros = []
            for j in range(cuantosGenerosTiene):
                generos = input(f"───> Digita el genero #{j+1} de {nombre}: ")
                listaGeneros.append(generos)
            listaGeneros.sort()
            año = preguntarNumeroNormal(f"En que año se estreno {nombre}?", 0)
            if len(codigosAnimes) == 0:
                codigo = 0
            else:
                codigo = codigosAnimes[len(codigosAnimes)-1] + 1
            codigosAnimes.append(codigo)
            listaAnime.append(nombre) #0
            listaAnime.append(capitulos) #1
            listaAnime.append(calificacion) #2
            listaAnime.append(estado) #3
            listaAnime.append(listaGeneros) #4
            listaAnime.append(año) #5
            listaAnime.append(codigo) #6
            contenidoAnimes.append(listaAnime)
            print(f"\nEl anime con nombre {nombre} ha sido agregado con exito!")
        print("")
            
    def buscarAnimeXNombre(contenidoAnimes, codigosAnimes):
        encontroAnime = 0
        nombreParaBuscar = input("───> Digite el nombre a buscar: ")
        print(f"\nAnimes con la palabra {nombreParaBuscar}:\n")
        for i in range(len(contenidoAnimes)):
            if contenidoAnimes[i][0].find(nombreParaBuscar) != -1:
                print(f"""Nombre: {contenidoAnimes[i][0]}
 Capitulos: {contenidoAnimes[i][1]}
 Calificacion: {contenidoAnimes[i][2]}
 Estado: {contenidoAnimes[i][3]}""")
                print(" Generos: ", end = '')
                for j in range(len(contenidoAnimes[i][4])):
                    if len(contenidoAnimes[i][4])-1 == j:
                        print(f"{contenidoAnimes[i][4][j]}", end = '')
                    else:
                        print(f"{contenidoAnimes[i][4][j]} / ", end = '')
                print(f"\n Año: {contenidoAnimes[i][5]}")
                print(f" Codigo: {contenidoAnimes[i][6]}\n")
                encontroAnime = 1
        if encontroAnime == 0:
            print(f"No se ha encontrado ningun nombre con '{nombreParaBuscar}'\n")
    def buscarAnimeXGenero(contenidoAnimes, codigosAnimes):
        encontroAnime = 0
        generosDisponibles = []
        for i in range(len(contenidoAnimes)):
            for j in range(len(contenidoAnimes[i][4])):
                if contenidoAnimes[i][4][j] not in generosDisponibles:
                    generosDisponibles.append(contenidoAnimes[i][4][j])
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
        print(f"\nAnimes con generos: ", end = '')
        for i in range(len(generosParaBuscar)):
            if len(generosParaBuscar)-1 == i:
                print(f"{generosParaBuscar[i]}", end = '')
            else:
                print(f"{generosParaBuscar[i]}, ", end = '')
        print("\n")
        for i in range(len(contenidoAnimes)):
            contenidoGenerosAnimes = []
            for w in range(len(generosParaBuscar)):
                if generosParaBuscar[w] in contenidoAnimes[i][4]:
                    contenidoGenerosAnimes.append(generosParaBuscar[w])
            if generosParaBuscar == contenidoGenerosAnimes:
                print(f"""Nombre: {contenidoAnimes[i][0]}
 Capitulos: {contenidoAnimes[i][1]}
 Calificacion: {contenidoAnimes[i][2]}
 Estado: {contenidoAnimes[i][3]}""")
                print(" Generos: ", end = '')
                for j in range(len(contenidoAnimes[i][4])):
                    if len(contenidoAnimes[i][4])-1 == j:
                        print(f"{contenidoAnimes[i][4][j]}", end = '')
                    else:
                        print(f"{contenidoAnimes[i][4][j]} / ", end = '')
                print(f"\n Año: {contenidoAnimes[i][5]}")
                print(f" Codigo: {contenidoAnimes[i][6]}\n")
                encontroAnime = 1
        if encontroAnime == 0:
            print(f"No se ha encontrado ningun genero de los que digistaste\n")
    
    def mostrarAnimes(contenidoAnimes, codigosAnimes):
        print("Animes que has visto:\n")
        for i in range(len(contenidoAnimes)):
            print(f"""Nombre: {contenidoAnimes[i][0]}
 Capitulos: {contenidoAnimes[i][1]}
 Calificacion: {contenidoAnimes[i][2]}
 Estado: {contenidoAnimes[i][3]}""")
            print(" Generos: ", end = '')
            for j in range(len(contenidoAnimes[i][4])):
                if len(contenidoAnimes[i][4])-1 == j:
                    print(f"{contenidoAnimes[i][4][j]}", end = '')
                else:
                    print(f"{contenidoAnimes[i][4][j]} / ", end = '')
            print(f"\n Año: {contenidoAnimes[i][5]}")
            print(f" Codigo: {contenidoAnimes[i][6]}\n")

    def editarAnime(contenidoAnimes, codigosAnimes):
        mostrarAnimes(contenidoAnimes, codigosAnimes)
        while True:
            print("Si no deseas editar ningun anime digita -1\n")
            codigoParaEditarAnime = preguntarNumeroNormal("Digita el codigo del anime que deseas editar", 2)
            if codigoParaEditarAnime != -1 and codigoParaEditarAnime >= 0:
                if codigoParaEditarAnime in codigosAnimes:
                    print("")
                    break
                else:
                    print("\nEl codigo no se encuentra en nuestra base de datos\n")
            elif codigoParaEditarAnime == -1:
                print("")
                return
            else:
                print("\nLos codigos empiezan en 0\n")
        while True:
            os.system('cls')
            print(f"""Nombre: {contenidoAnimes[codigoParaEditarAnime][0]}
 Capitulos: {contenidoAnimes[codigoParaEditarAnime][1]}
 Calificacion: {contenidoAnimes[codigoParaEditarAnime][2]}
 Estado: {contenidoAnimes[codigoParaEditarAnime][3]}""")
            print(" Generos: ", end = '')
            for j in range(len(contenidoAnimes[codigoParaEditarAnime][4])):
                if len(contenidoAnimes[codigoParaEditarAnime][4])-1 == j:
                    print(f"{contenidoAnimes[codigoParaEditarAnime][4][j]}", end = '')
                else:
                    print(f"{contenidoAnimes[codigoParaEditarAnime][4][j]} / ", end = '')
            print(f"\n Año: {contenidoAnimes[codigoParaEditarAnime][5]}")
            print(f" Codigo: {contenidoAnimes[codigoParaEditarAnime][6]}\n")
            menuEditarAnime()
            opcionMenuEditarAnime = preguntarNumero(0, 7, "[0,1,2,3,4,5,6,7]")
            if opcionMenuEditarAnime == 0: #Volver
                os.system('cls')
                return
            if opcionMenuEditarAnime == 1: #Nombre
                os.system('cls')
                nombre = input(f"───> Digita nuevamente el nombre del anime: ")
                contenidoAnimes[codigoParaEditarAnime][0] = nombre
            if opcionMenuEditarAnime == 2: #Capitulos
                os.system('cls')
                capitulos = preguntarNumeroNormal(f"Cuantos capitulos tiene nuevamente {contenidoAnimes[codigoParaEditarAnime][0]}?", 0)
                contenidoAnimes[codigoParaEditarAnime][1] = capitulos
            if opcionMenuEditarAnime == 3: #Calificacion
                os.system('cls')
                calificacion = preguntarNumeroNormal(f"Digita nuevamente la calificacion de {contenidoAnimes[codigoParaEditarAnime][0]}", 1)
                contenidoAnimes[codigoParaEditarAnime][2] = calificacion
            if opcionMenuEditarAnime == 4: #Estado
                os.system('cls')
                while True:
                    estado =  input(f"───> Digita nuevamente el estado de {contenidoAnimes[codigoParaEditarAnime][0]} [Emision = 1 / Finalizado = 0]: ")
                    if estado == "1":
                        estado = "Emision"
                        break
                    elif estado == "0":
                        estado = "Finalizado"
                        break
                    else:
                        print("\nNumero invalido")
                        print("Por favor digitelo nuevamente\n")
                contenidoAnimes[codigoParaEditarAnime][3] = estado
            if opcionMenuEditarAnime == 5: #Generos
                os.system('cls')
                cuantosGenerosTiene = preguntarNumeroNormal(f"Cuantos generos tiene nuevamente {contenidoAnimes[codigoParaEditarAnime][0]}?", 0)
                listaGeneros = []
                for i in range(cuantosGenerosTiene):
                    generos = input(f"───> Digita nuevamente el genero #{i+1} de {contenidoAnimes[codigoParaEditarAnime][0]}: ")
                    listaGeneros.append(generos)
                listaGeneros.sort()
                contenidoAnimes[codigoParaEditarAnime][4] = listaGeneros
            if opcionMenuEditarAnime == 6: #Año
                os.system('cls')
                año = preguntarNumeroNormal(f"En que año se estreno nuevamente {contenidoAnimes[codigoParaEditarAnime][0]}?", 0)
                contenidoAnimes[codigoParaEditarAnime][5] = año
            if opcionMenuEditarAnime == 7: #Todo
                os.system('cls')
                nombre = input(f"───> Digita nuevamente el nombre del anime: ")
                contenidoAnimes[codigoParaEditarAnime][0] = nombre
                capitulos = preguntarNumeroNormal(f"Cuantos capitulos tiene nuevamente {nombre}?", 0)
                contenidoAnimes[codigoParaEditarAnime][1] = capitulos
                calificacion = preguntarNumeroNormal(f"Digita nuevamente la calificacion de {nombre}", 1)
                contenidoAnimes[codigoParaEditarAnime][2] = calificacion
                while True:
                    estado =  input(f"───> Digita nuevamente el estado de {nombre} [Emision = 1 / Finalizado = 0]: ")
                    if estado == "1":
                        estado = "Emision"
                        break
                    elif estado == "0":
                        estado = "Finalizado"
                        break
                    else:
                        print("\nNumero invalido")
                        print("Por favor digitelo nuevamente\n")
                contenidoAnimes[codigoParaEditarAnime][3] = estado
                cuantosGenerosTiene = preguntarNumeroNormal(f"Cuantos generos tiene nuevamente {nombre}?", 0)
                listaGeneros = []
                for i in range(cuantosGenerosTiene):
                    generos = input(f"───> Digita nuevamente el genero #{i+1} de {nombre}: ")
                    listaGeneros.append(generos)
                contenidoAnimes[codigoParaEditarAnime][4] = listaGeneros
                año = preguntarNumeroNormal(f"En que año se estreno nuevamente {nombre}?", 0)
                contenidoAnimes[codigoParaEditarAnime][5] = año
            guardarArchivoAnimes(contenidoAnimes, codigosAnimes)
            print("")

    def borrarAnime(contenidoAnimes, codigosAnimes):
        mostrarAnimes(contenidoAnimes, codigosAnimes)
        while True:
            print("Si no deseas borrar ningun anime digita -1\n")
            codigoParaBorrarAnime = preguntarNumeroNormal("Digita el codigo del anime que deseas borrar", 2)
            if codigoParaBorrarAnime != -1 and codigoParaBorrarAnime >= 0:
                if codigoParaBorrarAnime in codigosAnimes:
                    print("")
                    break
                else:
                    print("\nEl codigo no se encuentra en nuestra base de datos\n")
            elif codigoParaBorrarAnime == -1:
                print("")
                return
            else:
                print("\nLos codigos empiezan en 0\n")
        posicionParaCambiarCodigos = None
        for i in range(len(contenidoAnimes.copy())):
            if codigoParaBorrarAnime == contenidoAnimes[i][6]:
                contenidoAnimes.pop(i)
                codigosAnimes.pop(i)
                posicionParaCambiarCodigos = i
                print(f"El anime con codigo {codigoParaBorrarAnime} se ha borrado con exito!\n")
                break
        while posicionParaCambiarCodigos <= len(codigosAnimes)-1:
            codigosAnimes[posicionParaCambiarCodigos] -= 1
            posicionParaCambiarCodigos += 1
    
    while True:
        menuAnimes()
        opcionMenuAnimes = preguntarNumero(0, 6, "[0,1,2,3,4,5,6]")
        if opcionMenuAnimes == 0: #Volver
            os.system('cls')
            return
        if opcionMenuAnimes == 1: #Agregar
            os.system('cls')
            agregarAnime(contenidoAnimes, codigosAnimes)
        if opcionMenuAnimes == 2: #Editar
            os.system('cls')
            editarAnime(contenidoAnimes, codigosAnimes)
        if opcionMenuAnimes == 3: #Buscar x nombre
            os.system('cls')
            buscarAnimeXNombre(contenidoAnimes, codigosAnimes)
        if opcionMenuAnimes == 4: #Buscar x genero
            os.system('cls')
            buscarAnimeXGenero(contenidoAnimes, codigosAnimes)
        if opcionMenuAnimes == 5: #Borrar
            os.system('cls')
            borrarAnime(contenidoAnimes, codigosAnimes)         
        if opcionMenuAnimes == 6: #Mostrar
            os.system('cls')
            if len(contenidoAnimes) == 0:
                print("No has colocado ningun anime\n")
            else:
                mostrarAnimes(contenidoAnimes, codigosAnimes)
        contenidoAnimes.sort()
        for i in range(len(contenidoAnimes)):
            contenidoAnimes[i][6] = codigosAnimes[i]
        guardarArchivoAnimes(contenidoAnimes, codigosAnimes)

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
            if opcionMenuEditarSerie == 0: #Volver
                os.system('cls')
                return
            if opcionMenuEditarSerie == 1: #Nombre
                os.system('cls')
                nombre = input(f"───> Digita nuevamente el nombre de la serie: ")
                contenidoSeries[codigoParaEditarSerie][0] = nombre
            if opcionMenuEditarSerie == 2: #Calificacion
                os.system('cls')
                calificacion = preguntarNumeroNormal(f"Digita nuevamente la calificacion de {contenidoSeries[codigoParaEditarSerie][0]}", 1)
                contenidoSeries[codigoParaEditarSerie][1] = calificacion
            if opcionMenuEditarSerie == 3: #Temporadas
                os.system('cls')
                temporadas = preguntarNumeroNormal(f"Cuantas temporadas tiene nuevamente {contenidoSeries[codigoParaEditarSerie][0]}?", 0)
                contenidoSeries[codigoParaEditarSerie][2] = temporadas
            if opcionMenuEditarSerie == 4: #Generos
                os.system('cls')
                cuantosGenerosTiene = preguntarNumeroNormal(f"Cuantos generos tiene nuevamente {contenidoSeries[codigoParaEditarSerie][0]}?", 0)
                listaGeneros = []
                for i in range(cuantosGenerosTiene):
                    generos = input(f"───> Digita nuevamente el genero #{i+1} de {contenidoSeries[codigoParaEditarSerie][0]}: ")
                    listaGeneros.append(generos)
                listaGeneros.sort()
                contenidoSeries[codigoParaEditarSerie][3] = listaGeneros
            if opcionMenuEditarSerie == 5: #Año
                os.system('cls')
                año = preguntarNumeroNormal(f"En que año se estreno nuevamente {contenidoSeries[codigoParaEditarSerie][0]}?", 0)
                contenidoSeries[codigoParaEditarSerie][4] = año
            if opcionMenuEditarSerie == 6: #Todo
                os.system('cls')
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
        if opcionMenuSeries == 0: #Volver
            os.system('cls')
            return
        if opcionMenuSeries == 1: #Agregar
            os.system('cls')
            agregarSerie(contenidoSeries, codigosSeries)
        if opcionMenuSeries == 2: #Editar
            os.system('cls')
            editarSerie(contenidoSeries, codigosSeries)
        if opcionMenuSeries == 3: #Buscar x nombre
            os.system('cls')
            buscarSerieXNombre(contenidoSeries, codigosSeries)
        if opcionMenuSeries == 4: #Buscar x genero
            os.system('cls')
            buscarSerieXGenero(contenidoSeries, codigosSeries)
        if opcionMenuSeries == 5: #Borrar
            os.system('cls')
            borrarSerie(contenidoSeries, codigosSeries)
        if opcionMenuSeries == 6: #Mostrar
            os.system('cls')
            if len(contenidoSeries) == 0:
                print("No has colocado ninguna serie\n")
            else:
                mostrarSeries(contenidoSeries, codigosSeries)
        contenidoSeries.sort()
        for i in range(len(contenidoSeries)):
            contenidoSeries[i][5] = codigosSeries[i]
        guardarArchivoSeries(contenidoSeries, codigosSeries)

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
            if opcionMenuEditarPelicula == 0: #Volver
                os.system('cls')
                return
            if opcionMenuEditarPelicula == 1: #Nombre
                os.system('cls')
                nombre = input(f"───> Digita nuevamente el nombre de la pelicula: ")
                contenidoPeliculas[codigoParaEditarPelicula][0] = nombre
            if opcionMenuEditarPelicula == 2: #Calificacion
                os.system('cls')
                calificacion = preguntarNumeroNormal(f"Digita nuevamente la calificacion de {contenidoPeliculas[codigoParaEditarPelicula][0]}", 1)
                contenidoPeliculas[codigoParaEditarPelicula][1] = calificacion
            if opcionMenuEditarPelicula == 3: #Duracion
                os.system('cls')
                duracion = preguntarNumeroNormal(f"Cuanto es la duracion nuevamente de {contenidoPeliculas[codigoParaEditarPelicula][0]} en minutos?", 0)
                contenidoPeliculas[codigoParaEditarPelicula][2] = duracion
            if opcionMenuEditarPelicula == 4: #Generos
                os.system('cls')
                cuantosGenerosTiene = preguntarNumeroNormal(f"Cuantos generos tiene nuevamente {contenidoPeliculas[codigoParaEditarPelicula][0]}?", 0)
                listaGeneros = []
                for i in range(cuantosGenerosTiene):
                    generos = input(f"───> Digita nuevamente el genero #{i+1} de {contenidoPeliculas[codigoParaEditarPelicula][0]}: ")
                    listaGeneros.append(generos)
                listaGeneros.sort()
                contenidoPeliculas[codigoParaEditarPelicula][3] = listaGeneros
            if opcionMenuEditarPelicula == 5: #Año
                os.system('cls')
                año = preguntarNumeroNormal(f"En que año se estreno nuevamente {contenidoPeliculas[codigoParaEditarPelicula][0]}?", 0)
                contenidoPeliculas[codigoParaEditarPelicula][4] = año
            if opcionMenuEditarPelicula == 6: #Todo
                os.system('cls')
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
        if opcionMenuPeliculas == 0: #Volver
            os.system('cls')
            return
        if opcionMenuPeliculas == 1: #Agregar
            os.system('cls')
            agregarPelicula(contenidoPeliculas, codigosPeliculas)
        if opcionMenuPeliculas == 2: #Editar
            os.system('cls')
            editarPelicula(contenidoPeliculas, codigosPeliculas)
        if opcionMenuPeliculas == 3: #Buscar x nombre
            os.system('cls')
            buscarPeliculaXNombre(contenidoPeliculas, codigosPeliculas)
        if opcionMenuPeliculas == 4: #Buscar x genero
            os.system('cls')
            buscarPeliculaXGenero(contenidoPeliculas, codigosPeliculas)
        if opcionMenuPeliculas == 5: #Borrar
            os.system('cls')
            borrarPelicula(contenidoPeliculas, codigosPeliculas)
        if opcionMenuPeliculas == 6: #Mostrar
            os.system('cls')
            if len(contenidoPeliculas) == 0:
                print("No has colocado ninguna pelicula\n")
            else:
                mostrarPeliculas(contenidoPeliculas, codigosPeliculas)
        contenidoPeliculas.sort()
        for i in range(len(contenidoPeliculas)):
            contenidoPeliculas[i][5] = codigosPeliculas[i]
        guardarArchivoPeliculas(contenidoPeliculas, codigosPeliculas)
        
def main():
    os.system('TITLE Record U Seen')
    contenidoAnimes = []
    codigosAnimes = []
    contenidoSeries = []
    codigosSeries = []
    contenidoPeliculas = []
    codigosPeliculas = []
    if path.exists("Contenido"):
        #Animes
        archivo = open(f"Contenido/animes","br")
        contenidoAnimes = marshal.load(archivo)
        archivo.close()
        ###
        archivo = open(f"Contenido/codigosAnimes","br")
        codigosAnimes = marshal.load(archivo)
        archivo.close()
        #Series
        archivo = open(f"Contenido/series","br")
        contenidoSeries = marshal.load(archivo)
        archivo.close()
        ###
        archivo = open(f"Contenido/codigosSeries","br")
        codigosSeries = marshal.load(archivo)
        archivo.close()
        #Peliculas
        archivo = open(f"Contenido/peliculas","br")
        contenidoPeliculas = marshal.load(archivo)
        archivo.close()
        ###
        archivo = open(f"Contenido/codigosPeliculas","br")
        codigosPeliculas = marshal.load(archivo)
        archivo.close()    
    else:
        os.mkdir("Contenido")
        guardarArchivoAnimes(contenidoAnimes, codigosAnimes)
        guardarArchivoSeries(contenidoSeries, codigosSeries)
        guardarArchivoPeliculas(contenidoPeliculas, codigosPeliculas)
    while True:
        menuPrincipal()
        opcionMenuPrincipal = preguntarNumero(0, 3, "[0,1,2,3]")
        if opcionMenuPrincipal == 0: #Salir
            print("Gracias por usar la aplicacion RECORD U SEEN vuelve pronto :D")
            time.sleep(2)
            return
        elif opcionMenuPrincipal == 1: #Animes
            os.system('cls')
            animes(contenidoAnimes, codigosAnimes)
        elif opcionMenuPrincipal == 2: #Series
            os.system('cls')
            series(contenidoSeries, codigosSeries)
        elif opcionMenuPrincipal == 3: #Peliculas
            os.system('cls')
            peliculas(contenidoPeliculas, codigosPeliculas)
        
main()
