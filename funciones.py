import os, webbrowser, parcial
from sqlite3.dbapi2 import Cursor, OptimizedUnicode
import sqlite3 as sql
import folium
from geopy.geocoders import Nominatim
from prettytable import from_db_cursor

#****************MENUS SECUNDARIOS**********************
menuact = """
Elija el campo a actualizar
===========================
[1] - Cédula
[2] - Nombre
[3] - Fecha
[4] - Monto de lo robado
[5] - Lugar del suceso
[6] - Salir
"""
menuexpo = """
Elija la opción correspondiente
===============================
[1] - Contrato
[2] - Mapa con los robos
[3] - Salir
"""

#****************CREACION DE BASE DE DATOS******************
def createdb():
    conn = sql.connect("Registro_robo.db")
    conn.commit()
    conn.close()

def createtable():
    conn = sql.connect("Registro_robo.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE Registro_robo(
        Cedula varchar(15) PRIMARY KEY,
        Nombre varchar(15),
        Fecha varchar(15),
        Valor varchar(15),
        Lugar varchar(50),
        Latitud real,
        Longitud real
    )
    """)
    conn.commit()
    conn.close()

#*****************INTRODUCCIÓN DE DATOS A LA DATABASE**********************
def createrow():
    try: 
        os.system("cls")
        showtable()
        opcion = input("Presione Enter para empezar o pulse s para salir")
        if opcion == "s":
            parcial.main()
        else:
            cedula = input("Ingrese la cédula del ladrón: ")
            nombre = input("Ingrese el nombre del ladrón: ")
            fecha = input("Ingrese la fecha de cuando ocurrió el robo: ")
            valor = input("Ingrese el monto de lo robado: $")
            lugar = input("Ingrese el lugar del suceso: ")
            geo = Nominatim(user_agent="Latitudelng")
            loc = geo.geocode(f"{lugar}")
            Latitude = f"{loc.latitude}, {loc.longitude}"
            conn = sql.connect("Registro_robo.db")
            cursor = conn.cursor()
            intruccion = (f"INSERT INTO Registro_robo VALUES ({cedula}, '{nombre}', '{fecha}', {valor}, '{lugar}', {loc.latitude}, {loc.longitude})")
            cursor.execute(intruccion)
            conn.commit()
            conn.close()
    except:
        input("Ingrese el valor correspondiente en cada campo por favor")

#********************ELIMINAR DATOS*******************************
def deleterow():
    os.system("cls")
    showtable()
    cedula = input("Ingrese la cédula de la persona a eliminar: ")
    opt = input("¿Seguro que desea continuar? [s/n]: ")
    if opt == "s":
        conn = sql.connect("Registro_robo.db")
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM Registro_robo WHERE Cedula={cedula}")
        conn.commit()
        conn.close()
        parcial.main()
    elif opt == "n":
        parcial.main()
    else:
        input("Ingrese una opción válida por favor 's' o 'n'")

#**************************ACTUALIZAR DATOS************************
def updaterow():
    os.system("cls")
    print(menuact)
    opcion = int(input("Ingrese la opción correspondiente: "))

    if opcion == 1:
        os.system("cls")
        showtable()
        cdl = input("Ingrese la cédula de la persona a modificar: ")
        os.system("cls")
        showtablecedu(cdl)
        cedula = input("Ingrese la nueva cédula: ")
        conn = sql.connect("Registro_robo.db")
        cursor = conn.cursor()
        cursor.execute(f"UPDATE Registro_robo SET Cedula={cedula} WHERE Cedula={cdl}")
        conn.commit()
        conn.close()
        parcial.main()

    elif opcion == 2:
        os.system("cls")
        showtable()
        cdl = input("Ingrese la cédula de la persona a modificar: ")
        os.system("cls")
        showtablecedu(cdl) 
        nombre = input("Ingrese el nuevo nombre: ")
        conn = sql.connect("Registro_robo.db")
        cursor = conn.cursor()
        cursor.execute(f"UPDATE Registro_robo SET Nombre='{nombre}' WHERE Cedula={cdl}")
        conn.commit()
        conn.close()
        parcial.main()

    elif opcion == 3:
        os.system("cls")
        showtable()
        cdl = input("Ingrese la cédula de la persona a modificar: ")
        os.system("cls")
        showtablecedu(cdl)
        fecha = input("Ingrese la nueva fecha: ")
        conn = sql.connect("Registro_robo.db")
        cursor = conn.cursor()
        cursor.execute(f"UPDATE Registro_robo SET Fecha='{fecha}' WHERE Cedula={cdl}")
        conn.commit()
        conn.close()
        parcial.main()

    elif opcion == 4:
        os.system("cls")
        showtable()
        cdl = input("Ingrese la cédula de la persona a modificar: ")
        os.system("cls")
        showtablecedu(cdl)
        valor = input("Ingrese el nuevo valor: ")
        conn = sql.connect("Registro_robo.db")
        cursor = conn.cursor()
        cursor.execute(f"UPDATE Registro_robo SET Valor={valor} WHERE Cedula={cdl}")
        conn.commit()
        conn.close()
        parcial.main()

    elif opcion == 5:
        os.system("cls")
        showtable()
        cdl = input("Ingrese la cédula de la persona a modificar: ")
        os.system("cls")
        showtablecedu(cdl)
        lugar = input("Ingrese el nuevo lugar: ")
        conn = sql.connect("Registro_robo.db")
        cursor = conn.cursor()
        cursor.execute(f"UPDATE Registro_robo SET Lugar='{lugar}' WHERE Cedula={cdl}")
        conn.commit()
        conn.close()
        parcial.main()

    elif opcion == 6:
        parcial.main()

#********************CONTRATO DE ROBO*********************
def contrato():
    os.system("cls")
    showtable()
    cedula = int(input("Ingrese la cédula de la persona que desea exportar en un caso: "))
    conn = sql.connect("Registro_robo.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM Registro_robo"
    cursor.execute(instruccion)
    Registro_robo = cursor.fetchall()
    for i in range(len(Registro_robo)):
        cedula = Registro_robo[i][0]
        nombre = Registro_robo[i][1]
        fecha = Registro_robo[i][2]
        valor = Registro_robo[i][3]
        lugar = Registro_robo[i][4]
    html = f"""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css">
    <title>Caso de robo</title>
