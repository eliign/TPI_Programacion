import os

RUTA_CSV = os.path.join(os.path.dirname(__file__), "paises.csv")


# -------------------------------
# FUNCIONES
# -------------------------------

def menu_principal():
    print("*************************************")
    print("\nMenú principal\n")
    try:
        opcion = int(input(
            "1- Agregar nuevo país\n"
            "2- Actualizar población y superficie\n"
            "3- Buscar un país\n"
            "4- Filtrar países\n"
            "5- Ordenar países\n"
            "6- Mostrar estadísticas generales\n"
            "7- Salir del programa\n"
            "👉 Opción: "
        ).strip())
        print("\n*************************************\n")
        return opcion  # Si todo sale bien, devuelvo la opción
    
    except ValueError:
        # Si el usuario escribe algo que NO es número (ej: "hola")
        print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print("🚩 ERROR: Ingresá una opción numérica.")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n") 
        return None  # Devuelvo None para indicar que la entrada fue inválida
    
    # Por si existe un error no contemplado:
    except Exception as error:
        print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print("⚠️  Se produjo un error inesperado: ", type(error).__name__ )
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
        return None

def cargar_datos_csv(RUTA_CSV):
    """
    Tarea 1: Leer el archivo CSV y carga los países en una lista de diccionarios.
    """
    lista_paises = []
    
    # Validamos si el archivo realmente existe en la carpeta para evitar que el programa se rompa
    if not os.path.exists(RUTA_CSV):
        print(f"Error: No se encontró el archivo '{RUTA_CSV}' en esta carpeta.")
        return lista_paises

    with open(RUTA_CSV, 'r', encoding='utf-8') as archivo:
        # Descartamos la primera línea de encabezados
        archivo.readline()
        
        for linea in archivo:
            # Limpiamos espacios y separamos por comas
            datos = linea.strip().split(',')
            
            # Control de formato: Aseguramos que la línea tenga exactamente 4 datos
            if len(datos) == 4:
                try:
                    nuevo_pais = {
                        "nombre": datos[0].strip(),
                        "poblacion": int(datos[1].strip()),   # Conversión obligatoria a entero
                        "superficie": int(datos[2].strip()),  # Conversión obligatoria a entero
                        "continente": datos[3].strip()
                    }
                    lista_paises.append(nuevo_pais)
                except ValueError:
                    # Si población o superficie no son números, salta este registro sin romper el programa
                    print(f"Error de formato en la línea: {linea.strip()} (Datos numéricos inválidos)")
                    
    print(f"Se cargaron correctamente {len(lista_paises)} países.")
    return lista_paises

def guardar_datos_csv(RUTA_CSV, lista_paises):
    try:
        with open(RUTA_CSV, "w", encoding="utf-8") as archivo:
            
            # Encabezado
            archivo.write("nombre,poblacion,superficie,continente\n")
            
            # Datos
            for pais in lista_paises:
                linea = f"{pais['nombre']},{pais['poblacion']},{pais['superficie']},{pais['continente']}\n"
                archivo.write(linea)

        print("    💾 Datos guardados correctamente en el CSV")

    except Exception as error:
        print(f"🚨 Error al guardar el archivo: {type(error).__name__}")

def ingresar_pais_continente(mensaje):
    while True:
        
        try:
            pais_continente = input(mensaje).strip().title()

            if pais_continente == "":
                raise ValueError("No se permiten campos vacíos")
            elif pais_continente.isdigit(): 
                raise ValueError("No se permiten números en este campo")
            else:
                return pais_continente

        except ValueError as error:
            print(f"   🚨 ERROR: {error}\n")

def ingresar_poblacion_superficie(mensaje):
    while True:
        try:
            pob_sup = int(input(mensaje).strip())
            # Comprueba que el número no sea menor a cero:
            if pob_sup < 0:
                print("   🚨 ERROR: El número no puede ser negativo.\n")
                continue
            else:
                return pob_sup # si es distinto, devuelvo el nro
        except ValueError:
            print("   🚨 ERROR: Ingresá un número entero.\n")

def agregar_pais(lista_paises, nombre, poblacion, superficie, continente):
    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    lista_paises.append(nuevo_pais)

