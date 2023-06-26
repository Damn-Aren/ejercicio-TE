import numpy as np
import os
import msvcrt
import time
list_fila = []
list_columna = []
#{-----------------------------------------------------------------------------------------}
arreglo_edifi = np.zeros((3,4), int)
arreglo_caro = np.zeros ((7,4), int)
#{-----------------------------------------------------------------------------------------}
class bcolor:
    G = '\033[92m'
    R = '\033[91m'
    reset = '\033[0m'
#{-----------------------------------------------------------------------------------------}
def menu_principal():
    while True:
        os.system ('cls')
        print ("""
        {====== Menú Venta de apartamentos: =======}
        \t1.- Ver edificio
        \t2.- Comprar edificio
        {==========================================}
        \t3.- Buscar Dueño
        \t4.- Ganancias Totales

        5.- SALIR
        {==========================================}
        """)
        return
#{=========================================================================================}
def vali_opcion():
    while True:
        try:
            opci = int(input("Ingrese una opción: "))
            if opci in (1,2,3,4,5,6):
                return opci
            else:
                print(bcolor.R+ "Opcion no valida, reintente" +bcolor.reset)
        except:
            print(bcolor.R+ "Debe ingresar un numero de opcion" +bcolor.reset)
            os.system('cls')
#{=========================================================================================}
def ver_edificios ():
    os.system ('cls')
    print("  = Mostrando el edificio =")
    print("")
    for x in range(3): #filas
        print(f"Pisos 10  |", end=" ")
        for y in range(4): #columnas
            if arreglo_edifi [x][y] == 0:
                print (bcolor.G + f"{arreglo_edifi[x][y]}", end=" " + bcolor.reset)
            else:
                print (bcolor.R + f"{arreglo_edifi[x][y]}", end=" " + bcolor.reset)
        print ()
    for x in range (7):
        print(f"Pisos 10  |", end=" ")
        for y in range (4):
            if arreglo_caro [x][y] == 0:
                print (bcolor.G + f"{arreglo_caro[x][y]}", end=" " + bcolor.reset)
            else:
                print (bcolor.R + f"{arreglo_caro[x][y]}", end=" " + bcolor.reset)
        print ()
    print("\t  -----------")
    print("\t  | 1 2 3 4 |")
    print("")
    print(bcolor.G + "Presione una tecla para continuar" + bcolor.reset)
    msvcrt.getch()
#{=========================================================================================}
def seleccion_edificio_fila():
        while True:
            try:
                fila = int(input("Ingrese el piso a comprar: "))
                if fila in (1,2,3,4,5,6,7,8,9,10):
                    break
                else:
                    print(bcolor.R + "Piso no existente" + bcolor.reset)
            except:
                print(bcolor.R + "Debe ingresar el numero del piso a comprar" + bcolor.reset)
#{=========================================================================================}
def seleccion_edificio_columna():
        while True:
            try:
                columna = int(input("Ingrese el departamento a comprar: "))
                if columna in (1,2,3,4):
                    break
                else:
                    print(bcolor.R + "Departamento no existente" + bcolor.reset)
            except:
                print(bcolor.R + "Debe ingresar el numero del departamento a comprar" + bcolor.reset)
#{=========================================================================================}
def proceso_seleccion_edificio ():
    fila = seleccion_edificio_fila()
    columna = seleccion_edificio_columna()
    if arreglo_edifi[fila-1][columna-1] == 0:
        arreglo_edifi[fila-1][columna-1] = 1    
        list_fila.append(fila-1)
        list_columna.append(columna-1)
        print(bcolor.G + "Registro realizado con exito!" + bcolor.reset)
        time.sleep(3)
    else:
        print (bcolor.R + "Su asiento esta ocpuado actualmente" + bcolor.reset)
        time.sleep(3)
    if arreglo_caro [fila-1][columna-1] == 0:
        arreglo_caro [fila-1][columna-1]
        list_fila.append(fila-1)
        list_columna.append(columna-1)
        print(bcolor.G + "Registro realizado con exito!" + bcolor.reset)
        time.sleep(3)
    else:
        print (bcolor.R + "Su asiento esta ocpuado actualmente" + bcolor.reset)
        time.sleep(3)
