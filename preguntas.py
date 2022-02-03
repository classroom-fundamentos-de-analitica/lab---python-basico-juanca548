"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

import csv

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    with open('data.csv', encoding='latin1') as fichero_csv:
        lector = csv.reader(fichero_csv)
        suma = 0
        for linea in lector:
            suma+=int(linea[0][2])
    print(suma)        
    return suma




def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    with open('data.csv', encoding='latin1') as fichero_csv:
        lector = csv.reader(fichero_csv)
        letras = ["A","B","C","D","E"]
        listaLetras = []
        frecuenciaLetras = []
        for linea in lector:
            listaLetras.append(linea[0][0])
        for letra in letras:
            frecuenciaLetras.append(listaLetras.count(letra))
    a = list(zip(letras, frecuenciaLetras))       
    return a



def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    with open('data.csv', encoding='latin1') as fichero_csv:
        lector = csv.reader(fichero_csv)
        sumaA = 0
        sumaB = 0
        sumaC = 0
        sumaD = 0
        sumaE = 0
        for linea in lector:
            if linea[0][0] == "A":
                sumaA+=int(linea[0][2])

            if linea[0][0] == "B":
                sumaB+=int(linea[0][2])

            if linea[0][0] == "C":
                sumaC+=int(linea[0][2])

            if linea[0][0] == "D":
                sumaD+=int(linea[0][2])

            if linea[0][0] == "E":
                sumaE+=int(linea[0][2])
    a = [("A",sumaA),("B",sumaB),("C",sumaC),("D",sumaD),("E",sumaE)]
    return a


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    with open('data.csv', encoding='latin1') as fichero_csv:
        lector = csv.reader(fichero_csv)
        listaNumeros = []
        Numeros = ["01","02","03","04","05","06","07","08","09","10","11","12"]
        frecuenciaNumeros = []
        for linea in lector:
            if linea[0][9] == "0":
                a = "0"+linea[0][10]
                listaNumeros.append(a)
            else:
                a = "1"+linea[0][10]
                listaNumeros.append(a)
        for numero in Numeros:
            frecuenciaNumeros.append(listaNumeros.count(numero))

    a = list(zip(Numeros, frecuenciaNumeros))
    return a




def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    with open('data.csv', encoding='latin1') as fichero_csv:
        lector = csv.reader(fichero_csv)
        maxA = 0
        minA = 10
        maxB = 0
        minB = 10
        maxC = 0
        minC = 10
        maxD = 0
        minD = 10
        maxE = 0
        minE = 10
        for linea in lector:
            if linea[0][0] == "A":
                if int(linea[0][2]) < minA:
                    minA = int(linea[0][2])
                if int(linea[0][2]) > maxA:
                    maxA = int(linea[0][2])

            if linea[0][0] == "B":
                if int(linea[0][2]) < minB:
                    minB = int(linea[0][2])
                if int(linea[0][2]) > maxB:
                    maxB = int(linea[0][2])

            if linea[0][0] == "C":
                if int(linea[0][2]) < minC:
                    minC = int(linea[0][2])
                if int(linea[0][2]) > maxC:
                    maxC = int(linea[0][2])

            if linea[0][0] == "D":
                if int(linea[0][2]) < minD:
                    minD = int(linea[0][2])
                if int(linea[0][2]) > maxD:
                    maxD = int(linea[0][2])

            if linea[0][0] == "E":
                if int(linea[0][2]) < minE:
                    minE = int(linea[0][2])
                if int(linea[0][2]) > maxE:
                    maxE = int(linea[0][2])

    a = [("A",maxA,minA),("B",maxB,minB),("C",maxC,minC),("D",maxD,minD),("E",maxE,minE)]
    return a

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    with open("./data.csv", "r") as file:
        datos = file.readlines()
    datoscsv = [line.replace("\n", "") for line in datos]
    datosLimpios = [line.split("\t") for line in datoscsv]
    listaKeys = []
    listaT = []
    listaMax = []
    listaMin = []

    for dato in datosLimpios:
        res = []
        for sub in dato[4].split(','):
            if ':' in sub:
                res.append(map(str.strip, sub.split(':', 1)))
        res = dict(res)
        for k in res.keys():
            letra = k
            if letra in listaKeys:
                val = listaKeys.index(letra)
                listaT[val].append(int(res[k]))
            else:
                listaKeys.append(letra)
                listaT.append([int(res[k])])
    for ele in listaT:
        listaMax.append(max(ele))
        listaMin.append(min(ele))
    lista = list(zip(listaKeys, listaMin, listaMax))
    return sorted(lista, key=lambda tup: tup[0])


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    with open('data.csv', encoding='latin1') as fichero_csv:
        lector = csv.reader(fichero_csv)
        letra0 = []
        letra1 = []
        letra2 = []
        letra3 = []
        letra4 = []
        letra5 = []
        letra6 = []
        letra7 = []
        letra8 = []
        letra9 = []
        for linea in lector:
            if int(linea[0][2]) == 0:
                letra0.append(linea[0][0])

            if int(linea[0][2]) == 1:
                letra1.append(linea[0][0])

            if int(linea[0][2]) == 2:
                letra2.append(linea[0][0])

            if int(linea[0][2]) == 3:
                letra3.append(linea[0][0])

            if int(linea[0][2]) == 4:
                letra4.append(linea[0][0])

            if int(linea[0][2]) == 5:
                letra5.append(linea[0][0])

            if int(linea[0][2]) == 6:
                letra6.append(linea[0][0])

            if int(linea[0][2]) == 7:
                letra7.append(linea[0][0])

            if int(linea[0][2]) == 8:
                letra8.append(linea[0][0])

            if int(linea[0][2]) == 9:
                letra9.append(linea[0][0])
    a = [(0,letra0),(1,letra1),(2,letra2),(3,letra3),(4,letra4),(5,letra5),(6,letra6),(7,letra7),(8,letra8),(9,letra9)]
    return a



