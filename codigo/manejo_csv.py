# Módulo de CSV --> Cargar datos del CVS + Guardar datos en el CVS

import os

RUTA_CSV = os.path.join(os.path.dirname(__file__), "paises.csv")


def cargar_datos_csv(RUTA_CSV):
    # Lee el archivo CSV y carga los países en una lista de diccionarios.
    lista_paises = []
    
    # Valido si el archivo realmente existe en la carpeta para evitar que el programa se rompa
    if not os.path.exists(RUTA_CSV):
        print(f"🚨 Error: No se encontró el archivo '{RUTA_CSV}' en esta carpeta.")
        return lista_paises

    try:
        # Intento abrir el archivo para capturar posibles errores de lectura
        with open(RUTA_CSV, 'r', encoding='utf-8') as archivo:

            # Descarto la primera línea de encabezados
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
                        print(f"🚨 Error de formato en la línea: {linea.strip()} (Datos numéricos inválidos)")

    except PermissionError:
        print("🚨 No tenés permisos para acceder al archivo.")

    except Exception as error:
        print(f"🚨 Error al leer el archivo: {type(error).__name__}")

    return lista_paises

def guardar_datos_csv(RUTA_CSV, lista_paises):
    # Guarda los datos en el archivo .csv
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
        print(f"    🚨 Error al guardar el archivo: {type(error).__name__}")
