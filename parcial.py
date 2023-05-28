import re
import json
import csv

ruta_jugadores_json = 'C:/Users/alvar/OneDrive/Documentos/Programacion_P/PARCIALES/pp_lab1_alvarez_dylan_lautaro/dt.json'


#-----------CARGA DE JASON---------------
with open(ruta_jugadores_json,'r',encoding='utf-8') as data:
    datos =json.load(data)
    lista_jugadores = datos['jugadores']


#-----------MENU---------------
def menu():
        print("Menú de opciones:")
        print("1.Mostrar la lista de todos los jugadores del Dream Team")
        print("2.Mostrar sus estadísticas segun su indice")
        print("3.Guardar las estadísticas del Jugador seleccionador en el punto 2 en un archivo CSV")
        print("4.Buscar un jugador por su nombre y mostrar sus logros,")
        print("5.Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team, ordenado por nombre de manera ascendente. ")
        print("6.Permitir al usuario ingresar el nombre de un jugador y mostrar si ese jugador es miembro del Salón de la Fama del Baloncesto.")
        print("7.Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.")
        print("8.Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo.")
        print("9.Calcular y mostrar el jugador con la mayor cantidad de asistencias totales.")
        print("10.Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado más puntos por partido que ese valor.")
        print("11.Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado más rebotes por partido que ese valor.")
        print("12.Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado más asistencias por partido que ese valor.")
        print("13.Calcular y mostrar el jugador con la mayor cantidad de robos totales.")
        print("14.Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales.")
        print("15.Permitir al usuario ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor.")
        print("16.Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.")
        print("17.Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos")
        print("18.Permitir al usuario ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor.")
        print("19.Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas")
        print("20.Ingresar un valor y mostrar los jugadores , ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor.")

        
















#-----------VALIDAR NUMEROS---------------
def validar_numeros(texto: str, patron: str):
    """
    Valida un texto dependiendo del patrón que se le de

    Args:
        texto (int): texto a validar
        patron (str): Patrón regex a cumplir
    Returns:
        Devuelve el texto en caso de cumplirse el patrón (str)
        Devuelve -1 en caso de no cumplirse o no ingresar ningún texto (int)
    """
    if texto:
        if re.match(patron, texto):
            return texto
        else:
            return "-1"
    return "-1"


#-----------CALCULAR PROMEDIO---------------
def calcular_promedio(lista:list,dato) -> int:
        """
        Calcula el promedio de un dato de estadisticas recibiendo el dato y contando todos los jugadores que contengan ese dato

        Arg:
                lista(list):Lista de jugadores
        Returns: 
                promedio(int):Promedio final del dato entre todos los jugadores
        """
        acumulador_promedio = 0
        for jugador in lista:
                acumulador_promedio += jugador['estadisticas'][dato]
        promedio = acumulador_promedio/len(lista)
        return promedio
       


#----------------------------------------------
#1
def mostrar_jugadores(lista:list) -> None:
        """
        Muestra todos los jugadores de la lista de jugadores junto con su posicion de juego

        Arg:
                lista(list):Lista de jugadores
        Returns: 
                None
        """
        if lista:
                for jugadores in lista:
                        print("{0} - {1}".format(jugadores['nombre'],jugadores['posicion']))
        else:
               print("La lista esta vacia.")
       
#--------------------------------------------------
#2
def mostrar_jugador_estadisticas(lista:list,indice:int):
        """
        Muestra las estadisticas de un jugador usando su indice

        Arg:
                lista(list):Lista de jugadores
                indice(int):Indice del jugador para ver sus estadisticas
        Returns:
                None
        
        """
        jugador = lista[indice]
        print("nombre: {0}".format(jugador['nombre']))
        for key,valor in jugador['estadisticas'].items():
                
                print("{0} : {1}".format(key,valor))
#--------------------------------------------------
#3


