# ==================== IMPORTACIÓN DE MÓDULOS ====================

import csv      # Módulo para trabajar con archivos CSV (leer y escribir)
import os       # Módulo para interactuar con el sistema operativo (verificar si existe un archivo)


# ==================== FUNCIONES DE CARGA Y GUARDADO ====================

def cargar_datos(nombre_archivo="paises.csv"):
    """
    Carga los paises desde el archivo CSV.
    Si el archivo no existe, retorna una lista vacía.
    
    Parámetro:
        nombre_archivo: string con el nombre del archivo CSV (opcional, por defecto "paises.csv")
    
    Retorna:
        Lista de diccionarios, donde cada diccionario representa un país
    """
    paises = []     # Inicializo una lista vacía para almacenar los países
    
    # os.path.exists() verifica si el archivo existe en el disco
    if not os.path.exists(nombre_archivo):
        return paises     # Si no existe el archivo, devuelvo lista vacía
    
    try:
        # with open() abre el archivo y lo cierra automáticamente al salir
        # "r" significa modo lectura (read)
        # encoding="utf-8" permite leer correctamente caracteres especiales
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            
            # csv.DictReader lee el CSV y convierte cada fila en un diccionario
            # La primera fila del CSV se usa como claves del diccionario
            lector = csv.DictReader(archivo)
            
            # Recorro cada fila del archivo CSV
            for fila in lector:
                # Creo un diccionario para cada país con sus datos
                pais = {
                    "nombre": fila["nombre"].strip(),           # .strip() elimina espacios al inicio/final
                    "poblacion": int(fila["poblacion"]),        # Convierto a entero
                    "superficie": int(fila["superficie"]),      # Convierto a entero
                    "continente": fila["continente"].strip()    # .strip() elimina espacios
                }
                paises.append(pais)     # Agrego el país a la lista
    
    # Manejo de errores: si algo falla, muestro un mensaje
    except (FileNotFoundError, KeyError, ValueError):
        print("⚠️ Error al leer el archivo. Se iniciara con lista vacia.")
    
    return paises      # Devuelvo la lista de países (puede estar vacía o con datos)


def guardar_datos(paises, nombre_archivo="paises.csv"):
    """
    Guarda la lista de paises en el archivo CSV.
    
    Parámetros:
        paises: lista de diccionarios con los datos de los países
        nombre_archivo: string con el nombre del archivo CSV (opcional)
    
    Retorna:
        True si se guardó correctamente, False si hubo error
    """
    try:
        # with open() abre el archivo en modo escritura
        # "w" significa modo escritura (write) - SOBRESCRIBE el archivo si existe
        # encoding="utf-8" para guardar correctamente caracteres especiales
        # newline="" evita líneas en blanco extra al guardar en Windows
        with open(nombre_archivo, "w", encoding="utf-8", newline="") as archivo:
            
            # Defino los nombres de las columnas en el orden que quiero
            campos = ["nombre", "poblacion", "superficie", "continente"]
            
            # csv.DictWriter escribe diccionarios en formato CSV
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            
            # writeheader() escribe la primera fila con los nombres de las columnas
            escritor.writeheader()
            
            # writerows() escribe TODOS los países de una vez
            escritor.writerows(paises)
        
        return True     # Devuelvo True indicando que se guardó correctamente
    
    except Exception:   # Si ocurre CUALQUIER error durante el guardado
        print("❌ Error al guardar los datos.")
        return False    # Devuelvo False indicando que hubo error


# ==================== FUNCIONES DE VALIDACIÓN ====================

def validar_entero_positivo(valor_str):
    """
    Valida que el string se pueda convertir a un número entero positivo.
    
    Parámetro:
        valor_str: string que se quiere convertir a entero
    
    Retorna:
        Una tupla (booleano, entero o None)
        - True, numero si la conversión fue exitosa y el número es > 0
        - False, None si falló la conversión o el número es <= 0
    """
    try:
        # Intento convertir el string a entero
        numero = int(valor_str)
        
        # Verifico que el número sea mayor que 0
        if numero > 0:
            return True, numero     # Éxito: devuelvo True y el número
        else:
            return False, None      # Error: el número no es positivo
    
    except ValueError:              # Si int() falla (ej: "abc" no se puede convertir)
        return False, None          # Error: no es un número válido