</head>
<body>
    <div>
    <h1>Denuncia de Robo</h1>
    <h2>Demandante: {nombre}</h2>
    <br>
    <img src="foto.jpg" alt="">
    <p>El/La senior/a {nombre}, dominicano/a mayor de edad, titular de la cedula de identidad y
    electoral No.{cedula}, domiciliado/a y residente en {lugar}. El senior/a {nombre} es acusado de robar
    un objeto con el valor de {valor} pesos dominicanos, en la localidad de {lugar}, de la fecha {fecha}. Residentes de
    dicha localidad afirman lo sucedido.</p>
    <br>
    <p>El senior/a {nombre}, sera llevado a justicia lo antes posible para que se le otorguen 
        las medidas necesarias por el robo del que se le acusa.
    </p>
    </div>
</body>
</html>
    """
    nombre_archivo = ("Caso_robo.html")
    archivo = open(nombre_archivo, "w")
    archivo.write(html)
    archivo.close()
    webbrowser.open_new_tab(nombre_archivo)   

#****************************MAPA DE DATOS********************************
def mapa():
    conn = sql.connect("Registro_robo.db")
    cursor = conn.cursor()
    instruccion = "SELECT * FROM Registro_robo"
    cursor.execute(instruccion)
    Registro_robo = cursor.fetchall()
    m = folium.Map(location=[18.669175,-71.2515167], zoom_start=10, tiles="Stamen Terrain")
    for i in range(len(Registro_robo)):
        lugar = Registro_robo[i][1]
        Latitud = Registro_robo[i][5]
        Longitud = Registro_robo[i][6]
        marker = folium.Marker(location=[Latitud, Longitud], popup=f"<i>{lugar}</i>", icon=folium.Icon(color="red"))
        marker.add_to(m)
    m.save("mapa.html")
    webbrowser.open_new_tab("mapa.html")

#*************************EXPORTAR LOS DATOS******************
def exportar():
    os.system("cls")
    print(menuexpo)
    opcion = int(input("Ingrese la opción deseada: "))
    if opcion == 1:
        contrato()
    elif opcion == 2:
        mapa()
    elif opcion == 3:
        parcial.main()

#*******************MOSTRAR DATOS (TABLAS)************************
def showtable():
    conn = sql.connect("Registro_robo.db")
    cursor = conn.cursor()
    intruccion = "SELECT * FROM Registro_robo"
    cursor.execute(intruccion)
    x = from_db_cursor(cursor)
    print(x)

def showtablecedu(cedula):
    conn = sql.connect("Registro_robo.db")
    cursor = conn.cursor()
    intruccion = f"SELECT * FROM Registro_robo WHERE Cedula={cedula}"
    cursor.execute(intruccion)
    x = from_db_cursor(cursor)
    print(x)

#*********************PRUEBA DE LAS FUNCIONES*************************
if __name__=="__main__":
    # createdb()
    # createtable()
    mapa()