import json
import re


def stark_normalizar_datos(listas):
    """
        la función verifica si la lista está vacía. Si no lo está,
        se normalizan los datos y se cuenta cuántos datos han sido
        normalizados. Luego, se imprime un mensaje que indica si
        los datos han sido normalizados o no. Si la lista está
        vacía, se imprime un mensaje indicando que la lista
        está vacía.

    Args:
        listas (list[dict]): La lista de diccionarios de héroes.
        
    Returns:
        None
    """
    modificador_aux = 0

    if (len(listas) != 0):
        for lista in listas:
            if (type(lista["altura"]) != float):
                lista["altura"] = float(lista["altura"])
                modificador_aux += 1
            if (type(lista["peso"]) != float):
                lista["peso"] = float(lista["peso"])
                modificador_aux += 1
            if (type(lista["fuerza"]) != int):
                lista["fuerza"] = int(lista["fuerza"])
                modificador_aux += 1

        if (modificador_aux != 0):
            print("Datos normalizados")
        else:
            print("Lista vacia")

with open('C:/Users/alvar/OneDrive/Documentos/Programacion_P/archivos/data_stark.json','r') as data:
    datos =json.load(data)
    lista = datos['heroes']

stark_normalizar_datos(lista)


##--------------------------------------------------------------------------------------------------------------------------------------------------------

def crear_csv(path: str,heroes:list[dict]) -> None:
    """
    Crea un archivo CSV a partir de una lista de diccionarios de héroes.

    Args:
        path (str): La ruta del archivo CSV a crear.
        heroes_auxuliar (list[dict]): La lista de diccionarios de héroes.

    Returns:
        None
    """
    heroes_auxuliar = heroes[:]

    if heroes_auxuliar:
        lista_string_heroes = [] 

        for heroe in heroes_auxuliar:
            
            dato_heroe = [] #Por cada heroe se crea "dato_heroe"
            
            for value in heroe.values():  #Los valores se van agregando como string de a uno en dato_heroe
                
                dato_heroe.append(str(value))    

            dato_heroe_str = ','.join(dato_heroe)  #se utiliza '\n'.join(lista_string_heroes) para unir todas las filas de la lista lista_string_heroes en una sola cadena separada por comas

            lista_string_heroes.append(dato_heroe_str) 

        datos_para_csv = '\n'.join(lista_string_heroes)

        #----------------------
        #  #El string que quiero escribir en el csv

        #escribir un string en el csv separando campos por coma
        with open(path,"w") as archivo:
            archivo.writelines(datos_para_csv)
    else:
        print("La lista esta vacia.")





###------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# LO MISMO PERO PARA SOLO TOMAR NOMBRE Y ALTURA
def crear_csv_nombres_alturas(path: str, heroes: list[dict]) -> None:
    """
    Crea un archivo CSV con los nombres y alturas de los héroes a partir de una lista de diccionarios de héroes.

    Args:
        path (str): La ruta del archivo CSV a crear.
        heroes_auxiliar (list[dict]): La lista de diccionarios de héroes.

    Returns:
        None
    """
    heroes_auxiliar = heroes[:]

    if heroes_auxiliar:
        lista_string_heroes = []

        for heroe in heroes_auxiliar:
            dato_heroe = []

            for key in ["nombre", "altura"]:
                dato_heroe.append(str(heroe[key]))

            lista_string_heroes.append(','.join(dato_heroe))

        datos_para_csv = '\n'.join(lista_string_heroes)

        with open(path, "w") as archivo:
            archivo.writelines(datos_para_csv)
    else:
        print("La lista está vacía.")

if __name__ == '__main__':

    PATH = 'C:/Users/alvar/OneDrive/Documentos/Programacion_P/notas/data_MARVE.csv' #DATA MARVEL CSV ES EL NOMBRE QUE LE DI, PUEDE SER CUALQUIERA

    crear_csv(PATH,lista)
    

##------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def menu():
        print("Menú de opciones:")
        print("1.Listar numero de heroes")
        print("2.")
        print("3.")
        print("4.")
        print("5.")
        print("6.")
        print("7.")
        print("8.")
        print("9.")
        print("10.")
        print('11.')
        print('12.')
        print('13.')
        print('14.')
        print('15.')
        print("16.")
        print("17.")
        print("18.")
        print("19.")
        print("20.")
        print("0.")

def validar_numeros(texto,patron):
    """
    Valida un numero dependiendo el patron que se le de

    Args:
        texto (str): Texto o numero a validar
        patron (str): Patron regex a cumplir
    Returns:
        Devuelve el texto en caso de cumplirse el patron (str)
        Devuelve -1 en caso de no cumplirse o no ingresar nignun texto(str)
    """
    if texto:
            if re.match(patron,texto):
                return texto
            else: return "-1"
    return "-1"

# menu()
# opcion = input("\nIngrese la opción deseada: ")
# opcion = validar_numeros(opcion,"^[0-7]{1}$")


# orden = asc_desc()
# if orden == -1:
#     print("Error")
# else:
#     heroes_ordenados = ordenar_y_listar_heroes(lista,"altura",orden)
#     for heroes in heroes_ordenados:
#         print("{0},{1}.".format(heroes['nombre'],heroes['altura']))

#------------------------------------------------------------------------------------------------------------------------------------------------------------------

def ordenar_y_listar_heroes(heroes: list, key: str, orden: bool)-> list:
    """
    Devuelve una lista ordenada de heroes sea ascendete o descendente elegido por el usuario

    Args:
        heroes (list): Lista de heroes
        key (str): Key a elegir para ordenar
        orden (bool): Orden deseado
    Returns:
        lista_izquierda (list): Lista con valores ordenados
    """
    if len(heroes) <= 1:
        return heroes

    pivot = heroes[0]
    lista_derecha = []
    lista_izquierda = []

    for elemento in heroes[1:]:
        if (orden and elemento[key] > pivot[key]) or (not orden and elemento[key] < pivot[key]):
            lista_derecha.append(elemento)
        else:
            lista_izquierda.append(elemento)

    lista_izquierda = ordenar_y_listar_heroes(lista_izquierda, key, orden)
    lista_izquierda.append(pivot)

    lista_derecha = ordenar_y_listar_heroes(lista_derecha, key, orden)
    lista_izquierda.extend(lista_derecha)

    return lista_izquierda
