from VDE_Funciones import *
#{=========================================================================================}
while True:
    menu_principal()
#{=========================================================================================}
    opci = vali_opcion()
    if opci == 1:
        ver_edificios()
    elif opci == 2:
        ver_edificios()
        proceso_seleccion_edificio()
    elif opci == 3:
        pass
    elif opci == 4:
        pass
    else:
        print("Gracias por la visita!")
        time.sleep (3)
        break