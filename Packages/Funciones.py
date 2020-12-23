import marshal

def preguntarNumero(inicio, final, recuadro):
    if recuadro == "":
        while True:
            try:
                opcion = int(input(f"\n───> Digite el numero deseado: "))
            except ValueError:
                print("\nSolo se recibe numeros enteros")
            else:
                if opcion >= inicio and opcion <= final:
                    print("")
                    return opcion
                else:
                    print("\nNumero invalido")
                    print("Por favor digitelo nuevamente")
    else:   
        while True:
            try:
                opcion = int(input(f"\n───> Digite el numero deseado {recuadro}: "))
            except ValueError:
                print("\nSolo se recibe numeros enteros")
            else:
                if opcion >= inicio and opcion <= final:
                    print("")
                    return opcion
                else:
                    print("\nNumero invalido")
                    print("Por favor digitelo nuevamente")

def preguntarNumeroNormal(recuadro, numero):
    if numero == 0:
        while True:
            try:
                opcion = int(input(f"───> {recuadro}: "))
            except ValueError:
                    print("\nSolo se recibe numeros enteros\n")
            else:
                if opcion > 0:
                    return opcion
                else:
                    print("\nEl numero a digitar debe ser mayor a 0\n")
    elif numero == 1:
        while True:
            try:
                opcion = float(input(f"───> {recuadro}: "))
            except ValueError:
                    print("\nSolo se recibe numeros flotantes\n")
            else:
                if opcion > 0:
                    return opcion
                else:
                    print("\nEl numero a digitar debe ser mayor a 0\n")
    elif numero == 2:
        while True:
            try:
                opcion = int(input(f"───> {recuadro}: "))
            except ValueError:
                    print("\nSolo se recibe numeros enteros\n")
            else:
                return opcion

def guardarArchivoAnimes(contenidoAnimes, codigosAnimes):
    archivo = open(f"Contenido/animes","bw")
    marshal.dump(contenidoAnimes,archivo)
    archivo.close()
    ###
    archivo = open(f"Contenido/codigosAnimes","bw")
    marshal.dump(codigosAnimes,archivo)
    archivo.close()

def guardarArchivoSeries(contenidoSeries, codigosSeries):
    archivo = open(f"Contenido/series","bw")
    marshal.dump(contenidoSeries,archivo)
    archivo.close()
    ###
    archivo = open(f"Contenido/codigosSeries","bw")
    marshal.dump(codigosSeries,archivo)
    archivo.close()

def guardarArchivoPeliculas(contenidoPeliculas, codigosPeliculas):
    archivo = open(f"Contenido/peliculas","bw")
    marshal.dump(contenidoPeliculas,archivo)
    archivo.close()
    ###
    archivo = open(f"Contenido/codigosPeliculas","bw")
    marshal.dump(codigosPeliculas,archivo)
    archivo.close()
