# Módulo para operaciones de las opciones

from validaciones import ingresar_pais_continente, ingresar_poblacion_superficie
from manejo_csv import guardar_datos_csv

# -------------------------------
# FUNCIONES PARA OPCIONES
# -------------------------------

# Inicio opción 1:
def existe_pais(lista_paises, nombre):
    # Verifica si un país ya existe en la lista
    for pais in lista_paises:
        if pais["nombre"].lower() == nombre.lower():
            return True

    return False

def agregar_pais(lista_paises, nombre, poblacion, superficie, continente):
    # Agrega un nuevo país a la lista

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente}

    lista_paises.append(nuevo_pais)

def alta_pais(lista_paises, ruta_csv):
    # Solicita los datos y registra un nuevo país

    print(">>> 🌎 Agregar nuevo país <<<")

    nombre = ingresar_pais_continente(" - Nombre: ")

    # Verifica si el país ya existe
    if existe_pais(lista_paises, nombre):
        print("    🚨 El país ya se encuentra registrado.\n")
        return

    # Si no existe:
    poblacion = ingresar_poblacion_superficie(" - Población: ")
    superficie = ingresar_poblacion_superficie(" - Superficie (km²): ")
    continente = ingresar_pais_continente(" - Continente: ")

    agregar_pais(lista_paises, nombre, poblacion, superficie, continente)

    guardar_datos_csv(ruta_csv, lista_paises)
# Fin opción 1


# Inicio opción 2:
def actualizar_poblacion_superficie(lista_paises):
    # Función para cambiar la superficie o población:

    nombre = ingresar_pais_continente(" - Nombre del país: ")
    pais_encontrado = False 

    for pais in lista_paises: #recorro cada diccionario
        if nombre.lower() == pais["nombre"].lower():
            nueva_poblacion = ingresar_poblacion_superficie(" - Nueva población: ")
            nueva_superficie = ingresar_poblacion_superficie(" - Nueva superficie: ")

            # Asigno los nuevos valores a las keys correspondientes:
            pais["poblacion"] = nueva_poblacion
            pais["superficie"] = nueva_superficie

            pais_encontrado = True # Si el país se encuentra, cambio la bandera a true
            break # salgo del for
    
    if not pais_encontrado: # Si no lo encuentra, le avisa al usuario
        print("    🚨No se encontró el país")
        return False
    return True
# Fin opción 2:


# Inicio opción 3:
def buscar_pais(lista_paises):
    # Función para buscar un país en la lista

    pais_buscado = ingresar_pais_continente(" - Nombre del país: ")
    print()
    pais_encontrado = False
    
    for pais in lista_paises: #recorro cada diccionario
        
        if pais_buscado.lower() in pais["nombre"].lower(): # compruebo si algo de lo ingresado en pais_buscado coincide con algún valor de la key nombre. Ej: arg --> argentina | tina --> argentina
            pais_encontrado = True # Si encuentra coincidencias, cambio la bandera
            print(f"    📍 País: {pais['nombre']}")
            print(f"    👥 Población: {pais['poblacion']}")
            print(f"    📏 Superficie: {pais['superficie']} km²")
            print(f"    🌍 Continente: {pais['continente']}")
            print()
        
    if not pais_encontrado:
        print("    🚨 El país ingresado no fue encontrado.")
# Fin opción 3:


# INICIO OPCIÓN 4:
def filtrar_por_continente(lista_paises, continente):
    # Función para filtrar por continente
    continente_encontrado = False

    for pais in lista_paises:

        if pais["continente"].lower() == continente.lower():

            # Imprime el encabezado solo la primera vez
            if not continente_encontrado:
                print("-" * 70)
                print(f"{'PAÍS':<20} {'POBLACIÓN':<15} {'SUPERFICIE':<15} {'CONTINENTE'}")
                print("-" * 70)

                continente_encontrado = True

            print(
                f"{pais['nombre']:<20} "
                f"{pais['poblacion']:<15} "
                f"{pais['superficie']:<15} "
                f"{pais['continente']}"
            )

    if continente_encontrado:
        print("-" * 70)
        print()
    else:
        print("     🚨 El continente ingresado no existe.")

def filtrar_por_poblacion_superficie(lista_paises, valor_minimo, valor_maximo, nombre_clave, titulo_resultado, unidad_medida):
    # Función para filtrar por población/superficie
    coincidencias_encontradas = False

    print(titulo_resultado)

    # Recorre todos los países de la lista
    for pais in lista_paises:

        if valor_minimo <= pais[nombre_clave] <= valor_maximo:

            if not coincidencias_encontradas: # Imprime el encabezado solo la primera vez que encuentra un resultado
                print("-" * 90)
                print(f"{'PAÍS':<20} {'VALOR':<20}")
                print("-" * 90)

                coincidencias_encontradas = True

            print(f"{pais['nombre']:<20} {str(pais[nombre_clave]) + ' ' + unidad_medida}")

    if coincidencias_encontradas:
        print("-" * 90)
        print()
    else:
        print("    🚨 No se encontraron países para ese rango.")

