# Módulo para validaciones


def validar_lista_con_datos(lista_paises):
    # valida que la lista tenga paises
    if len(lista_paises) == 0:
        print("🚨 Error: Aún no hay información cargada.")
        print("👉 Primero tenés que ingresar países desde la opción n° 1.\n")
        return False
    
    return True

def tiene_numero(texto):
    # Recorre cada carácter del texto buscando dígitos
    for caracter in texto:
        if caracter.isdigit():
            return True  # Encontró un número y devuelve true
    return False  # No encontró ningún número

def ingresar_pais_continente(mensaje):
    # Para ingresar un input que contenga letras
    while True:
        
        try:
            pais_continente = input(mensaje).strip().title()

            if pais_continente == "":
                raise ValueError("No se permiten campos vacíos")
            elif tiene_numero(pais_continente): # Si el campo tiene un número, arroja error
                raise ValueError("No se permiten números en este campo")
            else:
                return pais_continente

        except ValueError as error:
            print(f"   🚨 ERROR: {error}\n")
        except Exception as error:
            print(f"⚠️ Error inesperado: {type(error).__name__}")
            continue

def ingresar_poblacion_superficie(mensaje):
    # Para ingresar un input que contenga números
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
        
        except Exception as error:
            print(f"⚠️ Error inesperado: {type(error).__name__}")
            continue