def crear_csv_2(path: str, lista: list[dict],indice:int) -> None:
    """
    Crea un archivo CSV de un jugador seleccionado previamente en el punto 2, mostrando todos sus datos

    Args:
        path (str): La ruta del archivo CSV a crear.
        jugadores_auxuliar (list[dict]): La lista de jugadores 

    Returns:
        None
    """
    jugadores_auxuliar = lista[:]

    if jugadores_auxuliar:
 
            
        jugador = jugadores_auxuliar[indice]


        dato_jugador = []
        estadisticas = []
        for key,valor in jugador["estadisticas"].items():
                estadisticas.append("{0}:{1} ".format(key,valor))

        estadisticas = "\n".join(estadisticas)

        jugador["estadisticas"] = estadisticas

        for valor in ["nombre", "posicion","estadisticas"]:

                dato_jugador.append(str(jugador[valor]))

        datos_para_csv = "\n".join(dato_jugador)
        

        with open(path, "w") as archivo:
            archivo.writelines(datos_para_csv)
    else:
        print("La lista está vacía.")

if __name__ == '__main__':

    PATH = 'C:/Users/alvar/OneDrive/Documentos/Programacion_P/PARCIALES/data_csv_2.csv'

    

#--------------------------------------------------
#4

def mostrar_jugador_por_nombre(lista:list,nombre:str):
        """
        Buscar un jugador por su nombre para ver todos sus logros

        Arg:
                lista(list):Lista de jugadores
                nombre(str): Nombre del jugador que se desea buscar
        Returns: 
                None
        """
        contador_no_coincidencias = 0
        for jugador in lista:
                if re.search(nombre,jugador['nombre']):
                        for logros in jugador['logros']:
                                print(logros)
                        print("-------------------")
                else:
                        contador_no_coincidencias += 1
        if contador_no_coincidencias == len(lista):
                print("No hubo coincidencias")

#----------------------------------------------------
#5

def calcular_mayor_equipo(lista_original:list,indice_a_buscar:str) -> list:
        """
        Ordena de manera mayor a menor los jugadores de la lista recibiendo un dato como inicio

        Arg:
                lista_original(list):Lista de jugadores
                indice_a_buscar(str):Dato que se desea buscar el mayor
        Returns: 
                lista_izquierda(list): Lista de los diccionarios de los jugadores totalmente ordenada
        """
        lista = lista_original [:]
        lista_derecha = []
        lista_izquierda = []
        if (len(lista)<=1):
                return lista
        else:
                for elemento in lista[1:]:
                        if (elemento[indice_a_buscar] > lista[0][indice_a_buscar]):
                                lista_derecha.append(elemento)
                        else:
                                lista_izquierda.append(elemento)

        lista_izquierda = calcular_mayor_equipo(lista_izquierda,indice_a_buscar)
        lista_derecha = calcular_mayor_equipo(lista_derecha,indice_a_buscar)
        lista_izquierda.append(lista[0])
        lista_izquierda.extend(lista_derecha)


        return lista_izquierda
#-----------------------------------------------------
#6

def verificar_salon_de_la_fama(lista:list,nombre:str) -> None:
        """
        Verifica si el jugador que se ingreso pertenece al salon de la fama, en caso de pertenecer o no se hace aviso mediante un print 

        Arg:
                lista(list):Lista de jugadores
                nombre(str):Jugador que se desea buscar
        Returns: 
                None
        """
        contador_no_coincidencias = 0
        for jugador in lista:
                contador_no_coincidencias_fama = 0
                if re.search(jugador['nombre'][0:4],nombre[0:4]):
                        for logro in jugador['logros']:
                                if(logro != "Miembro del Salon de la Fama del Baloncesto"):
                                       contador_no_coincidencias_fama += 1

                        if contador_no_coincidencias_fama == len(jugador['logros']):
                               print("El jugador no pertece al salon de la fama")
                        else:
                                print("El pertece al salon de la fama")
                                
                        print("-------------------")
                else:
                        contador_no_coincidencias += 1
        if contador_no_coincidencias == len(lista):
                print("No hubo coincidencias")

#-----------------------------------------------------
#7 8 9 13 14

