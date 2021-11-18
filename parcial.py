import os, funciones

menu = """
Bienvenidos al programa de registro de robos\na continuación ingrese la opcion deseada
===========================================================
[1] - Agregar datos
[2] - Modificar datos
[3] - Eliminar datos 
[4] - Exportar
[5] - Salir
"""
#************************FUNCION PRINCIPAL***************************

def main():
    os.system("cls")
    print(menu)
    opcion = int(input("Ingrese la opción aquí: "))
    if opcion == 1:
        funciones.createrow()
        main()
    if opcion == 2:
        funciones.updaterow()
    if opcion == 3:
        funciones.deleterow()
    if opcion == 4:
        funciones.exportar()
    if opcion == 5:
        opt = input("¿Seguro que desea salir? [s/n]:")
        if opt == "s":
            os.system("exit")
        else:
            main()

#********************EJECUCIÓN DEL PROGRAMA************************
if __name__=="__main__":
    main()

