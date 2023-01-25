from Packages.Menus import *
from Packages.Funciones import *

import time
import os
import os.path as path

def animes( contenidoAnimes, codigosAnimes ):
    def agregarAnime( contenidoAnimes, codigosAnimes ): #AGREGAR ANIME
        cuantosAnimesParaAgregar = preguntarNumeroNormal( "Cuantos animes deseas agregar?", 0 )
        for i in range( cuantosAnimesParaAgregar ):
            listaAnime = []
            while True:
                nombre = input( f"\n───> Digita el nombre del anime #{ i + 1 }: " )
                encontroNombreAnime = 0
                for j in range( len( contenidoAnimes ) ):
                    if nombre == contenidoAnimes[ j ][ 0 ]:
                        encontroNombreAnime = 1
                        break
                if encontroNombreAnime == 1:
                    print( f"\nYa has agregado el anime con nombre { nombre }" )
                else:
                    break
            print( f"\nSi { nombre } no tiene nombre alternativo coloca 'No'\n" )
            nombresAlternativos = input( f"───> Digita los nombres alternativos separados por ',' de { nombre }: " )
            if nombresAlternativos.lower() == "no":
                nombresAlternativos = "N\A"
            capitulos = preguntarNumeroNormal( f"Cuantos capitulos tiene { nombre }?", 0 )
            while True:
                capitulosVistos = preguntarNumeroNormal( f"Cuantos capitulos has visto de { capitulos } cuyo nombre es { nombre }?", 2 )
                if capitulosVistos >= 0:
                    if capitulosVistos <= capitulos:
                        break
                    else:
                        print( f"\nLos capitulos vistos no pueden sobrepasar { capitulos } capitulos" )
                else:
                    print( f"\nLos capitulos vistos no pueden ser menor a 0" )
            while True:
                calificacion = preguntarNumeroNormal( f"Digita la calificacion de { nombre }", 1 )
                if calificacion <= 10:
                    break
                else:
                    print( "\nLa calificacion debe ser mayor a 0 y menor a 10\n" )
            while True:
                estado = input( f"───> Digita el estado de { nombre } [Emision = 1 / Finalizado = 0]: " )
                if estado == "1":
                    estado = "Emision"
                    break
                elif estado == "0":
                    estado = "Finalizado"
                    break
                else:
                    print( "\nNumero invalido")
                    print( "Por favor digitelo nuevamente\n" )
            cuantosGenerosTiene = preguntarNumeroNormal( f"Cuantos generos tiene { nombre }?", 0 )
            listaGeneros = []
            for j in range( cuantosGenerosTiene ):
                generos = input( f"───> Digita el genero #{ j + 1 } de { nombre }: " )
                listaGeneros.append( generos )
            listaGeneros.sort()
            año = preguntarNumeroNormal( f"En que año se estreno { nombre }?", 0 )
            #estudio = input( f"───> Digita el nombre del estudio de animacion de { nombre }" )
            if len( codigosAnimes ) == 0:
                codigo = 0
            else:
                codigo = codigosAnimes[ len( codigosAnimes ) - 1 ] + 1
            codigosAnimes.append( codigo )
            listaAnime.append( nombre ) #0
            listaAnime.append( capitulos ) #1
            listaAnime.append( calificacion ) #2
            listaAnime.append( estado ) #3
            listaAnime.append( listaGeneros ) #4
            listaAnime.append( año ) #5
            listaAnime.append( codigo ) #6
            listaAnime.append( capitulosVistos ) #7
            listaAnime.append( nombresAlternativos ) #8
            #listaAnime.append( estudio ) #9
            contenidoAnimes.append( listaAnime )
            print( f"\nEl anime con nombre { nombre } ha sido agregado con exito!" )
        print( "" )
            
    def buscarAnimeXNombre( contenidoAnimes, codigosAnimes ): #BUSCAR ANIME POR NOMBRE
        encontroAnime = 0
        nombreParaBuscar = input( "───> Digite el nombre a buscar: " )
        print( f"\nAnimes con la palabra { nombreParaBuscar }:\n" )
        for i in range( len( contenidoAnimes ) ):
            if contenidoAnimes[ i ][ 0 ].lower().find( nombreParaBuscar.lower() ) != -1 or contenidoAnimes[ i ][ 8 ].lower().find( nombreParaBuscar.lower() ) != -1 :
                print( f"""Nombre: { contenidoAnimes[ i ][ 0 ] }
 Nombre Alternativo: { contenidoAnimes[ i ][ 8 ]}
 Capitulos: { contenidoAnimes[ i ][ 7 ] } / { contenidoAnimes[ i ][ 1 ] }
 Calificacion: { contenidoAnimes[ i ][ 2 ] }
 Estado: { contenidoAnimes[ i ][ 3 ] }""" )
                print( " Generos: ", end = '' )
                for j in range( len( contenidoAnimes[ i ][ 4 ] ) ):
                    if len( contenidoAnimes[ i ][ 4 ] ) - 1 == j:
                        print( f"{ contenidoAnimes[ i ][ 4 ][ j ] }", end = '' )
                    else:
                        print( f"{ contenidoAnimes[ i ][ 4 ][ j ] } / ", end = '' )
                print( f"\n Año: { contenidoAnimes[ i ][ 5 ] }" )
                print( f" Codigo: { contenidoAnimes[ i ][ 6 ] }\n" )
                encontroAnime = 1
        if encontroAnime == 0:
            print( f"No se ha encontrado ningun nombre con '{ nombreParaBuscar }'\n" )

    def buscarAnimeXGenero(contenidoAnimes, codigosAnimes): #BUSCAR ANIME POR GENERO
        menuBuscarGeneroAnime()
        opcionMenuGenero = preguntarNumero(0, 2, "")
        if opcionMenuGenero == 1 or opcionMenuGenero == 2:
            encontroAnime = 0
            generosDisponibles = []
            cuantoGenerosParaBuscar = preguntarNumeroNormal(f"Cuantos generos deseas buscar?", 0)
            os.system('cls')
            for i in range(len(contenidoAnimes)):
                for j in range(len(contenidoAnimes[i][4])):
                    if contenidoAnimes[i][4][j] not in generosDisponibles:
                        generosDisponibles.append(contenidoAnimes[i][4][j])
            generosDisponibles.sort()
            print("Generos Encontrados: \n")
            if opcionMenuGenero == 1: #Automatico
                for i in range(len(generosDisponibles)):
                    print(f"{i}. {generosDisponibles[i]}") 
                print(f"{len(generosDisponibles)}. Volver")
                generosParaBuscar = []
                for i in range(cuantoGenerosParaBuscar):
                    while True:
                        opcionSeleccionGeneros = preguntarNumero(0, len(generosDisponibles), "")
                        if opcionSeleccionGeneros == len(generosDisponibles):
                            os.system('cls')
                            return
                        else:
                            genero = generosDisponibles[opcionSeleccionGeneros]
                            if genero in generosDisponibles:
                                if genero in generosParaBuscar:
                                    print("No puedes colocar un genero igual al que escogiste anteriormente")
                                else:
                                    generosParaBuscar.append(genero)
                                    print(f"Genero {genero} con codigo {opcionSeleccionGeneros}, agregado exitosamente")
                                    break
                            else:
                                print(f"\nNo se ha encontrado ningun genero con el nombre de {genero}\n")
            elif opcionMenuGenero == 2: #Manual
                for i in range(len(generosDisponibles)):
                    if len(generosDisponibles)-1 == i:
                        print(f"{generosDisponibles[i]}", end = '')
                    else:
                        print(f"{generosDisponibles[i]}, ", end = '')
                print("\n")
                generosParaBuscar = []
                for i in range(cuantoGenerosParaBuscar):
                    while True:
                        generoParaBuscar = input(f"───> Digite el genero #{i+1} a buscar: ")
                        if generoParaBuscar in generosDisponibles:
                            if generoParaBuscar in generosParaBuscar:
                                print("No puedes colocar un genero igual al que escogiste anteriormente")
                            else:
                                generosParaBuscar.append(generoParaBuscar)
                                break
                        else:
                            print(f"\nNo se ha encontrado ningun genero con el nombre de {generoParaBuscar}\n")
            os.system('cls')
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
 Nombre Alternativo: { contenidoAnimes[ i ][ 8 ]}
 Capitulos: {contenidoAnimes[i][7]} / {contenidoAnimes[i][1]}
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
        elif opcionMenuGenero == 0:
            os.system('cls')
            return
            
    def buscarAnimeXCalificacion(contenidoAnimes, codigosAnimes): #BUSCAR ANIME POR CALIFICACION
        encontroAnime = 0
        calificacionParaBuscar = preguntarNumeroNormal("Digita la calificacion a buscar", 3)
        print(f"\nAnimes con calificacion {calificacionParaBuscar} o superior:\n")
        for i in range(len(contenidoAnimes)):
            if contenidoAnimes[i][2] >= calificacionParaBuscar:
                print(f"""Nombre: {contenidoAnimes[i][0]}
 Nombre Alternativo: { contenidoAnimes[ i ][ 8 ]}
 Capitulos: {contenidoAnimes[i][7]} / {contenidoAnimes[i][1]}
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
            print(f"No se ha encontrado ningun anime con la calificacion que digistaste\n")

    def buscarAnimeXEstado(contenidoAnimes, codigosAnimes): #BUSCAR ANIME POR ESTADO
        encontroAnime = 0
        while True:
            estado =  input(f"───> Digita el estado a buscar [Emision = 1 / Finalizado = 0]: ")
            if estado == "1":
                estado = "Emision"
                break
            elif estado == "0":
                estado = "Finalizado"
                break
            else:
                print("\nNumero invalido")
                print("Por favor digitelo nuevamente\n")
        print(f"\nAnimes con estado {estado}:\n")
        for i in range(len(contenidoAnimes)):
            if estado == contenidoAnimes[i][3]:
                print(f"""Nombre: {contenidoAnimes[i][0]}
 Nombre Alternativo: { contenidoAnimes[ i ][ 8 ]}
 Capitulos: {contenidoAnimes[i][7]} / {contenidoAnimes[i][1]}
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
            print(f"No se ha encontrado ningun anime con el estado que digistaste\n")

    def buscarAnimeXAño(contenidoAnimes, codigosAnimes): #BUSCAR ANIME POR AÑO
        encontroAnime = 0
        año = preguntarNumeroNormal(f"Digita el año a buscar?", 0)
        print(f"\nAnimes con año {año}:\n")
        for i in range(len(contenidoAnimes)):
            if año == contenidoAnimes[i][5]:
                print(f"""Nombre: {contenidoAnimes[i][0]}
 Nombre Alternativo: { contenidoAnimes[ i ][ 8 ]}
 Capitulos: {contenidoAnimes[i][7]} / {contenidoAnimes[i][1]}
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
            print(f"No se ha encontrado ningun anime con el año que digistaste\n")

    def buscarAnimeXCapitulos(contenidoAnimes, codigosAnimes): #BUSCAR ANIME POR CAPITULOS
        encontroAnime = 0
        capitulos = preguntarNumeroNormal(f"Digita la cantidad de capitulos a buscar?", 0)
        if capitulos == 1:
            print(f"\nAnimes con {capitulos} capitulo:\n")
        else:
            print(f"\nAnimes con {capitulos} capitulos:\n")
        for i in range(len(contenidoAnimes)):
            if capitulos == contenidoAnimes[i][1]:
                print(f"""Nombre: {contenidoAnimes[i][0]}
 Nombre Alternativo: { contenidoAnimes[ i ][ 8 ]}
 Capitulos: {contenidoAnimes[i][7]} / {contenidoAnimes[i][1]}
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
            print(f"No se ha encontrado ningun anime con los capitulos que digistaste\n")

    def buscarAnimeXTerminado(contenidoAnimes, codigosAnimes): #BUSCAR ANIMES TERMINADOS
        print(f"Animes Terminados:\n")
        encontroAnime = 0
        for i in range(len(contenidoAnimes)):
            if contenidoAnimes[i][7] == contenidoAnimes[i][1]:
                print(f"""Nombre: {contenidoAnimes[i][0]}
 Nombre Alternativo: { contenidoAnimes[ i ][ 8 ]}
 Capitulos: {contenidoAnimes[i][7]} / {contenidoAnimes[i][1]}
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
            print(f"No se ha encontrado ningun anime terminado\n")

    def buscarAnimeXFaltantes(contenidoAnimes, codigosAnimes): #BUSCAR ANIMES FALTANTES
        print(f"Animes Faltantes:\n")
        encontroAnime = 0
        for i in range(len(contenidoAnimes)):
            if contenidoAnimes[i][7] != contenidoAnimes[i][1]:
                print(f"""Nombre: {contenidoAnimes[i][0]}
 Nombre Alternativo: { contenidoAnimes[ i ][ 8 ]}
 Capitulos: {contenidoAnimes[i][7]} / {contenidoAnimes[i][1]}
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
            print(f"No se ha encontrado ningun anime faltante\n")
        
    def mostrarAnimes(contenidoAnimes, codigosAnimes): #MOSTRAR ANIMES
        print("Animes que has visto:\n")
        for i in range(len(contenidoAnimes)):
            print(f"""Nombre: {contenidoAnimes[i][0]}
 Nombre Alternativo: { contenidoAnimes[ i ][ 8 ]}
 Capitulos: {contenidoAnimes[i][7]} / {contenidoAnimes[i][1]}
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

    def editarAnime(contenidoAnimes, codigosAnimes): #EDITAR ANIME
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
 Nombre Alternativo: { contenidoAnimes[ codigoParaEditarAnime ][ 8 ]}
 Capitulos: {contenidoAnimes[codigoParaEditarAnime][7]} / {contenidoAnimes[codigoParaEditarAnime][1]}
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
            opcionMenuEditarAnime = preguntarNumero(0, 9, "[0,1,2,3,4,5,6,7,8,9]")
            os.system('cls')
            print(f"""Nombre: {contenidoAnimes[codigoParaEditarAnime][0]}
 Nombre Alternativo: { contenidoAnimes[ codigoParaEditarAnime ][ 8 ]}
 Capitulos: {contenidoAnimes[codigoParaEditarAnime][7]} / {contenidoAnimes[codigoParaEditarAnime][1]}
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
            if opcionMenuEditarAnime == 0: #Volver
                os.system('cls')
                return
            if opcionMenuEditarAnime == 1: #Nombre
                nombre = input(f"───> Digita nuevamente el nombre del anime: ")
                contenidoAnimes[codigoParaEditarAnime][0] = nombre
            if opcionMenuEditarAnime == 2: #Nombres Alternativos
                print( f"Si { contenidoAnimes[codigoParaEditarAnime][0] } no tiene nombre alternativo coloca 'No'\n" )
                nombresAlternativos = input( f"Digita los nombres alternativos separados por ',' de { contenidoAnimes[codigoParaEditarAnime][0] }: " )
                if nombresAlternativos.lower() == "no":
                    nombresAlternativos = "N\A"
                contenidoAnimes[codigoParaEditarAnime][8] = nombresAlternativos
            if opcionMenuEditarAnime == 3: #Capitulos
                capitulos = preguntarNumeroNormal(f"Cuantos capitulos tiene nuevamente {contenidoAnimes[codigoParaEditarAnime][0]}?", 0)
                contenidoAnimes[codigoParaEditarAnime][1] = capitulos
            if opcionMenuEditarAnime == 4: #Capitulos Vistos
                while True:
                    capitulosVistos = preguntarNumeroNormal(f"Cuantos capitulos has visto de {contenidoAnimes[codigoParaEditarAnime][1]} cuyo nombre es {contenidoAnimes[codigoParaEditarAnime][0]}?", 2)
                    if capitulosVistos >= 0:
                        if capitulosVistos <= contenidoAnimes[codigoParaEditarAnime][1]:
                            break
                        else:
                            print(f"\nLos capitulos vistos no pueden sobrepasar {contenidoAnimes[codigoParaEditarAnime][1]} capitulos\n")
                    else:
                        print(f"\nLos capitulos vistos no pueden ser menor a 0\n")
                contenidoAnimes[codigoParaEditarAnime][7] = capitulosVistos
            if opcionMenuEditarAnime == 5: #Calificacion
                while True:
                    calificacion = preguntarNumeroNormal(f"Digita nuevamente la calificacion de {contenidoAnimes[codigoParaEditarAnime][0]}", 1)
                    if calificacion <= 10:
                        break
                    else:
                        print("\nLa calificacion debe ser mayor a 0 y menor a 10\n")
                contenidoAnimes[codigoParaEditarAnime][2] = calificacion
            if opcionMenuEditarAnime == 6: #Estado
                while True:
                    estado = input(f"───> Digita nuevamente el estado de {contenidoAnimes[codigoParaEditarAnime][0]} [Emision = 1 / Finalizado = 0]: ")
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
            if opcionMenuEditarAnime == 7: #Generos
                cuantosGenerosTiene = preguntarNumeroNormal(f"Cuantos generos tiene nuevamente {contenidoAnimes[codigoParaEditarAnime][0]}?", 0)
                listaGeneros = []
                for i in range(cuantosGenerosTiene):
                    generos = input(f"───> Digita nuevamente el genero #{i+1} de {contenidoAnimes[codigoParaEditarAnime][0]}: ")
                    listaGeneros.append(generos)
                listaGeneros.sort()
                contenidoAnimes[codigoParaEditarAnime][4] = listaGeneros
            if opcionMenuEditarAnime == 8: #Año
                año = preguntarNumeroNormal(f"En que año se estreno nuevamente {contenidoAnimes[codigoParaEditarAnime][0]}?", 0)
                contenidoAnimes[codigoParaEditarAnime][5] = año
            if opcionMenuEditarAnime == 9: #Todo
                nombre = input(f"───> Digita nuevamente el nombre del anime: ")
                contenidoAnimes[codigoParaEditarAnime][0] = nombre
                capitulos = preguntarNumeroNormal(f"Cuantos capitulos tiene nuevamente {nombre}?", 0)
                contenidoAnimes[codigoParaEditarAnime][1] = capitulos
                while True:
                    capitulosVistos = preguntarNumeroNormal(f"Cuantos capitulos has visto de {contenidoAnimes[codigoParaEditarAnime][1]} cuyo nombre es {contenidoAnimes[codigoParaEditarAnime][0]}?", 2)
                    if capitulosVistos >= 0:
                        if capitulosVistos <= contenidoAnimes[codigoParaEditarAnime][1]:
                            break
                        else:
                            print(f"\nLos capitulos vistos no pueden sobrepasar {contenidoAnimes[codigoParaEditarAnime][1]} capitulos\n")
                    else:
                        print(f"\nLos capitulos vistos no pueden ser menor a 0\n")
                contenidoAnimes[codigoParaEditarAnime][7] = capitulosVistos
                calificacion = preguntarNumeroNormal(f"Digita nuevamente la calificacion de {nombre}", 1)
                contenidoAnimes[codigoParaEditarAnime][2] = calificacion
                while True:
                    estado = input(f"───> Digita nuevamente el estado de {nombre} [Emision = 1 / Finalizado = 0]: ")
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

    def borrarAnime(contenidoAnimes, codigosAnimes): #BORRAR ANIME
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
        opcionMenuAnimes = preguntarNumero(0, 5, "[0,1,2,3,4,5]")
        os.system('cls')
        if opcionMenuAnimes == 0: #Volver
            return
        if opcionMenuAnimes == 1: #Agregar
            agregarAnime(contenidoAnimes, codigosAnimes)
        if opcionMenuAnimes == 2: #Editar
            if len(contenidoAnimes) == 0:
                print("No has colocado ningun anime\n")
            else:
                editarAnime(contenidoAnimes, codigosAnimes)
        if opcionMenuAnimes == 3: #Buscar por...
            os.system('cls')
            if len(contenidoAnimes) == 0:
                print("No has colocado ningun anime\n")
            else:
                while True:
                    menuAnimesBuscarPor()
                    opcionMenuAnimesBuscarPor = preguntarNumero(0, 8, "[0,1,2,3,4,5,6,7,8]")
                    os.system('cls')
                    if opcionMenuAnimesBuscarPor == 0:
                        break
                    if opcionMenuAnimesBuscarPor == 1: #Buscar x nombre
                        buscarAnimeXNombre(contenidoAnimes, codigosAnimes)
                    if opcionMenuAnimesBuscarPor == 2: #Buscar x genero
                        buscarAnimeXGenero(contenidoAnimes, codigosAnimes)
                    if opcionMenuAnimesBuscarPor == 3: #Buscar x calificacion
                        buscarAnimeXCalificacion(contenidoAnimes, codigosAnimes)
                    if opcionMenuAnimesBuscarPor == 4: #Buscar x estado
                        buscarAnimeXEstado(contenidoAnimes, codigosAnimes)
                    if opcionMenuAnimesBuscarPor == 5: #Buscar x año 
                        buscarAnimeXAño(contenidoAnimes, codigosAnimes)
                    if opcionMenuAnimesBuscarPor == 6: #Buscar x capitulos
                        buscarAnimeXCapitulos(contenidoAnimes, codigosAnimes)
                    if opcionMenuAnimesBuscarPor == 7: #Buscar Terminados
                        buscarAnimeXTerminado(contenidoAnimes, codigosAnimes)
                    if opcionMenuAnimesBuscarPor == 8: #Buscar Faltantes
                        buscarAnimeXFaltantes(contenidoAnimes, codigosAnimes)
        if opcionMenuAnimes == 4: #Borrar
            if len(contenidoAnimes) == 0:
                print("No has colocado ningun anime\n")
            else:
                borrarAnime(contenidoAnimes, codigosAnimes)         
        if opcionMenuAnimes == 5: #Mostrar
            if len(contenidoAnimes) == 0:
                print("No has colocado ningun anime\n")
            else:
                mostrarAnimes(contenidoAnimes, codigosAnimes)
        contenidoAnimes.sort()
        for i in range(len(contenidoAnimes)):
            contenidoAnimes[i][6] = codigosAnimes[i]
        guardarArchivoAnimes(contenidoAnimes, codigosAnimes)