def validar_no_vacio(texto):
    """
    Valida que el string no esté vacío ni sean solo espacios.
    
    Parámetro:
        texto: string a validar
    
    Retorna:
        True si el texto tiene al menos un carácter visible
        False si el texto es None, vacío o solo espacios
    """
    # texto is not None: verifica que no sea nulo
    # texto.strip() != "": elimina espacios y verifica que quede algo
    return texto is not None and texto.strip() != ""


# ==================== FUNCIÓN 1: AGREGAR PAÍS ====================

def agregar_pais(paises):
    """
    Agrega un nuevo país a la lista.
    No permite campos vacíos ni población/superficie negativas o cero.
    Tampoco permite nombres duplicados.
    
    Parámetro:
        paises: lista de diccionarios con los países existentes
    
    Retorna:
        La lista modificada (la original se modifica directamente)
    """
    print("\n--- AGREGAR NUEVO PAIS ---")
    
    # ===== VALIDACIÓN DEL NOMBRE =====
    # Uso un bucle while True que solo se rompe cuando el dato es válido
    while True:
        # .strip() elimina espacios al principio y final
        nombre = input("Nombre del pais: ").strip()
        
        # Verifico que no esté vacío
        if not validar_no_vacio(nombre):
            print("❌ El nombre no puede estar vacio.")
            continue    # Vuelvo a pedir el nombre
        
        # Verifico que no exista ya un país con el mismo nombre
        # Recorro toda la lista de países comparando nombres en minúscula
        existe = False
        for pais in paises:
            # .lower() convierte a minúsculas para comparar sin distinguir mayúsculas
            if pais["nombre"].lower() == nombre.lower():
                existe = True
                break   # Si lo encuentro, salgo del bucle
        
        if existe:
            print("❌ Ese pais ya existe. Use otro nombre o actualicelo.")
            # No pongo continue, el bucle sigue (se vuelve a pedir el nombre)
        else:
            break   # Nombre válido y no duplicado, salgo del bucle
    
    # ===== VALIDACIÓN DEL CONTINENTE =====
    while True:
        continente = input("Continente: ").strip()
        
        if validar_no_vacio(continente):
            break   # Continente válido, salgo del bucle
        else:
            print("❌ El continente no puede estar vacio.")
    
    # ===== VALIDACIÓN DE LA POBLACIÓN =====
    while True:
        poblacion_str = input("Poblacion (habitantes): ").strip()
        
        # Llamo a la función de validación de números positivos
        valido, poblacion = validar_entero_positivo(poblacion_str)
        
        if valido:
            break   # Población válida, salgo del bucle
        else:
            print("❌ Ingrese un numero entero positivo valido (mayor a 0).")
    
    # ===== VALIDACIÓN DE LA SUPERFICIE =====
    while True:
        superficie_str = input("Superficie (km2): ").strip()
        
        # Reutilizo la misma función de validación
        valido, superficie = validar_entero_positivo(superficie_str)
        
        if valido:
            break   # Superficie válida, salgo del bucle
        else:
            print("❌ Ingrese un numero entero positivo valido (mayor a 0).")
    
    # ===== CREACIÓN Y AGREGADO DEL NUEVO PAÍS =====
    # Armo un diccionario con todos los datos del nuevo país
    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    
    # Agrego el diccionario a la lista de países
    paises.append(nuevo_pais)
    
    # Mensaje de éxito
    print(f"✅ Pais '{nombre}' agregado correctamente.")
    
    return paises   # Devuelvo la lista (aunque ya fue modificada directamente)


# ==================== FUNCIÓN 2: BUSCAR PAÍS ====================

