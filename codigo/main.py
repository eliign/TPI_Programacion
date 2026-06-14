# -------------------------------
# MÓDULOS INTEGRADOS
# -------------------------------

from manejo_csv import (
    RUTA_CSV,
    cargar_datos_csv, 
    guardar_datos_csv
    )
from validaciones import (
    validar_lista_con_datos,
    ingresar_pais_continente, 
    ingresar_poblacion_superficie
    )
from operaciones import (
    alta_pais,
    actualizar_poblacion_superficie,
    buscar_pais,
    menu_filtrar_paises,
    opcion_filtrar,
    filtrar_por_continente,
    filtrar_por_poblacion_superficie,
    menu_ordenamiento,
    mostrar_estadisticas,
)


# -------------------------------
# FUNCIONES GENERALES
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
        print("\n❌ Debés ingresar un número.\n")
        return None
    except Exception as error:
        print(f"⚠️ Error inesperado: {type(error).__name__}")
        return None


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

    # Inicio opción 1 --> ingreso de nuevo país
    if opcion == 1:
        alta_pais(lista_paises, RUTA_CSV)
    
    # Inicio opción 2 --> Actualizar los datos de Población y Superficie de un País.
    elif opcion == 2:
        # Primero se corrobora que la lista tenga datos
        if not validar_lista_con_datos(lista_paises):
            continue

        print(">>> ↔️  Actualizar los datos de Población y Superficie <<<")
        if actualizar_poblacion_superficie(lista_paises):
            guardar_datos_csv(RUTA_CSV, lista_paises)
        print()

    # Inicio opción 3 --> Buscar país
    elif opcion == 3:
        # Opción para buscar un país
        # Primero se corrobora que la lista tenga datos
        if not validar_lista_con_datos(lista_paises):
            continue
        print(">>> 🔍 Buscar un país <<<")
        buscar_pais(lista_paises)
        print()
        
    # Inicio opción 4 --> Filtrar países
    elif opcion == 4:

        # Primero se corrobora que la lista tenga datos
        if not validar_lista_con_datos(lista_paises):
            continue

        opcion_filtrar(lista_paises)
        
    # Inicio opción 5 --> Ordenar países
    elif opcion == 5:
        # Primero se corrobora que la lista tenga datos
        if not validar_lista_con_datos(lista_paises):
            continue
        menu_ordenamiento(lista_paises)

    # Inicio opción 6 --> Mostrar Estadísticas
    elif opcion == 6:
        # Primero se corrobora que la lista tenga datos
        if not validar_lista_con_datos(lista_paises):
            continue
        mostrar_estadisticas(lista_paises)
        
    # Inicio opción 7 --> Salir del programa
    elif opcion == 7:
        print("¡Gracias por usar el sistema! Saliendo y guardando datos...")
        guardar_datos_csv(RUTA_CSV, lista_paises)
        break
        
    else:
        print("🚩 ERROR: Ingresá una opción dentro del rango (1 a 7) \n")