def calcular_max_min(lista:list,dato:str,max_min:bool) -> None:
        """
        Calcula el maximo y minimo de una lista, usando si lista "estadisticas" y eligiendo el dato a comparar

        Arg:
                lista(list):Lista de jugadores
                dato:(str):dato a buscar de "estadisticas"
                max_min(bool): Dato booleano, Maximo para encontrar el mayor, y False para encontrar el minimo
        Returns: 
                nombre_mas_alto(str):Nombre del jugador con el dato mas alto de todos en caso de que se use True en el booleano
                nombre_mas_bajo(str):Nombre del jugador con el dato mas bajo de todos en caso de que se use False en el booleano
        """
  

        valor_mas_alto = None
        valor_mas_bajo = None

    
        for jugador in lista:
                if(max_min == True):
                        valor = jugador["estadisticas"][dato]
                        if valor_mas_alto == None or valor > valor_mas_alto:
                                valor_mas_alto = valor
                                nombre_mas_alto = jugador["nombre"]
                else:
                        valor = jugador["estadisticas"][dato]
                        if valor_mas_alto == None or valor < valor_mas_bajo:
                                valor_mas_bajo = valor
                                nombre_mas_bajo = jugador["nombre"]
        

        if(max_min==True):
                return nombre_mas_alto
        else:
                return nombre_mas_bajo
#-----------------------------------------------------
#10 11 12 15 18

def promedio_mayor_a(lista:list,numero_ingresado:int,dato:str) -> None:
        """
        Encuentra el promedio mayor usando un dato ingresado por el usuario como comienzo, todos los jugadores que tengan un 
        promedio mayor al numero ingresado se mostraran mediante print


        Arg:
                lista(list):Lista de jugadores
                numero_ingresado(int):Numero ingresado por el usuario
                dato(str):dato a comparar
        Returns: 
                None
        """

        for jugador in lista:
               if jugador["estadisticas"][dato] > numero_ingresado:
                      print("{0} que es {1} supera ese valor en {2} con {3}".format(jugador["nombre"],jugador["posicion"],dato,jugador["estadisticas"][dato]))

#-----------------------------------------------------
#16

def promedio_sin_el_ultimo(lista:list,dato:str):
        """
        Calcular promedio sin el ultimo en la lista, para esto primero se encuentra el nombre del ultimo en la lista y luego se lo elimina con remove


        Arg:
                lista(list):Lista de jugadores
                dato(str):dato a comparar
        Returns: 
                promedio_final(int):Promedio final sin el ultimo jugador 
        """

        lista_auxiliar = lista[:]

        nombre_menos = calcular_max_min(lista_auxiliar,dato,False)

        for jugador in lista_auxiliar:

                if jugador["nombre"] == nombre_menos:

                        lista_auxiliar.remove(jugador)


        promedio_final = calcular_promedio(lista_auxiliar,dato)

        return promedio_final
#--------------------------
#17

def calcular_max_min_cantidad(lista:list,dato:str,max_min:bool) -> None:
        """
        Calcular maximo y minimo de la cantidad de datos que no esten dentro de estadisticas pero si dentro de otra lista


        Arg:
                lista(list):Lista de jugadores
                dato:(str):dato a buscar
                max_min(bool): Dato booleano, Maximo para encontrar el mayor, y False para encontrar el minimo
        Returns: 
                nombre_mas_alto(str):Nombre del jugador con el dato mas alto de todos en caso de que se use True en el booleano
                nombre_mas_bajo(str):Nombre del jugador con el dato mas bajo de todos en caso de que se use False en el booleano
        """

        valor_mas_alto = None
        valor_mas_bajo = None

    
        for jugador in lista:
                if(max_min == True):
                        valor = len(jugador[dato])
                        if valor_mas_alto == None or valor > valor_mas_alto:
                                valor_mas_alto = valor
                                nombre_mas_alto = jugador["nombre"]
                else:
                        valor = jugador[dato]
                        if valor_mas_alto == None or valor < valor_mas_bajo:
                                valor_mas_bajo = valor
                                nombre_mas_bajo = jugador["nombre"]
        

        if(max_min==True):
                return nombre_mas_alto
        else:
                return nombre_mas_bajo
#--------------------------------------------
#20