def buscar_pais(paises):
    """
    Busca países por nombre (coincidencia parcial o exacta).
    No distingue entre mayúsculas y minúsculas.
    
    Parámetro:
        paises: lista de diccionarios con los países
    
    Retorna:
        Lista con los resultados encontrados (vacía si no hay)
    """
    print("\n--- BUSCAR PAIS ---")
    
    # Pido al usuario el criterio de búsqueda y lo convierto a minúsculas
    criterio = input("Ingrese nombre o parte del nombre a buscar: ").strip().lower()
    
    # Verifico que el criterio no esté vacío
    if not validar_no_vacio(criterio):
        print("❌ El criterio de busqueda no puede estar vacio.")
        return []   # Devuelvo lista vacía
    
    # ===== REALIZAR LA BÚSQUEDA =====
    resultados = []   # Lista donde voy a guardar los países que coincidan
    
    # Recorro todos los países de la lista
    for pais in paises:
        # Verifico si el criterio está DENTRO del nombre (coincidencia parcial)
        # pais["nombre"].lower() convierte el nombre a minúsculas para comparar
        if criterio in pais["nombre"].lower():
            resultados.append(pais)   # Agrego el país a los resultados
    
    # ===== MOSTRAR RESULTADOS =====
    if not resultados:
        # No se encontraron coincidencias
        print(f"❌ No se encontraron paises que contengan '{criterio}'.")
    else:
        # Muestro la cantidad de resultados encontrados
        print(f"\n🔍 {len(resultados)} resultado(s):")
        
        # Recorro y muestro cada país encontrado
        for p in resultados:
            # El formato {:,} agrega separadores de miles (ej: 45.376.763)
            print(f"   • {p['nombre']} | Poblacion: {p['poblacion']:,} | Superficie: {p['superficie']:,} km2 | {p['continente']}")
    
    return resultados   # Devuelvo la lista de resultados (por si se necesita después)


# ==================== FUNCIÓN 3: ESTADÍSTICAS ====================

def mostrar_estadisticas(paises):
    """
    Muestra estadísticas completas del dataset:
    - País con mayor y menor población
    - Promedio de población
    - Promedio de superficie
    - Cantidad de países por continente
    
    Parámetro:
        paises: lista de diccionarios con los países
    """
    # Verifico que haya datos para mostrar
    if not paises:
        print("❌ No hay datos para mostrar estadisticas.")
        return   # Salgo de la función sin hacer nada
    
    # ===== ENCABEZADO =====
    # Los "=" * 50 crea una línea de 50 caracteres "=" como separador
    print("\n" + "=" * 50)
    print("📊 ESTADISTICAS DE PAISES")
    print("=" * 50)
    
    # ===== 1. PAÍS CON MAYOR Y MENOR POBLACIÓN =====
    # Inicializo las variables con el PRIMER país de la lista
    # Esto es seguro porque ya verificamos que la lista no está vacía
    mayor_pob = paises[0]
    menor_pob = paises[0]
    
    # Recorro todos los países comparando poblaciones
    for pais in paises:
        # Si encuentro un país con mayor población, actualizo "mayor_pob"
        if pais["poblacion"] > mayor_pob["poblacion"]:
            mayor_pob = pais
        
        # Si encuentro un país con menor población, actualizo "menor_pob"
        if pais["poblacion"] < menor_pob["poblacion"]:
            menor_pob = pais
    
    # Muestro los resultados con formato
    print(f"\n👥 POBLACION:")
    print(f"   • Mayor poblacion: {mayor_pob['nombre']} con {mayor_pob['poblacion']:,} habitantes")
    print(f"   • Menor poblacion: {menor_pob['nombre']} con {menor_pob['poblacion']:,} habitantes")
    
    # ===== 2. PROMEDIO DE POBLACIÓN =====
    suma_poblacion = 0   # Acumulador para sumar todas las poblaciones
    
    # Sumo la población de todos los países
    for pais in paises:
        suma_poblacion += pais["poblacion"]
    
    # Calculo el promedio dividiendo la suma por la cantidad de países
    # len(paises) devuelve la cantidad de elementos en la lista
    promedio_poblacion = suma_poblacion / len(paises)
    
    # Muestro el promedio con formato (:.0f significa sin decimales)
    print(f"   • Promedio de poblacion: {promedio_poblacion:,.0f} habitantes")
    
    # ===== 3. PROMEDIO DE SUPERFICIE =====
    suma_superficie = 0   # Acumulador para sumar todas las superficies
    
    # Sumo la superficie de todos los países
    for pais in paises:
        suma_superficie += pais["superficie"]
    
    # Calculo el promedio
    promedio_superficie = suma_superficie / len(paises)
    
    print(f"\n🗺️ SUPERFICIE:")
    print(f"   • Promedio de superficie: {promedio_superficie:,.0f} km2")
    
    # ===== 4. CANTIDAD DE PAÍSES POR CONTINENTE =====
    # Uso un diccionario donde la clave es el continente y el valor es la cantidad
    continentes = {}
    
    # Recorro todos los países
    for pais in paises:
        continente = pais["continente"]
        
        # Si el continente ya existe en el diccionario, incremento su contador
        if continente in continentes:
            continentes[continente] += 1   # Sumo 1 al valor existente
        else:
            continentes[continente] = 1    # Creo la clave con valor inicial 1
    
    # Muestro los resultados
    print(f"\n🌍 CANTIDAD DE PAISES POR CONTINENTE:")
    
    # sorted() ordena alfabéticamente los continentes para mejor presentación
    for continente in sorted(continentes.keys()):
        cantidad = continentes[continente]
        print(f"   • {continente}: {cantidad} pais(es)")
    
    # Línea final de cierre
    print("\n" + "=" * 50)


