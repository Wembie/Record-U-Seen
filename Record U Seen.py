from Packages.Menus import *
from Packages.Funciones import *
from Packages.Animes import animes
from Packages.Series import series
from Packages.Peliculas import peliculas

import time
import os
import os.path as path
        
def main():
    os.system( 'TITLE Record U Seen' )
    contenidoAnimes = []
    codigosAnimes = []
    contenidoSeries = []
    codigosSeries = []
    contenidoPeliculas = []
    codigosPeliculas = []
    if path.exists( "Contenido" ):
        #Animes
        archivo = open( f"Contenido/animes", "br" )
        contenidoAnimes = marshal.load( archivo )
        archivo.close()
        ###
        archivo = open( f"Contenido/codigosAnimes", "br" )
        codigosAnimes = marshal.load( archivo )
        archivo.close()
        #Series
        archivo = open( f"Contenido/series", "br" )
        contenidoSeries = marshal.load( archivo )
        archivo.close()
        ###
        archivo = open( f"Contenido/codigosSeries", "br" )
        codigosSeries = marshal.load( archivo )
        archivo.close()
        #Peliculas
        archivo = open( f"Contenido/peliculas", "br" )
        contenidoPeliculas = marshal.load( archivo )
        archivo.close()
        ###
        archivo = open( f"Contenido/codigosPeliculas", "br" )
        codigosPeliculas = marshal.load( archivo )
        archivo.close()    
    else:
        os.mkdir( "Contenido" )
        guardarArchivoAnimes( contenidoAnimes, codigosAnimes )
        guardarArchivoSeries( contenidoSeries, codigosSeries )
        guardarArchivoPeliculas( contenidoPeliculas, codigosPeliculas )
    while True:
        menuPrincipal()
        opcionMenuPrincipal = preguntarNumero( 0, 3, "[0,1,2,3]" )
        os.system( 'cls' )
        if opcionMenuPrincipal == 0: #Salir
            print( "Gracias por usar la aplicacion RECORD U SEEN vuelve pronto :D" )
            time.sleep( 2 )
            return
        elif opcionMenuPrincipal == 1: #Animes
            animes( contenidoAnimes, codigosAnimes )
        elif opcionMenuPrincipal == 2: #Series
            series( contenidoSeries, codigosSeries )
        elif opcionMenuPrincipal == 3: #Peliculas
            peliculas( contenidoPeliculas, codigosPeliculas )
        
main()