def ordenar_por_posicion_en_cancha (lista:list) -> list:
        """
        Se ordenan los jugadores y se van ingresando a una lista de a uno, 
        hasta que todas las posiciones son recorridas(base, escolta, alero, ala-pivo y pivot)

        Arg:
                lista(list):Lista de jugadores
        Returns: 

                lista_aux(lista):Lista ordenada de los jugadores
        """
        lista_aux = []
        contador_posicion = 0
        
        while True:
                contador_jugadores = 0
                for jugadores in lista:
                
                        if(contador_posicion == 0):

                                contador_jugadores +=1

                                if(jugadores["posicion"] == "Base"):

                                        lista_aux.append(jugadores)


                                if(contador_jugadores == len(lista)):

                                        contador_posicion+=1

                        elif(contador_posicion == 1):

                                contador_jugadores +=1

                                if(jugadores["posicion"] == "Escolta"):

                                        lista_aux.append(jugadores)

                                if(contador_jugadores == len(lista)):

                                        contador_posicion+=1

                        elif(contador_posicion == 2):

                                contador_jugadores +=1

                                if(jugadores["posicion"] == "Alero"):

                                        lista_aux.append(jugadores)

                                if(contador_jugadores == len(lista)):

                                        contador_posicion+=1
                        elif(contador_posicion == 3):

                                contador_jugadores +=1

                                if(jugadores["posicion"] == "Ala-Pivot"):

                                        lista_aux.append(jugadores)

                                if(contador_jugadores == len(lista)):

                                        contador_posicion+=1
                        elif(contador_posicion == 4):

                                contador_jugadores +=1

                                if(jugadores["posicion"] == "Pivot"):

                                        lista_aux.append(jugadores)

                                if(contador_jugadores == len(lista)):

                                        contador_posicion+=1
                if(contador_posicion==5):
                        return lista_aux
                

#----------------------------------------------------