def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    with open('data.csv', encoding='latin1') as fichero_csv:
        lector = csv.reader(fichero_csv)
        letra0 = []
        letra1 = []
        letra2 = []
        letra3 = []
        letra4 = []
        letra5 = []
        letra6 = []
        letra7 = []
        letra8 = []
        letra9 = []
        for linea in lector:
            if int(linea[0][2]) == 0:
                letra0.append(linea[0][0])

            if int(linea[0][2]) == 1:
                letra1.append(linea[0][0])

            if int(linea[0][2]) == 2:
                letra2.append(linea[0][0])

            if int(linea[0][2]) == 3:
                letra3.append(linea[0][0])

            if int(linea[0][2]) == 4:
                letra4.append(linea[0][0])

            if int(linea[0][2]) == 5:
                letra5.append(linea[0][0])

            if int(linea[0][2]) == 6:
                letra6.append(linea[0][0])

            if int(linea[0][2]) == 7:
                letra7.append(linea[0][0])

            if int(linea[0][2]) == 8:
                letra8.append(linea[0][0])

            if int(linea[0][2]) == 9:
                letra9.append(linea[0][0])
    a = [(0,sorted(list(set(letra0)))),(1,sorted(list(set(letra1)))),(2,sorted(list(set(letra2)))),(3,sorted(list(set(letra3)))),(4,sorted(list(set(letra4)))),(5,sorted(list(set(letra5)))),(6,sorted(list(set(letra6)))),(7,sorted(list(set(letra7)))),(8,sorted(list(set(letra8)))),(9,sorted(list(set(letra9))))]
    return a




def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    with open("./data.csv", "r") as file:
        datos = file.readlines()
    datoscsv = [line.replace("\n", "") for line in datos]
    datosLimpios = [line.split("\t") for line in datoscsv]
    listaKeys = []
    listaT = []
    listaN = []

    for dato in datosLimpios:
        res = []
        for sub in dato[4].split(','):
            if ':' in sub:
                res.append(map(str.strip, sub.split(':', 1)))
        res = dict(res)
        for k in res.keys():
            letra = k
            if letra in listaKeys:
                val = listaKeys.index(letra)
                listaT[val].append(int(res[k]))
            else:
                listaKeys.append(letra)
                listaT.append([int(res[k])])
    for ele in listaT:
        listaN.append(len(ele))
    lista = dict(zip(listaKeys, listaN))
    return lista
    

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    with open("./data.csv", "r") as file:
        datos = file.readlines()
    datoscsv = [line.replace("\n", "") for line in datos]
    datosLimpios = [line.split("\t") for line in datoscsv]
    listaKeys = []
    listaA = []
    listaD = []
    for dato in datosLimpios:
        res = []
        listaKeys.append(dato[0])
        lista = dato[3].split(',')
        listaA.append(len(lista))
        for sub in dato[4].split(','):
            if ':' in sub:
                res.append(map(str.strip, sub.split(':', 1)))
        res = dict(res)
        listaD.append(len(res))

    lista = list(zip(listaKeys, listaA, listaD))
    return lista

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    with open("./data.csv", "r") as file:
        datos = file.readlines()
    datoscsv = [line.replace("\n", "") for line in datos]
    datosLimpios = [line.split("\t") for line in datoscsv]
    diccio = {}
    for dato in datosLimpios:
        valor = int(dato[1])
        for letra in dato[3].split(','):
            if letra in diccio:
                diccio[letra] += valor
            else:
                diccio[letra] = valor
    return diccio

   


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    with open("./data.csv", "r") as file:
        datos = file.readlines()
    datoscsv = [line.replace("\n", "") for line in datos]
    datosLimpios = [line.split("\t") for line in datoscsv]
    diccio = {}
    for dato in datosLimpios:
        res = []
        letra = dato[0]
        for sub in dato[4].split(','):
            if ':' in sub:
                res.append(map(str.strip, sub.split(':', 1)))
        res = dict(res)
        res = dict([a, int(x)] for a, x in res.items())
        valor = sum(res.values())
        if letra in diccio:
            diccio[letra] += valor
        else:
            diccio[letra] = valor
    return diccio