def actualizar_poblacion_superficie(lista_paises):
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
    
    if not pais_encontrado: # Si no se encuentra, se le avisa al usuario
        print("🚨    No se encontró el país")

def buscar_pais(lista_paises):
    pais_buscado = ingresar_pais_continente(" - Nombre del país: ")
    pais_encontrado = False
    

    for pais in lista_paises: #recorro cada diccionario
        
        if pais_buscado.lower() in pais["nombre"].lower(): # compruebo si algo de lo ingresado en pais_buscado coincide con algún valor de la key nombre. Ej: arg --> argentina | tina --> argentina
            pais_encontrado = True # Si encuentra coincidencias, cambio la bandera
            print(f"    👥 Población: {pais['poblacion']}")
            print(f"    📏 Superficie: {pais['superficie']} km²")
            print(f"    🌍 Continente: {pais['continente']}")
            print()
        
    if not pais_encontrado:
        print("No se encontraron países.")


# ------------------------------------------------------------------
# NUEVAS FUNCIONES 
# ------------------------------------------------------------------

def filtrar_por_continente(lista_paises):
    continente_buscado = input(" - Ingrese el continente a filtrar: ").strip()
    
    print(f"\n Países en el continente: {continente_buscado}")
    for pais in lista_paises:
        if pais["continente"].lower() == continente_buscado.lower():
            print(f"- {pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']}")


def filtrar_por_rango_poblacion(lista_paises):
    print(" - Ingresá el rango de población:")
    #el usuario podría meter letras o un mínimo mayor al máximo y rompería el flujo.
    minimo = int(input("   Población mínima: "))
    maximo = int(input("   Población máxima: "))

    print(f"\n Países con población entre {minimo} y {maximo} hab.")
    for pais in lista_paises:
        if minimo <= pais["poblacion"] <= maximo:
            print(f"- {pais['nombre']} ({pais['poblacion']} hab.)")


def filtrar_por_rango_superficie(lista_paises):
    print(" - Ingresá el rango de superficie (en km²):")
    #falta usar funciones de validación seguras.
    minimo = int(input("   Superficie mínima (km²): "))
    maximo = int(input("   Superficie máxima (km²): "))

    print(f"\n Países con superficie entre {minimo} y {maximo} km²")
    for pais in lista_paises:
        if minimo <= pais["superficie"] <= maximo:
            print(f"- {pais['nombre']} ({pais['superficie']} km²)")


def ordenar_paises(lista_paises, criterio, ascendente=True):
    # Algoritmo Bubble Sort para ordenar
    lista_ordenada = lista_paises.copy()
    n = len(lista_ordenada)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if ascendente:
                if lista_ordenada[j][criterio] > lista_ordenada[j + 1][criterio]:
                    lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]
            else:
                if lista_ordenada[j][criterio] < lista_ordenada[j + 1][criterio]:
                    lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]
                    
    return lista_ordenada


def mostrar_estadisticas(lista_paises):
    # Si lista_paises llega a estar vacía = IndexError. Falta validarlo.
    pais_mayor_pob = lista_paises[0]
    pais_menor_pob = lista_paises[0]
    suma_poblacion = 0
    suma_superficie = 0
    conteo_continentes = {}

    for pais in lista_paises:
        suma_poblacion += pais["poblacion"]
        suma_superficie += pais["superficie"]

        if pais["poblacion"] > pais_mayor_pob["poblacion"]:
            pais_mayor_pob = pais

        if pais["poblacion"] < pais_menor_pob["poblacion"]:
            pais_menor_pob = pais

        continente = pais["continente"]
        if continente in conteo_continentes:
            conteo_continentes[continente] += 1
        else:
            conteo_continentes[continente] = 1

    promedio_pob = suma_poblacion / len(lista_paises)
    promedio_sup = suma_superficie / len(lista_paises)

    print("\n=== ESTADÍSTICAS DEL SISTEMA ===")
    print(f"País con mayor población: {pais_mayor_pob['nombre']}")
    print(f"País con menor población: {pais_menor_pob['nombre']}")
    print(f"Promedio de población: {promedio_pob:.2f}")
    print(f"Promedio de superficie: {promedio_sup:.2f}")
    print("Cantidad de países por continente:", conteo_continentes)


