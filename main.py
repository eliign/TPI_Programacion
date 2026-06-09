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
    # Fin opción 1 --> Cargar herramienta
    
    # Inicio opción 2 --> Actualizar los datos de Población y Superficie de un País.
    elif opcion == 2:
    # Opción para Actualizar los datos de Población y Superficie de un País.
        print(">>> ↔️  Actualizar los datos de Población y Superficie <<<")
        actualizar_poblacion_superficie(lista_paises)
        guardar_datos_csv(RUTA_CSV, lista_paises)
        print()
    # Fin opción 2 --> Actualizar los datos de Población y Superficie de un País.

    # Inicio opción 3 --> Buscar país
    elif opcion == 3:
        # Opción para buscar un país
        print(">>> 🔍 Buscar un país <<<")
        buscar_pais(lista_paises)
        print()
    # Fin opción 3 --> Buscar país
    
    else:
        print(" \n🚩 ERROR: Ingresá una opción dentro del rango.\n")


