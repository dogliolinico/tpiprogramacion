# Sistema de Gestión de Países
Trabajo Práctico Integrador — Programación I | UTN
Repositorio
https://github.com/dogliolinico/tpiprogramacion
Video de presentación
https://youtu.be/BwJre1pwz3Q

Informe
tpiprogramacion.pdf

Descripción
Aplicación de consola en Python para administrar un dataset de países del mundo. Los datos se persisten automáticamente en un archivo CSV (paises.csv) al finalizar cada operación de escritura.
Estructura del proyecto
TPI/
├── tpi.py           # Lógica principal y menú del programa
├── funciones.py     # Funciones auxiliares (importadas en versiones anteriores)
├── paises.csv       # Base de datos en formato CSV
└── README.md

Requisitos
·	Python 3.x
·	No requiere librerías externas (solo módulos estándar: csv, os)
Cómo ejecutar
python tpi.py

Funcionalidades
Opción	Función
1	Agregar un nuevo país (nombre, población, superficie, continente)
2	Actualizar población o superficie de un país existente
3	Buscar país por nombre (coincidencia parcial)
4	Filtrar países por continente, rango de población o rango de superficie
5	Ordenar países por nombre, población o superficie (asc/desc)
6	Mostrar estadísticas: mayor/menor población, promedios y países por continente
7	Guardar y salir

Estructura de los datos
Cada país se almacena como un diccionario con los siguientes campos:
Campo	Tipo	Descripción
nombre	str	Nombre del país
poblacion	int	Cantidad de habitantes
superficie	int	Superficie en km²
continente	str	Continente al que pertenece

Validaciones
·	El nombre no puede estar vacío ni repetido.
·	La población y la superficie deben ser enteros positivos.
·	Los campos de texto solo aceptan letras.
·	Los rangos de filtrado validan que el mínimo no supere el máximo.