def mostrar_lista_paises(lista):
    for p in lista:
        print(f"{p['nombre']} | Población: {p['poblacion']} | Superficie: {p['superficie']} | Continente: {p['continente']}")


# -------------------------------
# VARIABLES
# -------------------------------

lista_paises = cargar_datos_csv(RUTA_CSV) # Dejo que la función cree la lista


# -------------------------------
# MAIN 
# -------------------------------

while True:

    # Inicio menú principal
    opcion = menu_principal() 
    # Si el usuario ingresó algo inválido, vuelvo a pedir que ingrese una opción válida:
    if opcion is None:
        continue
    # Fin menú principal

    # Inicio opción 1 --> Cargar herramienta
    if opcion == 1:
        # Opción de ingreso de nuevo país
        print(">>> 🌎 Agregar nuevo país <<<")
        nombre = ingresar_pais_continente(" - Nombre: ")
        poblacion = ingresar_poblacion_superficie(" - Población: ")
        superficie = ingresar_poblacion_superficie(" - Superficie (km²): ")
        continente = ingresar_pais_continente(" - Continente: ")

        agregar_pais(lista_paises, nombre, poblacion, superficie, continente) # Guarda la info en como diccionario en la lista
        guardar_datos_csv(RUTA_CSV, lista_paises)
        print()
    
    # Inicio opción 2 --> Actualizar los datos de Población y Superficie de un País.
    elif opcion == 2:
    # Opción para Actualizar los datos de Población y Superficie de un País.
        print(">>> ↔️  Actualizar los datos de Población y Superficie <<<")
        actualizar_poblacion_superficie(lista_paises)
        guardar_datos_csv(RUTA_CSV, lista_paises)
        print()

    # Inicio opción 3 --> Buscar país
    elif opcion == 3:
        # Opción para buscar un país
        print(">>> 🔍 Buscar un país <<<")
        buscar_pais(lista_paises)
        print()
        
    # Inicio opción 4 --> Filtrar países
    elif opcion == 4:
        print(">>> Filtrar países <<<")
        print("1. Por continente")
        print("2. Por rango de población")
        print("3. Por rango de superficie")
        #Falta validar que el input sea un número entre 1 y 3.
        sub_opcion = input(" Seleccione tipo de filtro (1-3): ").strip()

        if sub_opcion == "1":
            filtrar_por_continente(lista_paises)
        elif sub_opcion == "2":
            filtrar_por_rango_poblacion(lista_paises)
        elif sub_opcion == "3":
            filtrar_por_rango_superficie(lista_paises)
        else:
            print("Opción inválida.\n")
        
    # Inicio opción 5 --> Ordenar países
    elif opcion == 5:
        print(">>> Ordenar países <<<")
        print("1. Ordenar por Nombre")
        print("2. Ordenar por Población")
        print("3. Ordenar por Superficie")
        crit_opcion = input(" Seleccione criterio (1-3): ").strip()
        
        criterio = ""
        if crit_opcion == "1": criterio = "nombre"
        elif crit_opcion == "2": criterio = "poblacion"
        elif crit_opcion == "3": criterio = "superficie"
        
        if criterio != "":
            print("1. Ascendente")
            print("2. Descendente")
            sentido = input(" Seleccione sentido (1-2): ").strip()
            es_ascendente = (sentido == "1")
            
            paises_ordenados = ordenar_paises(lista_paises, criterio, es_ascendente)
            mostrar_lista_paises(paises_ordenados)
        else:
            print("Opción de ordenamiento inválida.\n")
            
    # Inicio opción 6 --> Mostrar Estadísticas
    elif opcion == 6:
        mostrar_estadisticas(lista_paises)
        
    # Inicio opción 7 --> Salir del programa
    elif opcion == 7:
        print("¡Gracias por usar el sistema! Saliendo y guardando datos...")
        guardar_datos_csv(RUTA_CSV, lista_paises)
        break
        
    else:
        print(" \n🚩 ERROR: Ingresá una opción dentro del rango (1 a 7) \n")