def aplicacion(lista:list[dict])->None:

        pasar_por_el_2 = False
        while(True):
                
                menu()
                opcion_elegida = input("\nIngrese la opción deseada: ")
                opcion = validar_numeros(opcion_elegida, r'^[1-9]$|^1[0-9]$|^20$|^21$')
        


                if opcion == "1":
                        mostrar_jugadores(lista_jugadores)
                elif opcion == "2":
                        indice_jugador = input ("Ingrese el numero de jugador a buscar: ")

                        cantidad_jugadores = len(lista_jugadores)
                        
                        indice_jugador = validar_numeros(indice_jugador,r'^[0-9]+$') 

                        if(indice_jugador== "-1"):
                                print("Porfavor ingresar un numero")
                        else:
                                indice_jugador = int(indice_jugador)
                                if(indice_jugador<=cantidad_jugadores-1 and indice_jugador>=0):
                                        pasar_por_el_2 = True
                                        mostrar_jugador_estadisticas(lista_jugadores,indice_jugador)
                                        
                                else:
                                       print("Porfavor ingreasar otro numero, no se aceptan numeros mayor o iguales a {0}".format(cantidad_jugadores))
                                
                elif opcion == "3":
                        if(pasar_por_el_2==True):
                                crear_csv_2(PATH,lista_jugadores,indice_jugador)
                        else:
                                print("Para ingresar a este punto primero debes ingresar un usuario en el punto numero 2")

                elif opcion == "4":

                        nombre = input("Porfavor ingrese el nombre del jugador a buscar: ")
                        nombre = nombre.capitalize() 
                        mostrar_jugador_por_nombre(lista,nombre)

                elif opcion == "5":

                        promedio = calcular_promedio(lista_jugadores,'promedio_puntos_por_partido')

                        lista_jugadores_ordenada = calcular_mayor_equipo(lista_jugadores,"nombre")

                        print("Promedio del equipo: {0}".format(promedio))

                        for jugador in lista_jugadores_ordenada:

                                print("{0}: {1}".format(jugador['nombre'],jugador['estadisticas']['promedio_puntos_por_partido']))


                elif opcion == "6":
                        nombre = input("Porfavor ingrese el nombre del jugador a buscar: ")
                        nombre = nombre.capitalize() 
                        verificar_salon_de_la_fama(lista,nombre)

                elif opcion == "7": 
                        print("{0} Es el jugador con mayor porcentaje de Rebotes Totales".format(calcular_max_min(lista,"rebotes_totales",True)))
                elif opcion == "8": 
                        print("{0} Es el jugador con mayor porcentaje de Asistencias Totales".format(calcular_max_min(lista,"asistencias_totales",True)))
                elif opcion == "9": 
                        print("{0} Es el jugador con mayor porcentaje de Tiros de Campo".format(calcular_max_min(lista,"porcentaje_tiros_de_campo",True)))
                elif opcion == "10": 

                        numero = input("Porfavor, Ingrese el numero para elegir el promedio mayor")
                        numero = validar_numeros(numero,r'^[0-9]+$')
                        numero = int(numero)
                        if(numero != -1):
                                promedio_mayor_a(lista_jugadores,numero,"promedio_puntos_por_partido")
                        else:
                                print("Porfavor ingrese un numero")


                elif opcion == "11": 
                        numero = input("Porfavor, Ingrese el numero para elegir el promedio mayor")
                        numero = validar_numeros(numero,r'^[0-9]+$')
                        numero = int(numero)
                        if(numero != -1):
                                promedio_mayor_a(lista_jugadores,numero,"promedio_rebotes_por_partido")
                        else:
                                print("Porfavor ingrese un numero")


                elif opcion == "12": 
                        numero = input("Porfavor, Ingrese el numero para elegir el promedio mayor")
                        numero = validar_numeros(numero,r'^[0-9]+$')
                        numero = int(numero)
                        if(numero != -1):
                                promedio_mayor_a(lista_jugadores,numero,"promedio_asistencias_por_partido")
                        else:
                                print("Porfavor ingrese un numero")


                elif opcion == "13": 
                        print("{0} Es el jugador con mayor cantidad de Robos Totales".format(calcular_max_min(lista,"rebos_totales",True)))
                elif opcion == "14": 
                        print("{0} Es el jugador con cantidad de Bloqueos Totales".format(calcular_max_min(lista,"bloqueos_totales",True)))
                elif opcion == "15": 

                        numero = input("Porfavor, Ingrese el numero para elegir el promedio mayor")
                        numero = validar_numeros(numero,r'^[0-9]+$')
                        numero = int(numero)
                        if(numero != -1):
                                promedio_mayor_a(lista_jugadores,numero,"porcentaje_tiros_libres")
                        else:
                                print("Porfavor ingrese un numero")
                elif opcion == "16": 
                        print(promedio_sin_el_ultimo(lista_jugadores,"promedio_puntos_por_partido"))
                elif opcion == "17": 
                        print("El jugador con mas logros es {0}".format(calcular_max_min_cantidad(lista_jugadores,"logros",True)))
                elif opcion == "18": 

                        numero = input("Porfavor, Ingrese el numero para elegir el promedio mayor")
                        numero = validar_numeros(numero,r'^[0-9]+$')
                        numero = int(numero)
                        if(numero != -1):
                                promedio_mayor_a(lista_jugadores,numero,"porcentaje_tiros_triples")
                        else:
                                print("Porfavor ingrese un numero")

                elif opcion == "19": 
                        print("{0} Es el jugador con mayor cantidad de Temporadas jugadas fue: ".format(calcular_max_min(lista,"temporadas",True)))
                elif opcion == "20":   

                        numero = input("Porfavor, Ingrese el numero para elegir el promedio mayor")
                        numero = validar_numeros(numero,r'^[0-9]+$')
                        numero = int(numero)
                        if(numero != -1):
                                lista_jugadores_ordenada_por_posicion = ordenar_por_posicion_en_cancha(lista_jugadores)
                                promedio_mayor_a(lista_jugadores_ordenada_por_posicion,numero,"porcentaje_tiros_de_campo")
                        else:
                                print("Porfavor ingrese un numero")

                elif opcion == "21": 
                        pass
                elif opcion == "22": 
                        pass
                elif opcion == "23": 
                        pass

                elif opcion == "-1":
                        print("Porfavor ingrese un numero del 0-7")
                
aplicacion(lista_jugadores)