def menu_filtrar_paises():

    while True:
        try:
            print(">>> Formas de filtrado <<<")
            opcion = int(input(
                "1- Por continente\n"
                "2- Por rango de población\n"
                "3- Por rango de superficie\n"
                "👉 Opción: ").strip())
            print()

            if opcion not in (1, 2, 3):
                print("❌ Opción inválida. Debe ser 1, 2 o 3.\n")
                continue

            return opcion

        except ValueError:
            print("❌ Debés ingresar un número.\n")

        except Exception as error:
            print(f"⚠️ Error inesperado: {type(error).__name__}")

def opcion_filtrar(lista_paises):
    op_menu_filtrar = menu_filtrar_paises()

    if op_menu_filtrar == 1:
        continente_buscado = ingresar_pais_continente(f"🔵 Ingresá el continente: ")
        filtrar_por_continente(lista_paises, continente_buscado)
        print()

    elif op_menu_filtrar == 2:
        print("🔵 Ingresá el rango de población:")
        poblacion_minima = ingresar_poblacion_superficie(f"   - Población mínima: ")
        poblacion_maxima = ingresar_poblacion_superficie(f"   - Población máxima: ")

        if poblacion_minima > poblacion_maxima:
            print("\n   🚨 La población mínima no puede ser mayor que la máxima.")
        else:
            filtrar_por_poblacion_superficie(
            lista_paises,
            poblacion_minima,
            poblacion_maxima,
            "poblacion",
            f"\n👤 Países con población entre {poblacion_minima} y {poblacion_maxima} hab:",
            "hab.")
        print()

    elif op_menu_filtrar == 3:
        print("🔵 Ingresá el rango de superficie (en km²):")
        superficie_minima = ingresar_poblacion_superficie(f"   - Superficie mínima: ")
        superficie_maxima = ingresar_poblacion_superficie(f"   - Superficie máxima: ")

        if superficie_minima > superficie_maxima:
            print("\n   🚨 La superficie mínima no puede ser mayor que la máxima.")
        else:
            filtrar_por_poblacion_superficie(
            lista_paises,
            superficie_minima,
            superficie_maxima,
            "superficie",
            f"\n🌍 Países con superficie entre {superficie_minima} y {superficie_maxima} km²:",
            "km².")
        print()
    else:
        print("🚩 ERROR: Ingresá una opción dentro del rango (1 a 3) \n")
# FIN OPCIÓN 4


# INICIO OPCIÓN 5:
def ordenar_paises(lista_paises, criterio, ascendente=True):
    #ascendente: True = menor a mayor, False = mayor a menor


    # Copia para no modificar la lista original
    lista_ordenada = lista_paises.copy()

    cantidad_paises = len(lista_ordenada)

    # Recorro la lista
    for vuelta in range(cantidad_paises):

        # Comparo países vecinos
        for posicion in range(0, cantidad_paises - vuelta - 1):

            pais_actual = lista_ordenada[posicion]
            pais_siguiente = lista_ordenada[posicion + 1]

            valor_actual = pais_actual[criterio]
            valor_siguiente = pais_siguiente[criterio]

            # Orden ascendente
            if ascendente: # Si es True
                if valor_actual > valor_siguiente:
                    lista_ordenada[posicion], lista_ordenada[posicion + 1] = (
                        pais_siguiente,
                        pais_actual,
                    )

            # Orden descendente
            else: # Si es false
                if valor_actual < valor_siguiente:
                    lista_ordenada[posicion], lista_ordenada[posicion + 1] = (
                        pais_siguiente,
                        pais_actual,
                    )

    return lista_ordenada

