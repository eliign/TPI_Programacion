# 🌍 Gestión de Datos de Países en Python

**Trabajo Práctico Integrador — Programación 1**
**Tecnicatura Universitaria en Programación | UTN – TUPaD**

---

## 📋 Descripción

Sistema de gestión de información sobre países desarrollado en Python. Permite cargar datos desde un archivo CSV y realizar operaciones de consulta, filtrado, ordenamiento y estadísticas desde un menú interactivo en consola.

---

## 👥 Integrantes

| Nombre | 
|---|---|
| Calzada Candela Estefania | 
| Garmendia Ruete Faustina Elisa | 
---

## 🗂️ Estructura del proyecto

```
📁 TPI_Programacion/
├── main.py            # Punto de entrada · menú principal y loop
├── operaciones.py     # Lógica de las 6 opciones del menú
├── manejo_csv.py      # Carga y guardado del archivo CSV
├── validaciones.py    # Validaciones de entrada y manejo de errores
├── paises.csv         # Dataset base con países precargados
└── README.md
```

---

## ▶️ Instrucciones de uso

**Requisitos:** Python 3.x (sin librerías externas)

```bash
# Clonar el repositorio
git clone https://github.com/eliign/TPI_Programacion

# Entrar a la carpeta
cd TPI_Programacion

# Ejecutar
python main.py
```

> ⚠️ Todos los archivos `.py` y el `paises.csv` deben estar en la misma carpeta.

---

## 🧭 Menú del sistema

```
1- Agregar nuevo país
2- Actualizar población y superficie
3- Buscar un país
4- Filtrar países
5- Ordenar países
6- Mostrar estadísticas generales
7- Salir del programa
```

---

## 💡 Ejemplos de uso

### Agregar un país
```
>>> 🌎 Agregar nuevo país <<<
 - Nombre: Francia
 - Población: 68400000
 - Superficie (km²): 551695
 - Continente: Europa
    💾 Datos guardados correctamente en el CSV
```

### Buscar un país (coincidencia parcial)
```
>>> 🔍 Buscar un país <<<
 - Nombre del país: arg

    📍 País: Argentina
    👥 Población: 45376763
    📏 Superficie: 2780400 km²
    🌍 Continente: América
```

### Filtrar por rango de población
```
🔵 Ingresá el rango de población:
   - Población mínima: 50000000
   - Población máxima: 200000000

👤 Países con población entre 50000000 y 200000000 hab:
------------------------------------------------------------------------------------------
PAÍS                 VALOR               
------------------------------------------------------------------------------------------
Japón                125800000 hab.
Alemania             83149300 hab.
```

### Ordenar por superficie descendente
```
SUPERFICIE      PAÍS                 POBLACIÓN       CONTINENTE
----------------------------------------------------------------------
8515767         Brasil               213993437       América
2780400         Argentina            45376763        América
...
```

### Estadísticas
```
🟢 ESTADÍSTICAS DEL SISTEMA

    🌍 País con mayor población: China
    🌎 País con menor población: Nueva Zelanda
    📈 Promedio de población: 268695195.50
    📉 Promedio de superficie: 5924070.79

🗺️  Cantidad de países por continente:
----------------------------------------
    CONTINENTE           CANTIDAD       
----------------------------------------
    América                 4
    Asia                    3
    Europa                  3
    Oceanía                 2
    África                  2
----------------------------------------
```

---

## 🔒 Validaciones implementadas

- Campos de texto: no permite vacíos ni números en nombre/continente
- Campos numéricos: solo enteros no negativos
- Rango de filtros: mínimo no puede ser mayor que máximo
- País duplicado: no permite agregar un país ya registrado
- Lista vacía: avisa si se intenta operar sin datos cargados
- CSV con formato inválido: salta el registro sin interrumpir la carga

---

## 📄 Documentación

[📎 Informe técnico (PDF)] *(insertar link)*

---

## 🎥 Video demostración

[▶️ Ver video explicativo] *(insertar link)*

---

## 📦 Dataset base (`paises.csv`)

```
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Brasil,213993437,8515767,América
...
```