# ==================== MENÚ PRINCIPAL ====================

def mostrar_menu():
    """
    Muestra el menú principal de opciones en consola.
    Esta función solo se encarga de mostrar las opciones, no de procesarlas.
    """
    print("\n" + "=" * 50)
    print("🌍 SISTEMA DE GESTION DE PAISES 🌍")
    print("=" * 50)
    print("1. Agregar pais")
    print("2. Buscar pais por nombre")
    print("3. Mostrar estadisticas")
    print("4. Guardar y salir")
    print("-" * 50)


def main():
    """
    Función principal del programa.
    Contiene el bucle while que mantiene el programa en ejecución
    hasta que el usuario elige la opción de salir.
    """
    # Cargo los datos existentes desde el archivo CSV al iniciar el programa
    paises = cargar_datos()
    
    # Bucle infinito que se rompe solo cuando el usuario elige la opción 4
    while True:
        # Muestro el menú
        mostrar_menu()
        
        # Pido la opción al usuario y elimino espacios alrededor
        opcion = input("Seleccione una opcion (1-4): ").strip()
        
        # ===== OPCIÓN 1: AGREGAR PAÍS =====
        if opcion == "1":
            agregar_pais(paises)           # Llamo a mi función
            guardar_datos(paises)          # Guardo automáticamente después de agregar
        
        # ===== OPCIÓN 2: BUSCAR PAÍS =====
        elif opcion == "2":
            buscar_pais(paises)            # Llamo a mi función de búsqueda
        
        # ===== OPCIÓN 3: MOSTRAR ESTADÍSTICAS =====
        elif opcion == "3":
            mostrar_estadisticas(paises)   # Llamo a mi función de estadísticas
        
        # ===== OPCIÓN 4: GUARDAR Y SALIR =====
        elif opcion == "4":
            print("\n📀 Guardando datos...")
            
            # Intento guardar los datos
            if guardar_datos(paises):
                print("✅ Datos guardados correctamente. ¡Hasta luego!")
            else:
                print("❌ Error al guardar. Los datos no se preservaran.")
            
            break   # Rompo el bucle while para salir del programa
        
        # ===== OPCIÓN INVÁLIDA =====
        else:
            print("❌ Opcion invalida. Por favor, seleccione 1, 2, 3 o 4.")


# ==================== PUNTO DE ENTRADA DEL PROGRAMA ====================

# Esta condición verifica si el archivo se está ejecutando directamente
# (y no siendo importado como módulo desde otro archivo)
if __name__ == "__main__":
    main()   # Llamo a la función principal para iniciar el programa