def menu_ordenamiento(lista_paises):

    # Opción del menú: ordenar países
    print(">>> Ordenar países <<<")
    while True:
        try:
            opcion_ordenar = int(input(
                "1- Por nombre\n"
                "2- Por población\n"
                "3- Por superficie\n"
                "👉 Opción: ").strip())
            print()

            # Validación de rango
            if opcion_ordenar not in (1, 2, 3):
                print("    ❌ Opción inválida. Debe ser 1, 2 o 3.\n")
                continue

            break  # solo sale si es válido

        except ValueError:
            print("    ❌ Debés ingresar un número.\n")
            continue
        except Exception as error:
            print(f"    ⚠️ Error inesperado: {type(error).__name__}")

    # Se traduce la opción del usuario a la clave del diccionario
    if opcion_ordenar == 1:
        campo_orden = "nombre"
    elif opcion_ordenar == 2:
        campo_orden = "poblacion"
    elif opcion_ordenar == 3:
        campo_orden = "superficie"
    else:
        print("❌ Opción fuera de rango")
        return

    # Si el criterio es válido, se continúa con el ordenamiento
    # Se muestra opción de orden ascendente o descendente
    while True:
        try:
            opcion_sentido = int(input(
                "   Elije el orden:\n"
                "   1- Ascendente\n"
                "   2- Descendente\n"
                "   👉 Opción: ").strip())
            print()

            # Validación de rango
            if opcion_sentido not in (1, 2):
                print("    ❌ Opción inválida. Debe ser 1 o 2.\n")
                continue 

            break  # solo salimos si está bien

        except ValueError:
            print("\n    ❌ Debés ingresar un número.\n")
            continue

    # Si el usuario elige 1 → ascendente (True), si no → descendente (False)
    es_ascendente = (opcion_sentido == 1)

    paises_ordenados = ordenar_paises(lista_paises, campo_orden, es_ascendente)

    # Se muestra la lista ordenada
    mostrar_lista_paises(paises_ordenados, campo_orden)

def mostrar_lista_paises(lista, campo_orden):
    # Depende como la persona desee ordenar, será el orden en el que se imprimirá la tabla
    print("-" * 70)

    # Si está ordenado por nombre
    if campo_orden == "nombre":
        print(f"{'PAÍS':<20} {'POBLACIÓN':<15} {'SUPERFICIE':<15} {'CONTINENTE'}")
        print("-" * 70)

        for pais in lista:
            print(f"{pais['nombre']:<20} {pais['poblacion']:<15} {pais['superficie']:<15} {pais['continente']}")

    # Si está ordenado por población
    elif campo_orden == "poblacion":
        print(f"{'POBLACIÓN':<15} {'PAÍS':<20} {'SUPERFICIE':<15} {'CONTINENTE'}")
        print("-" * 70)

        for pais in lista:
            print(f"{pais['poblacion']:<15} {pais['nombre']:<20} {pais['superficie']:<15} {pais['continente']}")

    # Si está ordenado por superficie
    elif campo_orden == "superficie":
        print(f"{'SUPERFICIE':<15} {'PAÍS':<20} {'POBLACIÓN':<15} {'CONTINENTE'}")
        print("-" * 70)

        for pais in lista:
            print(f"{pais['superficie']:<15} {pais['nombre']:<20} {pais['poblacion']:<15} {pais['continente']}")

    #<20 y <15 --> Lo traduzco como: mostrá el texto ocupando 20/15 espacios hacia la izquierda
    print("-" * 70)
    print()
# FIN OPCIÓN 5:


# INICIO OPCIÓN 6:
def mostrar_estadisticas(lista_paises):

    # Verifico que la lista no esté vacía
    if not lista_paises:
        print("❌ No hay países cargados para mostrar estadísticas.\n")
        return
    
    pais_mayor_pob = lista_paises[0]
    pais_menor_pob = lista_paises[0]
    suma_poblacion = 0
    suma_superficie = 0
    conteo_continentes = {}

    # Recorro la lista:
    for pais in lista_paises:

        # Acumuladores
        suma_poblacion += pais["poblacion"]
        suma_superficie += pais["superficie"]

        # Mayor población
        if pais["poblacion"] > pais_mayor_pob["poblacion"]:
            pais_mayor_pob = pais

        # Menor población
        if pais["poblacion"] < pais_menor_pob["poblacion"]:
            pais_menor_pob = pais

        # Conteo por continente
        continente = pais["continente"]

        if continente in conteo_continentes: # si se encuentra, sumo 
            conteo_continentes[continente] += 1
        else:
            conteo_continentes[continente] = 1

    # Cálculo de promedios
    promedio_poblacion = suma_poblacion / len(lista_paises)
    promedio_superficie = suma_superficie / len(lista_paises)

    print("🟢 ESTADÍSTICAS DEL SISTEMA")
    print()
    print(f"    🌍 País con mayor población: {pais_mayor_pob['nombre']}")
    print(f"    🌎 País con menor población: {pais_menor_pob['nombre']}")
    print(f"    📈 Promedio de población: {promedio_poblacion:.2f}")
    print(f"    📉 Promedio de superficie: {promedio_superficie:.2f}")

    print()

    #Encabezado de la tabla
    print("🗺️  Cantidad de países por continente: \n")
    print("-" * 40)
    print(f"    {'CONTINENTE':<20} {'CANTIDAD':<15}")
    print("-" * 40)

    for continente in conteo_continentes:
        cantidad = conteo_continentes[continente]
        print(f"    {continente:<23} {cantidad}")
    
    print("-" * 40)
    print()
# FIN OPCIÓN 6:
