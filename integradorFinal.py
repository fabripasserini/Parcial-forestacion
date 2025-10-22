"""
INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO
============================================================================
Directorio raiz: /home/fabri/Parcial-forestacion
Fecha de generacion: 2025-10-22 01:25:44
Total de archivos integrados: 69
Total de directorios procesados: 22
============================================================================
"""

# ==============================================================================
# TABLA DE CONTENIDOS
# ==============================================================================

# DIRECTORIO: .
#   1. __init__.py
#   2. buscar_paquete.py
#   3. main.py
#
# DIRECTORIO: python_forestacion
#   4. __init__.py
#   5. constantes.py
#
# DIRECTORIO: python_forestacion/entidades
#   6. __init__.py
#
# DIRECTORIO: python_forestacion/entidades/cultivos
#   7. __init__.py
#   8. arbol.py
#   9. cultivo.py
#   10. hortaliza.py
#   11. lechuga.py
#   12. olivo.py
#   13. pino.py
#   14. tipo_aceituna.py
#   15. zanahoria.py
#
# DIRECTORIO: python_forestacion/entidades/personal
#   16. __init__.py
#   17. apto_medico.py
#   18. herramienta.py
#   19. tarea.py
#   20. trabajador.py
#
# DIRECTORIO: python_forestacion/entidades/terrenos
#   21. __init__.py
#   22. plantacion.py
#   23. registro_florestal.py
#   24. registro_forestal.py
#   25. tierra.py
#
# DIRECTORIO: python_forestacion/excepciones
#   26. __init__.py
#   27. agua_agotada_exception.py
#   28. forestacion_exception.py
#   29. mensajes_exception.py
#   30. persistencia_exception.py
#   31. superficie_insuficiente_exception.py
#
# DIRECTORIO: python_forestacion/patrones
#   32. __init__.py
#
# DIRECTORIO: python_forestacion/patrones/factory
#   33. __init__.py
#   34. cultivo_factory.py
#
# DIRECTORIO: python_forestacion/patrones/observer
#   35. __init__.py
#   36. observable.py
#   37. observer.py
#
# DIRECTORIO: python_forestacion/patrones/observer/eventos
#   38. __init__.py
#   39. evento_sensor.py
#
# DIRECTORIO: python_forestacion/patrones/singleton
#   40. __init__.py
#
# DIRECTORIO: python_forestacion/patrones/strategy
#   41. __init__.py
#   42. absorcion_agua_strategy.py
#
# DIRECTORIO: python_forestacion/patrones/strategy/impl
#   43. __init__.py
#   44. absorcion_constante_strategy.py
#   45. absorcion_seasonal_strategy.py
#
# DIRECTORIO: python_forestacion/riego
#   46. __init__.py
#
# DIRECTORIO: python_forestacion/riego/control
#   47. __init__.py
#   48. control_riego_task.py
#
# DIRECTORIO: python_forestacion/riego/sensores
#   49. __init__.py
#   50. humedad_reader_task.py
#   51. temperatura_reader_task.py
#
# DIRECTORIO: python_forestacion/servicios
#   52. __init__.py
#
# DIRECTORIO: python_forestacion/servicios/cultivos
#   53. __init__.py
#   54. arbol_service.py
#   55. cultivo_service.py
#   56. cultivo_service_registry.py
#   57. lechuga_service.py
#   58. olivo_service.py
#   59. pino_service.py
#   60. zanahoria_service.py
#
# DIRECTORIO: python_forestacion/servicios/negocio
#   61. __init__.py
#   62. fincas_service.py
#   63. paquete.py
#
# DIRECTORIO: python_forestacion/servicios/personal
#   64. __init__.py
#   65. trabajador_service.py
#
# DIRECTORIO: python_forestacion/servicios/terrenos
#   66. __init__.py
#   67. plantacion_service.py
#   68. registro_forestal_service.py
#   69. tierra_service.py
#



################################################################################
# DIRECTORIO: .
################################################################################

# ==============================================================================
# ARCHIVO 1/69: __init__.py
# Directorio: .
# Ruta completa: /home/fabri/Parcial-forestacion/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 2/69: buscar_paquete.py
# Directorio: .
# Ruta completa: /home/fabri/Parcial-forestacion/buscar_paquete.py
# ==============================================================================

"""
Script para buscar el paquete python_forestacion desde el directorio raiz del proyecto.
Incluye funcionalidad para integrar archivos Python en cada nivel del arbol de directorios.
"""
import os
import sys
from datetime import datetime


def buscar_paquete(directorio_raiz: str, nombre_paquete: str) -> list:
    """
    Busca un paquete Python en el directorio raiz y subdirectorios.

    Args:
        directorio_raiz: Directorio desde donde iniciar la busqueda
        nombre_paquete: Nombre del paquete a buscar

    Returns:
        Lista de rutas donde se encontro el paquete
    """
    paquetes_encontrados = []

    for raiz, directorios, archivos in os.walk(directorio_raiz):
        # Verificar si el directorio actual es el paquete buscado
        nombre_dir = os.path.basename(raiz)

        if nombre_dir == nombre_paquete:
            # Verificar que sea un paquete Python (contiene __init__.py)
            if '__init__.py' in archivos:
                paquetes_encontrados.append(raiz)
                print(f"[+] Paquete encontrado: {raiz}")
            else:
                print(f"[!] Directorio encontrado pero no es un paquete Python: {raiz}")

    return paquetes_encontrados


def obtener_archivos_python(directorio: str) -> list:
    """
    Obtiene todos los archivos Python en un directorio (sin recursion).

    Args:
        directorio: Ruta del directorio a examinar

    Returns:
        Lista de rutas completas de archivos .py
    """
    archivos_python = []
    try:
        for item in os.listdir(directorio):
            ruta_completa = os.path.join(directorio, item)
            if os.path.isfile(ruta_completa) and item.endswith('.py'):
                # Excluir archivos integradores para evitar recursion infinita
                if item not in ['integrador.py', 'integradorFinal.py']:
                    archivos_python.append(ruta_completa)
    except PermissionError:
        print(f"[!] Sin permisos para leer: {directorio}")

    return sorted(archivos_python)


def obtener_subdirectorios(directorio: str) -> list:
    """
    Obtiene todos los subdirectorios inmediatos de un directorio.

    Args:
        directorio: Ruta del directorio a examinar

    Returns:
        Lista de rutas completas de subdirectorios
    """
    subdirectorios = []
    try:
        for item in os.listdir(directorio):
            ruta_completa = os.path.join(directorio, item)
            if os.path.isdir(ruta_completa):
                # Excluir directorios especiales
                if not item.startswith('.') and item not in ['__pycache__', 'venv', '.venv']:
                    subdirectorios.append(ruta_completa)
    except PermissionError:
        print(f"[!] Sin permisos para leer: {directorio}")

    return sorted(subdirectorios)


def leer_contenido_archivo(ruta_archivo: str) -> str:
    """
    Lee el contenido de un archivo Python.

    Args:
        ruta_archivo: Ruta completa del archivo

    Returns:
        Contenido del archivo como string
    """
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            return archivo.read()
    except Exception as error:
        print(f"[!] Error al leer {ruta_archivo}: {error}")
        return f"# Error al leer este archivo: {error}\n"


def crear_archivo_integrador(directorio: str, archivos_python: list) -> bool:
    """
    Crea un archivo integrador.py con el contenido de todos los archivos Python.

    Args:
        directorio: Directorio donde crear el archivo integrador
        archivos_python: Lista de rutas de archivos Python a integrar

    Returns:
        True si se creo exitosamente, False en caso contrario
    """
    if not archivos_python:
        return False

    ruta_integrador = os.path.join(directorio, 'integrador.py')

    try:
        with open(ruta_integrador, 'w', encoding='utf-8') as integrador:
            # Encabezado
            integrador.write('"""\n')
            integrador.write(f"Archivo integrador generado automaticamente\n")
            integrador.write(f"Directorio: {directorio}\n")
            integrador.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            integrador.write(f"Total de archivos integrados: {len(archivos_python)}\n")
            integrador.write('"""\n\n')

            # Integrar cada archivo
            for idx, archivo in enumerate(archivos_python, 1):
                nombre_archivo = os.path.basename(archivo)
                integrador.write(f"# {'=' * 80}\n")
                integrador.write(f"# ARCHIVO {idx}/{len(archivos_python)}: {nombre_archivo}\n")
                integrador.write(f"# Ruta: {archivo}\n")
                integrador.write(f"# {'=' * 80}\n\n")

                contenido = leer_contenido_archivo(archivo)
                integrador.write(contenido)
                integrador.write("\n\n")

        print(f"[OK] Integrador creado: {ruta_integrador}")
        print(f"     Archivos integrados: {len(archivos_python)}")
        return True

    except Exception as error:
        print(f"[!] Error al crear integrador en {directorio}: {error}")
        return False


def procesar_directorio_recursivo(directorio: str, nivel: int = 0, archivos_totales: list = None) -> list:
    """
    Procesa un directorio de forma recursiva, creando integradores en cada nivel.
    Utiliza DFS (Depth-First Search) para llegar primero a los niveles mas profundos.

    Args:
        directorio: Directorio a procesar
        nivel: Nivel de profundidad actual (para logging)
        archivos_totales: Lista acumulativa de todos los archivos procesados

    Returns:
        Lista de todos los archivos Python procesados en el arbol
    """
    if archivos_totales is None:
        archivos_totales = []

    indentacion = "  " * nivel
    print(f"{indentacion}[INFO] Procesando nivel {nivel}: {os.path.basename(directorio)}")

    # Obtener subdirectorios
    subdirectorios = obtener_subdirectorios(directorio)

    # Primero, procesar recursivamente todos los subdirectorios (DFS)
    for subdir in subdirectorios:
        procesar_directorio_recursivo(subdir, nivel + 1, archivos_totales)

    # Despues de procesar subdirectorios, procesar archivos del nivel actual
    archivos_python = obtener_archivos_python(directorio)

    if archivos_python:
        print(f"{indentacion}[+] Encontrados {len(archivos_python)} archivo(s) Python")
        crear_archivo_integrador(directorio, archivos_python)
        # Agregar archivos a la lista total
        archivos_totales.extend(archivos_python)
    else:
        print(f"{indentacion}[INFO] No hay archivos Python en este nivel")

    return archivos_totales


def crear_integrador_final(directorio_raiz: str, archivos_totales: list) -> bool:
    """
    Crea un archivo integradorFinal.py con TODO el codigo fuente de todas las ramas.

    Args:
        directorio_raiz: Directorio donde crear el archivo integrador final
        archivos_totales: Lista completa de todos los archivos Python procesados

    Returns:
        True si se creo exitosamente, False en caso contrario
    """
    if not archivos_totales:
        print("[!] No hay archivos para crear el integrador final")
        return False

    ruta_integrador_final = os.path.join(directorio_raiz, 'integradorFinal.py')

    # Organizar archivos por directorio para mejor estructura
    archivos_por_directorio = {}
    for archivo in archivos_totales:
        directorio = os.path.dirname(archivo)
        if directorio not in archivos_por_directorio:
            archivos_por_directorio[directorio] = []
        archivos_por_directorio[directorio].append(archivo)

    try:
        with open(ruta_integrador_final, 'w', encoding='utf-8') as integrador_final:
            # Encabezado principal
            integrador_final.write('"""\n')
            integrador_final.write("INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO\n")
            integrador_final.write("=" * 76 + "\n")
            integrador_final.write(f"Directorio raiz: {directorio_raiz}\n")
            integrador_final.write(f"Fecha de generacion: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            integrador_final.write(f"Total de archivos integrados: {len(archivos_totales)}\n")
            integrador_final.write(f"Total de directorios procesados: {len(archivos_por_directorio)}\n")
            integrador_final.write("=" * 76 + "\n")
            integrador_final.write('"""\n\n')

            # Tabla de contenidos
            integrador_final.write("# " + "=" * 78 + "\n")
            integrador_final.write("# TABLA DE CONTENIDOS\n")
            integrador_final.write("# " + "=" * 78 + "\n\n")

            contador_global = 1
            for directorio in sorted(archivos_por_directorio.keys()):
                dir_relativo = os.path.relpath(directorio, directorio_raiz)
                integrador_final.write(f"# DIRECTORIO: {dir_relativo}\n")
                for archivo in sorted(archivos_por_directorio[directorio]):
                    nombre_archivo = os.path.basename(archivo)
                    integrador_final.write(f"#   {contador_global}. {nombre_archivo}\n")
                    contador_global += 1
                integrador_final.write("#\n")

            integrador_final.write("\n\n")

            # Contenido completo organizado por directorio
            contador_global = 1
            for directorio in sorted(archivos_por_directorio.keys()):
                dir_relativo = os.path.relpath(directorio, directorio_raiz)

                # Separador de directorio
                integrador_final.write("\n" + "#" * 80 + "\n")
                integrador_final.write(f"# DIRECTORIO: {dir_relativo}\n")
                integrador_final.write("#" * 80 + "\n\n")

                # Procesar cada archivo del directorio
                for archivo in sorted(archivos_por_directorio[directorio]):
                    nombre_archivo = os.path.basename(archivo)

                    integrador_final.write(f"# {'=' * 78}\n")
                    integrador_final.write(f"# ARCHIVO {contador_global}/{len(archivos_totales)}: {nombre_archivo}\n")
                    integrador_final.write(f"# Directorio: {dir_relativo}\n")
                    integrador_final.write(f"# Ruta completa: {archivo}\n")
                    integrador_final.write(f"# {'=' * 78}\n\n")

                    contenido = leer_contenido_archivo(archivo)
                    integrador_final.write(contenido)
                    integrador_final.write("\n\n")

                    contador_global += 1

            # Footer
            integrador_final.write("\n" + "#" * 80 + "\n")
            integrador_final.write("# FIN DEL INTEGRADOR FINAL\n")
            integrador_final.write(f"# Total de archivos: {len(archivos_totales)}\n")
            integrador_final.write(f"# Generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            integrador_final.write("#" * 80 + "\n")

        print(f"\n[OK] Integrador final creado: {ruta_integrador_final}")
        print(f"     Total de archivos integrados: {len(archivos_totales)}")
        print(f"     Total de directorios procesados: {len(archivos_por_directorio)}")

        # Mostrar tamanio del archivo
        tamanio = os.path.getsize(ruta_integrador_final)
        if tamanio < 1024:
            tamanio_str = f"{tamanio} bytes"
        elif tamanio < 1024 * 1024:
            tamanio_str = f"{tamanio / 1024:.2f} KB"
        else:
            tamanio_str = f"{tamanio / (1024 * 1024):.2f} MB"
        print(f"     Tamanio del archivo: {tamanio_str}")

        return True

    except Exception as error:
        print(f"[!] Error al crear integrador final: {error}")
        return False


def integrar_arbol_directorios(directorio_raiz: str) -> None:
    """
    Inicia el proceso de integracion para todo el arbol de directorios.

    Args:
        directorio_raiz: Directorio raiz desde donde comenzar
    """
    print("\n" + "=" * 80)
    print("INICIANDO INTEGRACION DE ARCHIVOS PYTHON")
    print("=" * 80)
    print(f"Directorio raiz: {directorio_raiz}\n")

    # Procesar directorios y obtener lista de todos los archivos
    archivos_totales = procesar_directorio_recursivo(directorio_raiz)

    print("\n" + "=" * 80)
    print("INTEGRACION POR NIVELES COMPLETADA")
    print("=" * 80)

    # Crear integrador final con todos los archivos
    if archivos_totales:
        print("\n" + "=" * 80)
        print("CREANDO INTEGRADOR FINAL")
        print("=" * 80)
        crear_integrador_final(directorio_raiz, archivos_totales)

    print("\n" + "=" * 80)
    print("PROCESO COMPLETO FINALIZADO")
    print("=" * 80)


def main():
    """Funcion principal del script."""
    # Obtener el directorio raiz del proyecto (donde esta este script)
    directorio_raiz = os.path.dirname(os.path.abspath(__file__))

    # Verificar argumentos de linea de comandos
    if len(sys.argv) > 1:
        comando = sys.argv[1].lower()

        if comando == "integrar":
            # Modo de integracion de archivos
            if len(sys.argv) > 2:
                directorio_objetivo = sys.argv[2]
                if not os.path.isabs(directorio_objetivo):
                    directorio_objetivo = os.path.join(directorio_raiz, directorio_objetivo)
            else:
                directorio_objetivo = directorio_raiz

            if not os.path.isdir(directorio_objetivo):
                print(f"[!] El directorio no existe: {directorio_objetivo}")
                return 1

            integrar_arbol_directorios(directorio_objetivo)
            return 0

        elif comando == "help" or comando == "--help" or comando == "-h":
            print("Uso: python buscar_paquete.py [COMANDO] [OPCIONES]")
            print("")
            print("Comandos disponibles:")
            print("  (sin argumentos)     Busca el paquete python_forestacion")
            print("  integrar [DIR]       Integra archivos Python en el arbol de directorios")
            print("                       DIR: directorio raiz (por defecto: directorio actual)")
            print("  help                 Muestra esta ayuda")
            print("")
            print("Ejemplos:")
            print("  python buscar_paquete.py")
            print("  python buscar_paquete.py integrar")
            print("  python buscar_paquete.py integrar python_forestacion")
            return 0

        else:
            print(f"[!] Comando desconocido: {comando}")
            print("    Use 'python buscar_paquete.py help' para ver los comandos disponibles")
            return 1

    # Modo por defecto: buscar paquete
    print(f"[INFO] Buscando desde: {directorio_raiz}")
    print(f"[INFO] Buscando paquete: python_forestacion")
    print("")

    # Buscar el paquete
    paquetes = buscar_paquete(directorio_raiz, "python_forestacion")

    print("")
    if paquetes:
        print(f"[OK] Se encontraron {len(paquetes)} paquete(s):")
        for paquete in paquetes:
            print(f"  - {paquete}")

            # Mostrar estructura basica del paquete
            print(f"    Contenido:")
            try:
                contenido = os.listdir(paquete)
                for item in sorted(contenido)[:10]:  # Mostrar primeros 10 items
                    ruta_item = os.path.join(paquete, item)
                    if os.path.isdir(ruta_item):
                        print(f"      [DIR]  {item}")
                    else:
                        print(f"      [FILE] {item}")
                if len(contenido) > 10:
                    print(f"      ... y {len(contenido) - 10} items mas")
            except PermissionError:
                print(f"      [!] Sin permisos para leer el directorio")
    else:
        print("[!] No se encontro el paquete python_forestacion")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())

# ==============================================================================
# ARCHIVO 3/69: main.py
# Directorio: .
# Ruta completa: /home/fabri/Parcial-forestacion/main.py
# ==============================================================================

"""
Script para buscar el paquete python_forestacion desde el directorio raiz del proyecto.
Incluye funcionalidad para integrar archivos Python en cada nivel del arbol de directorios.
"""
import os
import sys
from datetime import datetime


def buscar_paquete(directorio_raiz: str, nombre_paquete: str) -> list:
    """
    Busca un paquete Python en el directorio raiz y subdirectorios.

    Args:
        directorio_raiz: Directorio desde donde iniciar la busqueda
        nombre_paquete: Nombre del paquete a buscar

    Returns:
        Lista de rutas donde se encontro el paquete
    """
    paquetes_encontrados = []

    for raiz, directorios, archivos in os.walk(directorio_raiz):
        # Verificar si el directorio actual es el paquete buscado
        nombre_dir = os.path.basename(raiz)

        if nombre_dir == nombre_paquete:
            # Verificar que sea un paquete Python (contiene __init__.py)
            if '__init__.py' in archivos:
                paquetes_encontrados.append(raiz)
                print(f"[+] Paquete encontrado: {raiz}")
            else:
                print(f"[!] Directorio encontrado pero no es un paquete Python: {raiz}")

    return paquetes_encontrados


def obtener_archivos_python(directorio: str) -> list:
    """
    Obtiene todos los archivos Python en un directorio (sin recursion).

    Args:
        directorio: Ruta del directorio a examinar

    Returns:
        Lista de rutas completas de archivos .py
    """
    archivos_python = []
    try:
        for item in os.listdir(directorio):
            ruta_completa = os.path.join(directorio, item)
            if os.path.isfile(ruta_completa) and item.endswith('.py'):
                # Excluir archivos integradores para evitar recursion infinita
                if item not in ['integrador.py', 'integradorFinal.py']:
                    archivos_python.append(ruta_completa)
    except PermissionError:
        print(f"[!] Sin permisos para leer: {directorio}")

    return sorted(archivos_python)


def obtener_subdirectorios(directorio: str) -> list:
    """
    Obtiene todos los subdirectorios inmediatos de un directorio.

    Args:
        directorio: Ruta del directorio a examinar

    Returns:
        Lista de rutas completas de subdirectorios
    """
    subdirectorios = []
    try:
        for item in os.listdir(directorio):
            ruta_completa = os.path.join(directorio, item)
            if os.path.isdir(ruta_completa):
                # Excluir directorios especiales
                if not item.startswith('.') and item not in ['__pycache__', 'venv', '.venv']:
                    subdirectorios.append(ruta_completa)
    except PermissionError:
        print(f"[!] Sin permisos para leer: {directorio}")

    return sorted(subdirectorios)


def leer_contenido_archivo(ruta_archivo: str) -> str:
    """
    Lee el contenido de un archivo Python.

    Args:
        ruta_archivo: Ruta completa del archivo

    Returns:
        Contenido del archivo como string
    """
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            return archivo.read()
    except Exception as error:
        print(f"[!] Error al leer {ruta_archivo}: {error}")
        return f"# Error al leer este archivo: {error}\n"


def crear_archivo_integrador(directorio: str, archivos_python: list) -> bool:
    """
    Crea un archivo integrador.py con el contenido de todos los archivos Python.

    Args:
        directorio: Directorio donde crear el archivo integrador
        archivos_python: Lista de rutas de archivos Python a integrar

    Returns:
        True si se creo exitosamente, False en caso contrario
    """
    if not archivos_python:
        return False

    ruta_integrador = os.path.join(directorio, 'integrador.py')

    try:
        with open(ruta_integrador, 'w', encoding='utf-8') as integrador:
            # Encabezado
            integrador.write('"""\n')
            integrador.write(f"Archivo integrador generado automaticamente\n")
            integrador.write(f"Directorio: {directorio}\n")
            integrador.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            integrador.write(f"Total de archivos integrados: {len(archivos_python)}\n")
            integrador.write('"""\n\n')

            # Integrar cada archivo
            for idx, archivo in enumerate(archivos_python, 1):
                nombre_archivo = os.path.basename(archivo)
                integrador.write(f"# {'=' * 80}\n")
                integrador.write(f"# ARCHIVO {idx}/{len(archivos_python)}: {nombre_archivo}\n")
                integrador.write(f"# Ruta: {archivo}\n")
                integrador.write(f"# {'=' * 80}\n\n")

                contenido = leer_contenido_archivo(archivo)
                integrador.write(contenido)
                integrador.write("\n\n")

        print(f"[OK] Integrador creado: {ruta_integrador}")
        print(f"     Archivos integrados: {len(archivos_python)}")
        return True

    except Exception as error:
        print(f"[!] Error al crear integrador en {directorio}: {error}")
        return False


def procesar_directorio_recursivo(directorio: str, nivel: int = 0, archivos_totales: list = None) -> list:
    """
    Procesa un directorio de forma recursiva, creando integradores en cada nivel.
    Utiliza DFS (Depth-First Search) para llegar primero a los niveles mas profundos.

    Args:
        directorio: Directorio a procesar
        nivel: Nivel de profundidad actual (para logging)
        archivos_totales: Lista acumulativa de todos los archivos procesados

    Returns:
        Lista de todos los archivos Python procesados en el arbol
    """
    if archivos_totales is None:
        archivos_totales = []

    indentacion = "  " * nivel
    print(f"{indentacion}[INFO] Procesando nivel {nivel}: {os.path.basename(directorio)}")

    # Obtener subdirectorios
    subdirectorios = obtener_subdirectorios(directorio)

    # Primero, procesar recursivamente todos los subdirectorios (DFS)
    for subdir in subdirectorios:
        procesar_directorio_recursivo(subdir, nivel + 1, archivos_totales)

    # Despues de procesar subdirectorios, procesar archivos del nivel actual
    archivos_python = obtener_archivos_python(directorio)

    if archivos_python:
        print(f"{indentacion}[+] Encontrados {len(archivos_python)} archivo(s) Python")
        crear_archivo_integrador(directorio, archivos_python)
        # Agregar archivos a la lista total
        archivos_totales.extend(archivos_python)
    else:
        print(f"{indentacion}[INFO] No hay archivos Python en este nivel")

    return archivos_totales


def crear_integrador_final(directorio_raiz: str, archivos_totales: list) -> bool:
    """
    Crea un archivo integradorFinal.py con TODO el codigo fuente de todas las ramas.

    Args:
        directorio_raiz: Directorio donde crear el archivo integrador final
        archivos_totales: Lista completa de todos los archivos Python procesados

    Returns:
        True si se creo exitosamente, False en caso contrario
    """
    if not archivos_totales:
        print("[!] No hay archivos para crear el integrador final")
        return False

    ruta_integrador_final = os.path.join(directorio_raiz, 'integradorFinal.py')

    # Organizar archivos por directorio para mejor estructura
    archivos_por_directorio = {}
    for archivo in archivos_totales:
        directorio = os.path.dirname(archivo)
        if directorio not in archivos_por_directorio:
            archivos_por_directorio[directorio] = []
        archivos_por_directorio[directorio].append(archivo)

    try:
        with open(ruta_integrador_final, 'w', encoding='utf-8') as integrador_final:
            # Encabezado principal
            integrador_final.write('"""\n')
            integrador_final.write("INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO\n")
            integrador_final.write("=" * 76 + "\n")
            integrador_final.write(f"Directorio raiz: {directorio_raiz}\n")
            integrador_final.write(f"Fecha de generacion: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            integrador_final.write(f"Total de archivos integrados: {len(archivos_totales)}\n")
            integrador_final.write(f"Total de directorios procesados: {len(archivos_por_directorio)}\n")
            integrador_final.write("=" * 76 + "\n")
            integrador_final.write('"""\n\n')

            # Tabla de contenidos
            integrador_final.write("# " + "=" * 78 + "\n")
            integrador_final.write("# TABLA DE CONTENIDOS\n")
            integrador_final.write("# " + "=" * 78 + "\n\n")

            contador_global = 1
            for directorio in sorted(archivos_por_directorio.keys()):
                dir_relativo = os.path.relpath(directorio, directorio_raiz)
                integrador_final.write(f"# DIRECTORIO: {dir_relativo}\n")
                for archivo in sorted(archivos_por_directorio[directorio]):
                    nombre_archivo = os.path.basename(archivo)
                    integrador_final.write(f"#   {contador_global}. {nombre_archivo}\n")
                    contador_global += 1
                integrador_final.write("#\n")

            integrador_final.write("\n\n")

            # Contenido completo organizado por directorio
            contador_global = 1
            for directorio in sorted(archivos_por_directorio.keys()):
                dir_relativo = os.path.relpath(directorio, directorio_raiz)

                # Separador de directorio
                integrador_final.write("\n" + "#" * 80 + "\n")
                integrador_final.write(f"# DIRECTORIO: {dir_relativo}\n")
                integrador_final.write("#" * 80 + "\n\n")

                # Procesar cada archivo del directorio
                for archivo in sorted(archivos_por_directorio[directorio]):
                    nombre_archivo = os.path.basename(archivo)

                    integrador_final.write(f"# {'=' * 78}\n")
                    integrador_final.write(f"# ARCHIVO {contador_global}/{len(archivos_totales)}: {nombre_archivo}\n")
                    integrador_final.write(f"# Directorio: {dir_relativo}\n")
                    integrador_final.write(f"# Ruta completa: {archivo}\n")
                    integrador_final.write(f"# {'=' * 78}\n\n")

                    contenido = leer_contenido_archivo(archivo)
                    integrador_final.write(contenido)
                    integrador_final.write("\n\n")

                    contador_global += 1

            # Footer
            integrador_final.write("\n" + "#" * 80 + "\n")
            integrador_final.write("# FIN DEL INTEGRADOR FINAL\n")
            integrador_final.write(f"# Total de archivos: {len(archivos_totales)}\n")
            integrador_final.write(f"# Generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            integrador_final.write("#" * 80 + "\n")

        print(f"\n[OK] Integrador final creado: {ruta_integrador_final}")
        print(f"     Total de archivos integrados: {len(archivos_totales)}")
        print(f"     Total de directorios procesados: {len(archivos_por_directorio)}")

        # Mostrar tamanio del archivo
        tamanio = os.path.getsize(ruta_integrador_final)
        if tamanio < 1024:
            tamanio_str = f"{tamanio} bytes"
        elif tamanio < 1024 * 1024:
            tamanio_str = f"{tamanio / 1024:.2f} KB"
        else:
            tamanio_str = f"{tamanio / (1024 * 1024):.2f} MB"
        print(f"     Tamanio del archivo: {tamanio_str}")

        return True

    except Exception as error:
        print(f"[!] Error al crear integrador final: {error}")
        return False


def integrar_arbol_directorios(directorio_raiz: str) -> None:
    """
    Inicia el proceso de integracion para todo el arbol de directorios.

    Args:
        directorio_raiz: Directorio raiz desde donde comenzar
    """
    print("\n" + "=" * 80)
    print("INICIANDO INTEGRACION DE ARCHIVOS PYTHON")
    print("=" * 80)
    print(f"Directorio raiz: {directorio_raiz}\n")

    # Procesar directorios y obtener lista de todos los archivos
    archivos_totales = procesar_directorio_recursivo(directorio_raiz)

    print("\n" + "=" * 80)
    print("INTEGRACION POR NIVELES COMPLETADA")
    print("=" * 80)

    # Crear integrador final con todos los archivos
    if archivos_totales:
        print("\n" + "=" * 80)
        print("CREANDO INTEGRADOR FINAL")
        print("=" * 80)
        crear_integrador_final(directorio_raiz, archivos_totales)

    print("\n" + "=" * 80)
    print("PROCESO COMPLETO FINALIZADO")
    print("=" * 80)


def main():
    """Funcion principal del script."""
    # Obtener el directorio raiz del proyecto (donde esta este script)
    directorio_raiz = os.path.dirname(os.path.abspath(__file__))

    # Verificar argumentos de linea de comandos
    if len(sys.argv) > 1:
        comando = sys.argv[1].lower()

        if comando == "integrar":
            # Modo de integracion de archivos
            if len(sys.argv) > 2:
                directorio_objetivo = sys.argv[2]
                if not os.path.isabs(directorio_objetivo):
                    directorio_objetivo = os.path.join(directorio_raiz, directorio_objetivo)
            else:
                directorio_objetivo = directorio_raiz

            if not os.path.isdir(directorio_objetivo):
                print(f"[!] El directorio no existe: {directorio_objetivo}")
                return 1

            integrar_arbol_directorios(directorio_objetivo)
            return 0

        elif comando == "help" or comando == "--help" or comando == "-h":
            print("Uso: python buscar_paquete.py [COMANDO] [OPCIONES]")
            print("")
            print("Comandos disponibles:")
            print("  (sin argumentos)     Busca el paquete python_forestacion")
            print("  integrar [DIR]       Integra archivos Python en el arbol de directorios")
            print("                       DIR: directorio raiz (por defecto: directorio actual)")
            print("  help                 Muestra esta ayuda")
            print("")
            print("Ejemplos:")
            print("  python buscar_paquete.py")
            print("  python buscar_paquete.py integrar")
            print("  python buscar_paquete.py integrar python_forestacion")
            return 0

        else:
            print(f"[!] Comando desconocido: {comando}")
            print("    Use 'python buscar_paquete.py help' para ver los comandos disponibles")
            return 1

    # Modo por defecto: buscar paquete
    print(f"[INFO] Buscando desde: {directorio_raiz}")
    print(f"[INFO] Buscando paquete: python_forestacion")
    print("")

    # Buscar el paquete
    paquetes = buscar_paquete(directorio_raiz, "python_forestacion")

    print("")
    if paquetes:
        print(f"[OK] Se encontraron {len(paquetes)} paquete(s):")
        for paquete in paquetes:
            print(f"  - {paquete}")

            # Mostrar estructura basica del paquete
            print(f"    Contenido:")
            try:
                contenido = os.listdir(paquete)
                for item in sorted(contenido)[:10]:  # Mostrar primeros 10 items
                    ruta_item = os.path.join(paquete, item)
                    if os.path.isdir(ruta_item):
                        print(f"      [DIR]  {item}")
                    else:
                        print(f"      [FILE] {item}")
                if len(contenido) > 10:
                    print(f"      ... y {len(contenido) - 10} items mas")
            except PermissionError:
                print(f"      [!] Sin permisos para leer el directorio")
    else:
        print("[!] No se encontro el paquete python_forestacion")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())


################################################################################
# DIRECTORIO: python_forestacion
################################################################################

# ==============================================================================
# ARCHIVO 4/69: __init__.py
# Directorio: python_forestacion
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 5/69: constantes.py
# Directorio: python_forestacion
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/constantes.py
# ==============================================================================


AGUA_MINIMA = 10
AGUA_INICIAL_PLANTACION = 500

# Riego
TEMP_MIN_RIEGO = 8
TEMP_MAX_RIEGO = 15
HUMEDAD_MAX_RIEGO = 50
INTERVALO_CONTROL_RIEGO = 2.5
INTERVALO_SENSOR_TEMPERATURA = 2.0
INTERVALO_SENSOR_HUMEDAD = 3.0

# Estaciones
MES_INICIO_VERANO = 12
MES_FIN_VERANO = 2

# Absorción de agua
ABSORCION_SEASONAL_VERANO = 5
ABSORCION_SEASONAL_INVIERNO = 2
ABSORCION_CONSTANTE_LECHUGA = 1
ABSORCION_CONSTANTE_ZANAHORIA = 2

# Crecimiento
CRECIMIENTO_PINO_POR_RIEGO = 0.10
CRECIMIENTO_OLIVO_POR_RIEGO = 0.01

# Superficies (m²)
SUPERFICIE_PINO = 2.0
SUPERFICIE_OLIVO = 1.5
SUPERFICIE_LECHUGA = 0.5
SUPERFICIE_ZANAHORIA = 0.3

# Agua inicial por cultivo
AGUA_INICIAL_PINO = 2
AGUA_INICIAL_OLIVO = 2
AGUA_INICIAL_LECHUGA = 1
AGUA_INICIAL_ZANAHORIA = 1

# Altura inicial (metros)
ALTURA_INICIAL_PINO = 0.5
ALTURA_INICIAL_OLIVO = 1.0

# Sensores - Rangos
TEMP_MIN = -25.0
TEMP_MAX = 50.0
HUMEDAD_MIN = 0.0
HUMEDAD_MAX = 100.0

# Persistencia
DIRECTORIO_DATOS = "data"


################################################################################
# DIRECTORIO: python_forestacion/entidades
################################################################################

# ==============================================================================
# ARCHIVO 6/69: __init__.py
# Directorio: python_forestacion/entidades
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/entidades/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: python_forestacion/entidades/cultivos
################################################################################

# ==============================================================================
# ARCHIVO 7/69: __init__.py
# Directorio: python_forestacion/entidades/cultivos
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/entidades/cultivos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 8/69: arbol.py
# Directorio: python_forestacion/entidades/cultivos
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/entidades/cultivos/arbol.py
# ==============================================================================



from python_forestacion.entidades.cultivos.cultivo import Cultivo


class Arbol(Cultivo):
    """Cultivo de tipo árbol con altura."""
    
    def __init__(self, agua: int, superficie: float, altura: float):
        super().__init__(agua, superficie)
        self._altura = altura
    
    def get_altura(self) -> float:
        return self._altura
    
    def set_altura(self, altura: float) -> None:
        self._altura = altura

# ==============================================================================
# ARCHIVO 9/69: cultivo.py
# Directorio: python_forestacion/entidades/cultivos
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/entidades/cultivos/cultivo.py
# ==============================================================================



from abc import ABC


class Cultivo(ABC):
    """Clase base para todos los cultivos."""
    
    def __init__(self, agua: int, superficie: float):
        self._agua = agua
        self._superficie = superficie
    
    def get_agua(self) -> int:
        return self._agua
    
    def set_agua(self, agua: int) -> None:
        self._agua = agua
    
    def get_superficie(self) -> float:
        return self._superficie
    
    def set_superficie(self, superficie: float) -> None:
        self._superficie = superficie

# ==============================================================================
# ARCHIVO 10/69: hortaliza.py
# Directorio: python_forestacion/entidades/cultivos
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/entidades/cultivos/hortaliza.py
# ==============================================================================



from python_forestacion.entidades.cultivos.cultivo import Cultivo


class Hortaliza(Cultivo):
    """Cultivo de tipo hortaliza."""
    
    def __init__(self, agua: int, superficie: float, invernadero: bool):
        super().__init__(agua, superficie)
        self._invernadero = invernadero
    
    def tiene_invernadero(self) -> bool:
        return self._invernadero
    
    def set_invernadero(self, invernadero: bool) -> None:
        self._invernadero = invernadero

# ==============================================================================
# ARCHIVO 11/69: lechuga.py
# Directorio: python_forestacion/entidades/cultivos
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/entidades/cultivos/lechuga.py
# ==============================================================================


from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import (
    AGUA_INICIAL_LECHUGA,
    SUPERFICIE_LECHUGA
)


class Lechuga(Hortaliza):
    """Hortaliza tipo Lechuga."""
    
    def __init__(self, variedad: str):
        super().__init__(
            agua=AGUA_INICIAL_LECHUGA,
            superficie=SUPERFICIE_LECHUGA,
            invernadero=True
        )
        self._variedad = variedad
    
    def get_variedad(self) -> str:
        return self._variedad
    
    def set_variedad(self, variedad: str) -> None:
        self._variedad = variedad

# ==============================================================================
# ARCHIVO 12/69: olivo.py
# Directorio: python_forestacion/entidades/cultivos
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/entidades/cultivos/olivo.py
# ==============================================================================


from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna
from python_forestacion.constantes import (
    AGUA_INICIAL_OLIVO,
    SUPERFICIE_OLIVO,
    ALTURA_INICIAL_OLIVO
)


class Olivo(Arbol):
    """Árbol tipo Olivo."""
    
    def __init__(self, tipo_aceituna: TipoAceituna):
        super().__init__(
            agua=AGUA_INICIAL_OLIVO,
            superficie=SUPERFICIE_OLIVO,
            altura=ALTURA_INICIAL_OLIVO
        )
        self._tipo_aceituna = tipo_aceituna
    
    def get_tipo_aceituna(self) -> TipoAceituna:
        return self._tipo_aceituna
    
    def set_tipo_aceituna(self, tipo: TipoAceituna) -> None:
        self._tipo_aceituna = tipo

# ==============================================================================
# ARCHIVO 13/69: pino.py
# Directorio: python_forestacion/entidades/cultivos
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/entidades/cultivos/pino.py
# ==============================================================================


from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.constantes import (
    AGUA_INICIAL_PINO,
    SUPERFICIE_PINO,
    ALTURA_INICIAL_PINO
)


class Pino(Arbol):
    """Árbol tipo Pino."""
    
    def __init__(self, variedad: str):
        super().__init__(
            agua=AGUA_INICIAL_PINO,
            superficie=SUPERFICIE_PINO,
            altura=ALTURA_INICIAL_PINO
        )
        self._variedad = variedad
    
    def get_variedad(self) -> str:
        return self._variedad
    
    def set_variedad(self, variedad: str) -> None:
        self._variedad = variedad

# ==============================================================================
# ARCHIVO 14/69: tipo_aceituna.py
# Directorio: python_forestacion/entidades/cultivos
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/entidades/cultivos/tipo_aceituna.py
# ==============================================================================



from enum import Enum


class TipoAceituna(Enum):
    """Tipos de aceitunas para olivos."""
    ARBEQUINA = "Arbequina"
    PICUAL = "Picual"
    MANZANILLA = "Manzanilla"

# ==============================================================================
# ARCHIVO 15/69: zanahoria.py
# Directorio: python_forestacion/entidades/cultivos
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/entidades/cultivos/zanahoria.py
# ==============================================================================


from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import (
    AGUA_INICIAL_ZANAHORIA,
    SUPERFICIE_ZANAHORIA
)


class Zanahoria(Hortaliza):
    """Hortaliza tipo Zanahoria."""
    
    def __init__(self, es_baby: bool):
        super().__init__(
            agua=AGUA_INICIAL_ZANAHORIA,
            superficie=SUPERFICIE_ZANAHORIA,
            invernadero=False
        )
        self._es_baby = es_baby
    
    def es_baby(self) -> bool:
        return self._es_baby
    
    def set_es_baby(self, es_baby: bool) -> None:
        self._es_baby = es_baby


################################################################################
# DIRECTORIO: python_forestacion/entidades/personal
################################################################################

# ==============================================================================
# ARCHIVO 16/69: __init__.py
# Directorio: python_forestacion/entidades/personal
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/entidades/personal/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 17/69: apto_medico.py
# Directorio: python_forestacion/entidades/personal
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/entidades/personal/apto_medico.py
# ==============================================================================

# python_forestacion/entidades/personal/apto_medico.py
"""
Entidad AptoMedico - Certificación médica.
"""

from datetime import date


class AptoMedico:
    """Certificación médica de un trabajador."""
    
    def __init__(self, fecha_emision: date, observaciones: str = ""):
        self._fecha_emision = fecha_emision
        self._observaciones = observaciones
    
    def get_fecha_emision(self) -> date:
        return self._fecha_emision
    
    def get_observaciones(self) -> str:
        return self._observaciones

# ==============================================================================
# ARCHIVO 18/69: herramienta.py
# Directorio: python_forestacion/entidades/personal
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/entidades/personal/herramienta.py
# ==============================================================================

# python_forestacion/entidades/personal/herramienta.py
"""
Entidad Herramienta - Herramienta de trabajo.
"""


class Herramienta:
    """Herramienta con certificación H&S."""
    
    def __init__(self, id_herramienta: int, nombre: str, certificacion_hs: bool):
        self._id = id_herramienta
        self._nombre = nombre
        self._certificacion_hs = certificacion_hs
    
    def get_id(self) -> int:
        return self._id
    
    def get_nombre(self) -> str:
        return self._nombre
    
    def tiene_certificacion_hs(self) -> bool:
        return self._certificacion_hs

# ==============================================================================
# ARCHIVO 19/69: tarea.py
# Directorio: python_forestacion/entidades/personal
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/entidades/personal/tarea.py
# ==============================================================================

# python_forestacion/entidades/personal/tarea.py
"""
Entidad Tarea - Tarea asignada a trabajador.
"""

from datetime import date
from enum import Enum


class EstadoTarea(Enum):
    """Estados posibles de una tarea."""
    PENDIENTE = "Pendiente"
    COMPLETADA = "Completada"


class Tarea:
    """Tarea asignada a un trabajador."""
    
    def __init__(self, id_tarea: int, descripcion: str, fecha_programada: date):
        self._id = id_tarea
        self._descripcion = descripcion
        self._fecha_programada = fecha_programada
        self._estado = EstadoTarea.PENDIENTE
    
    def get_id(self) -> int:
        return self._id
    
    def get_descripcion(self) -> str:
        return self._descripcion
    
    def get_fecha_programada(self) -> date:
        return self._fecha_programada
    
    def get_estado(self) -> EstadoTarea:
        return self._estado
    
    def marcar_completada(self) -> None:
        self._estado = EstadoTarea.COMPLETADA


# ==============================================================================
# ARCHIVO 20/69: trabajador.py
# Directorio: python_forestacion/entidades/personal
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/entidades/personal/trabajador.py
# ==============================================================================

# python_forestacion/entidades/personal/trabajador.py
"""
Entidad Trabajador - Trabajador agrícola.
"""

from typing import List, Optional
from python_forestacion.entidades.personal.tarea import Tarea
from python_forestacion.entidades.personal.apto_medico import AptoMedico


class Trabajador:
    """Trabajador con tareas y certificación médica."""
    
    def __init__(self, dni: int, nombre: str, tareas: List[Tarea], 
                 apto_medico: Optional[AptoMedico] = None):
        self._dni = dni
        self._nombre = nombre
        self._tareas = tareas
        self._apto_medico = apto_medico
    
    def get_dni(self) -> int:
        return self._dni
    
    def get_nombre(self) -> str:
        return self._nombre
    
    def get_tareas(self) -> List[Tarea]:
        return self._tareas
    
    def add_tarea(self, tarea: Tarea) -> None:
        self._tareas.append(tarea)
    
    def get_apto_medico(self) -> Optional[AptoMedico]:
        return self._apto_medico
    
    def set_apto_medico(self, apto: AptoMedico) -> None:
        self._apto_medico = apto
    
    def tiene_apto_medico(self) -> bool:
        return self._apto_medico is not None


################################################################################
# DIRECTORIO: python_forestacion/entidades/terrenos
################################################################################

# ==============================================================================
# ARCHIVO 21/69: __init__.py
# Directorio: python_forestacion/entidades/terrenos
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/entidades/terrenos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 22/69: plantacion.py
# Directorio: python_forestacion/entidades/terrenos
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/entidades/terrenos/plantacion.py
# ==============================================================================

# python_forestacion/entidades/terrenos/plantacion.py
"""
Entidad Plantacion - Conjunto de cultivos.
"""

from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo
    from python_forestacion.entidades.personal.trabajador import Trabajador


class Plantacion:
    """Representa una plantación agrícola."""
    
    def __init__(self, nombre: str, superficie: float):
        self._nombre = nombre
        self._superficie_total = superficie
        self._cultivos: List['Cultivo'] = []
        self._trabajadores: List['Trabajador'] = []
        self._agua_disponible = 0
    
    def get_nombre(self) -> str:
        return self._nombre
    
    def get_superficie_total(self) -> float:
        return self._superficie_total
    
    def get_cultivos(self) -> List['Cultivo']:
        return self._cultivos
    
    def add_cultivo(self, cultivo: 'Cultivo') -> None:
        self._cultivos.append(cultivo)
    
    def get_trabajadores(self) -> List['Trabajador']:
        return self._trabajadores
    
    def add_trabajador(self, trabajador: 'Trabajador') -> None:
        if trabajador not in self._trabajadores:
            self._trabajadores.append(trabajador)
    
    def get_agua_disponible(self) -> int:
        return self._agua_disponible
    
    def set_agua_disponible(self, agua: int) -> None:
        self._agua_disponible = agua
    
    def calcular_superficie_disponible(self) -> float:
        """Calcula superficie no ocupada por cultivos."""
        superficie_ocupada = sum(c.get_superficie() for c in self._cultivos)
        return self._superficie_total - superficie_ocupada

# ==============================================================================
# ARCHIVO 23/69: registro_florestal.py
# Directorio: python_forestacion/entidades/terrenos
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/entidades/terrenos/registro_florestal.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 24/69: registro_forestal.py
# Directorio: python_forestacion/entidades/terrenos
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/entidades/terrenos/registro_forestal.py
# ==============================================================================

# python_forestacion/entidades/terrenos/registro_forestal.py
"""
Entidad RegistroForestal - Registro completo persistible.
"""

from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion


class RegistroForestal:
    """Registro forestal completo con tierra y plantación."""
    
    def __init__(self, id_padron: int, tierra: Tierra, 
                 plantacion: Plantacion, propietario: str, avaluo: float):
        self._id_padron = id_padron
        self._tierra = tierra
        self._plantacion = plantacion
        self._propietario = propietario
        self._avaluo = avaluo
    
    def get_id_padron(self) -> int:
        return self._id_padron
    
    def get_tierra(self) -> Tierra:
        return self._tierra
    
    def get_plantacion(self) -> Plantacion:
        return self._plantacion
    
    def get_propietario(self) -> str:
        return self._propietario
    
    def get_avaluo(self) -> float:
        return self._avaluo

# ==============================================================================
# ARCHIVO 25/69: tierra.py
# Directorio: python_forestacion/entidades/terrenos
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/entidades/terrenos/tierra.py
# ==============================================================================

# python_forestacion/entidades/terrenos/tierra.py
"""
Entidad Tierra - Terreno catastral.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion


class Tierra:
    """Representa un terreno con padrón catastral."""
    
    def __init__(self, id_padron_catastral: int, superficie: float, domicilio: str):
        self._id_padron = id_padron_catastral
        self._superficie = superficie
        self._domicilio = domicilio
        self._finca: 'Plantacion' = None
    
    def get_id_padron(self) -> int:
        return self._id_padron
    
    def get_superficie(self) -> float:
        return self._superficie
    
    def get_domicilio(self) -> str:
        return self._domicilio
    
    def get_finca(self) -> 'Plantacion':
        return self._finca
    
    def set_finca(self, finca: 'Plantacion') -> None:
        self._finca = finca



################################################################################
# DIRECTORIO: python_forestacion/excepciones
################################################################################

# ==============================================================================
# ARCHIVO 26/69: __init__.py
# Directorio: python_forestacion/excepciones
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/excepciones/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 27/69: agua_agotada_exception.py
# Directorio: python_forestacion/excepciones
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/excepciones/agua_agotada_exception.py
# ==============================================================================

from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones.mensajes_exception import MensajesException


class AguaAgotadaException(ForestacionException):
    """
    Excepción lanzada cuando el agua disponible es insuficiente
    para cumplir con un requerimiento de riego.
    """

    def __init__(self, agua_disponible: int, agua_requerida: int) -> None:
        self._agua_disponible = agua_disponible
        self._agua_requerida = agua_requerida

        mensaje_usuario = MensajesException.AGUA_AGOTADA_USUARIO
        mensaje_tecnico = (
            f"{MensajesException.AGUA_AGOTADA_TECNICO}: "
            f"disponible={agua_disponible}L, requerida={agua_requerida}L"
        )

        super().__init__(mensaje_usuario, mensaje_tecnico)

    @property
    def agua_disponible(self) -> int:
        """Cantidad actual de agua disponible (en litros)."""
        return self._agua_disponible

    @property
    def agua_requerida(self) -> int:
        """Cantidad de agua requerida (en litros)."""
        return self._agua_requerida

    def __str__(self) -> str:
        """Representación legible de la excepción."""
        return (
            f"AguaAgotadaException("
            f"disponible={self._agua_disponible}L, "
            f"requerida={self._agua_requerida}L)"
        )


# ==============================================================================
# ARCHIVO 28/69: forestacion_exception.py
# Directorio: python_forestacion/excepciones
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/excepciones/forestacion_exception.py
# ==============================================================================

class ForestacionException(Exception):
    """
    Excepción base del sistema forestal.
    
    Proporciona soporte para mensajes separados (usuario y técnico)
    y permite el encadenamiento opcional de causas.
    """

    def __init__(
        self,
        mensaje_usuario: str,
        mensaje_tecnico: str,
        causa: Exception | None = None
    ) -> None:
        self._mensaje_usuario = mensaje_usuario
        self._mensaje_tecnico = mensaje_tecnico
        self._causa = causa
        super().__init__(mensaje_tecnico)

    @property
    def mensaje_usuario(self) -> str:
        """Mensaje amigable destinado a mostrar al usuario final."""
        return self._mensaje_usuario

    @property
    def mensaje_tecnico(self) -> str:
        """Mensaje detallado para logs o diagnóstico técnico."""
        return self._mensaje_tecnico

    @property
    def causa(self) -> Exception | None:
        """Causa original que produjo la excepción, si existe."""
        return self._causa

    def __str__(self) -> str:
        """Devuelve el mensaje técnico (útil para logging estándar)."""
        return self._mensaje_tecnico

    def __repr__(self) -> str:
        """Representación detallada para debugging."""
        return (
            f"{self.__class__.__name__}("
            f"usuario='{self._mensaje_usuario}', "
            f"tecnico='{self._mensaje_tecnico}', "
            f"causa={repr(self._causa)})"
        )

    def get_full_message(self) -> str:
        """Construye un mensaje combinado y legible."""
        partes = [
            f"Usuario: {self._mensaje_usuario}",
            f"Técnico: {self._mensaje_tecnico}"
        ]
        if self._causa:
            partes.append(f"Causa: {self._causa}")
        return "\n".join(partes)


# ==============================================================================
# ARCHIVO 29/69: mensajes_exception.py
# Directorio: python_forestacion/excepciones
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/excepciones/mensajes_exception.py
# ==============================================================================

class MensajesException:
    """
    Contenedor centralizado de mensajes de error del sistema de forestación.

    Distingue entre mensajes orientados al usuario final (amigables)
    y mensajes técnicos para registro o depuración.
    """

    # ==========================================================
    # 🌱 Superficie
    # ==========================================================
    SUPERFICIE_INSUFICIENTE_USUARIO = (
        "No hay suficiente superficie disponible para completar la plantación."
    )
    SUPERFICIE_INSUFICIENTE_TECNICO = (
        "La superficie requerida excede la disponible en el sistema."
    )

    # ==========================================================
    # 💧 Agua
    # ==========================================================
    AGUA_AGOTADA_USUARIO = (
        "El agua disponible en la plantación se ha agotado. "
        "Revise el sistema de riego o las reservas."
    )
    AGUA_AGOTADA_TECNICO = (
        "Cantidad de agua insuficiente para completar la operación de riego."
    )

    # ==========================================================
    # 💾 Persistencia
    # ==========================================================
    PERSISTENCIA_ERROR_USUARIO = (
        "Se produjo un error al guardar o recuperar los datos. "
        "Por favor, intente nuevamente."
    )
    PERSISTENCIA_ERROR_TECNICO = (
        "Error en la operación de persistencia (por ejemplo, con Pickle o acceso a disco)."
    )

    # ==========================================================
    # ⚙️ Genéricos / Futuros
    # ==========================================================
    ERROR_DESCONOCIDO_USUARIO = "Ocurrió un error inesperado en el sistema."
    ERROR_DESCONOCIDO_TECNICO = "Excepción no manejada detectada en la capa de aplicación."


# ==============================================================================
# ARCHIVO 30/69: persistencia_exception.py
# Directorio: python_forestacion/excepciones
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/excepciones/persistencia_exception.py
# ==============================================================================

from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones.mensajes_exception import MensajesException


class PersistenciaException(ForestacionException):
    """
    Excepción lanzada cuando ocurre un error en la capa de persistencia de datos.
    
    Aporta contexto adicional sobre la operación que falló (por ejemplo: 'guardar', 'leer', 'actualizar').
    """

    def __init__(self, operacion: str, causa: Exception | None = None) -> None:
        self._operacion = operacion

        mensaje_usuario = MensajesException.PERSISTENCIA_ERROR_USUARIO
        mensaje_tecnico = (
            f"{MensajesException.PERSISTENCIA_ERROR_TECNICO} "
            f"during operation '{operacion}'"
        )

        super().__init__(mensaje_usuario, mensaje_tecnico, causa)

    @property
    def operacion(self) -> str:
        """Operación de persistencia que produjo el error (ej. 'insertar', 'actualizar', 'eliminar')."""
        return self._operacion

    def __str__(self) -> str:
        """Devuelve una descripción técnica legible del error."""
        return f"PersistenciaException(operacion='{self._operacion}') → {self.mensaje_tecnico}"


# ==============================================================================
# ARCHIVO 31/69: superficie_insuficiente_exception.py
# Directorio: python_forestacion/excepciones
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/excepciones/superficie_insuficiente_exception.py
# ==============================================================================

from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones.mensajes_exception import MensajesException


class SuperficieInsuficienteException(ForestacionException):
    """Excepción lanzada cuando la superficie disponible es insuficiente."""
    
    def __init__(self, superficie_requerida: float, superficie_disponible: float):
        self._superficie_requerida = superficie_requerida
        self._superficie_disponible = superficie_disponible
        
        super().__init__(
            MensajesException.SUPERFICIE_INSUFICIENTE_USUARIO,
            f"{MensajesException.SUPERFICIE_INSUFICIENTE_TECNICO}: "
            f"requerida={superficie_requerida}m², disponible={superficie_disponible}m²"
        )
    
    def get_superficie_requerida(self) -> float:
        return self._superficie_requerida
    
    def get_superficie_disponible(self) -> float:
        return self._superficie_disponible




################################################################################
# DIRECTORIO: python_forestacion/patrones
################################################################################

# ==============================================================================
# ARCHIVO 32/69: __init__.py
# Directorio: python_forestacion/patrones
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/patrones/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: python_forestacion/patrones/factory
################################################################################

# ==============================================================================
# ARCHIVO 33/69: __init__.py
# Directorio: python_forestacion/patrones/factory
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/patrones/factory/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 34/69: cultivo_factory.py
# Directorio: python_forestacion/patrones/factory
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/patrones/factory/cultivo_factory.py
# ==============================================================================

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class CultivoFactory:
    """Factory para crear instancias de cultivos."""
    
    @staticmethod
    def crear_cultivo(especie: str) -> 'Cultivo':
        """
        Crea un cultivo según la especie.
        
        Args:
            especie: Tipo de cultivo ("Pino", "Olivo", "Lechuga", "Zanahoria")
            
        Returns:
            Instancia del cultivo solicitado
            
        Raises:
            ValueError: Si la especie es desconocida
        """
        factories = {
            "Pino": CultivoFactory._crear_pino,
            "Olivo": CultivoFactory._crear_olivo,
            "Lechuga": CultivoFactory._crear_lechuga,
            "Zanahoria": CultivoFactory._crear_zanahoria
        }
        
        if especie not in factories:
            raise ValueError(f"Especie desconocida: {especie}")
        
        return factories[especie]()
    
    @staticmethod
    def _crear_pino() -> 'Cultivo':
        from python_forestacion.entidades.cultivos.pino import Pino
        return Pino(variedad="Paraná")
    
    @staticmethod
    def _crear_olivo() -> 'Cultivo':
        from python_forestacion.entidades.cultivos.olivo import Olivo
        from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna
        return Olivo(tipo_aceituna=TipoAceituna.ARBEQUINA)
    
    @staticmethod
    def _crear_lechuga() -> 'Cultivo':
        from python_forestacion.entidades.cultivos.lechuga import Lechuga
        return Lechuga(variedad="Crespa")
    
    @staticmethod
    def _crear_zanahoria() -> 'Cultivo':
        from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
        return Zanahoria(es_baby=False)


################################################################################
# DIRECTORIO: python_forestacion/patrones/observer
################################################################################

# ==============================================================================
# ARCHIVO 35/69: __init__.py
# Directorio: python_forestacion/patrones/observer
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/patrones/observer/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 36/69: observable.py
# Directorio: python_forestacion/patrones/observer
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/patrones/observer/observable.py
# ==============================================================================

from abc import ABC
from typing import Generic, TypeVar, List
from threading import Lock
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.patrones.observer.observer import Observer

T = TypeVar("T")


class Observable(Generic[T], ABC):
    """
    Clase base para objetos observables que emiten eventos de tipo T.

    Implementa el patrón Observer, permitiendo que múltiples observadores
    se suscriban y reciban notificaciones cuando ocurre un evento.
    """

    def __init__(self) -> None:
        self._observadores: List["Observer[T]"] = []
        self._lock = Lock()  # 🔒 Protege el acceso concurrente a la lista

    def agregar_observador(self, observador: "Observer[T]") -> None:
        """Agrega un observador, evitando duplicados."""
        with self._lock:
            if observador not in self._observadores:
                self._observadores.append(observador)
                # print(f"[OBSERVABLE] Observador agregado: {observador.__class__.__name__}")

    def remover_observador(self, observador: "Observer[T]") -> None:
        """Remueve un observador si está registrado."""
        with self._lock:
            if observador in self._observadores:
                self._observadores.remove(observador)
                # print(f"[OBSERVABLE] Observador removido: {observador.__class__.__name__}")

    def notificar_observadores(self, evento: T) -> None:
        """Notifica a todos los observadores con el evento generado."""
        # Copia local para evitar problemas si la lista cambia durante la iteración
        with self._lock:
            observadores_snapshot = list(self._observadores)

        for observador in observadores_snapshot:
            try:
                observador.actualizar(evento)
            except Exception as e:
                # Evita que un error en un observador rompa la notificación global
                print(f"[ERROR] Falló notificación a {observador.__class__.__name__}: {e}")


# ==============================================================================
# ARCHIVO 37/69: observer.py
# Directorio: python_forestacion/patrones/observer
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/patrones/observer/observer.py
# ==============================================================================

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class Observer(Generic[T], ABC):
    """
    Interfaz base para observadores que reciben eventos de tipo T.

    Cualquier clase que herede de esta debe implementar el método `actualizar`,
    que será invocado por un Observable cuando ocurra un evento.
    """

    @abstractmethod
    def actualizar(self, evento: T) -> None:
        """
        Método llamado por el Observable cuando se produce un evento.

        Args:
            evento: Dato o información del evento (tipo genérico T).
        """
        raise NotImplementedError("El observador debe implementar el método 'actualizar'.")

    def __repr__(self) -> str:
        """Representación útil para debugging."""
        return f"{self.__class__.__name__}()"



################################################################################
# DIRECTORIO: python_forestacion/patrones/observer/eventos
################################################################################

# ==============================================================================
# ARCHIVO 38/69: __init__.py
# Directorio: python_forestacion/patrones/observer/eventos
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/patrones/observer/eventos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 39/69: evento_sensor.py
# Directorio: python_forestacion/patrones/observer/eventos
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/patrones/observer/eventos/evento_sensor.py
# ==============================================================================




################################################################################
# DIRECTORIO: python_forestacion/patrones/singleton
################################################################################

# ==============================================================================
# ARCHIVO 40/69: __init__.py
# Directorio: python_forestacion/patrones/singleton
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/patrones/singleton/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: python_forestacion/patrones/strategy
################################################################################

# ==============================================================================
# ARCHIVO 41/69: __init__.py
# Directorio: python_forestacion/patrones/strategy
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/patrones/strategy/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 42/69: absorcion_agua_strategy.py
# Directorio: python_forestacion/patrones/strategy
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/patrones/strategy/absorcion_agua_strategy.py
# ==============================================================================

from abc import ABC, abstractmethod
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class AbsorcionAguaStrategy(ABC):
    """
    Estrategia abstracta para calcular la absorción de agua de un cultivo.

    Esta clase define la interfaz común que deben implementar todas las
    estrategias concretas de absorción (por ejemplo, según tipo de cultivo,
    etapa de crecimiento o condiciones ambientales).
    """

    @abstractmethod
    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: "Cultivo",
    ) -> int:
        """
        Calcula la cantidad de litros de agua absorbidos por el cultivo.

        Args:
            fecha: Fecha actual.
            temperatura: Temperatura ambiente (°C).
            humedad: Humedad relativa del aire (%).
            cultivo: Instancia del cultivo que absorbe el agua.

        Returns:
            int: Litros de agua absorbidos.
        """
        raise NotImplementedError("La estrategia debe implementar 'calcular_absorcion'.")

    def __repr__(self) -> str:
        """Representación útil para depuración."""
        return f"{self.__class__.__name__}()"



################################################################################
# DIRECTORIO: python_forestacion/patrones/strategy/impl
################################################################################

# ==============================================================================
# ARCHIVO 43/69: __init__.py
# Directorio: python_forestacion/patrones/strategy/impl
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/patrones/strategy/impl/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 44/69: absorcion_constante_strategy.py
# Directorio: python_forestacion/patrones/strategy/impl
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/patrones/strategy/impl/absorcion_constante_strategy.py
# ==============================================================================

from datetime import date
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy


class AbsorcionConstanteStrategy(AbsorcionAguaStrategy):
    """Absorción constante independiente de la estación."""
    
    def __init__(self, cantidad_constante: int):
        self._cantidad = cantidad_constante
    
    def calcular_absorcion(self, fecha: date, temperatura: float,
                          humedad: float, cultivo) -> int:
        return self._cantidad

# ==============================================================================
# ARCHIVO 45/69: absorcion_seasonal_strategy.py
# Directorio: python_forestacion/patrones/strategy/impl
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/patrones/strategy/impl/absorcion_seasonal_strategy.py
# ==============================================================================

from datetime import date
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
from python_forestacion.constantes import (
    MES_INICIO_VERANO,
    MES_FIN_VERANO,
    ABSORCION_SEASONAL_VERANO,
    ABSORCION_SEASONAL_INVIERNO
)


class AbsorcionSeasonalStrategy(AbsorcionAguaStrategy):
    """Absorción diferenciada por estación del año."""
    
    def calcular_absorcion(self, fecha: date, temperatura: float, 
                          humedad: float, cultivo) -> int:
        mes = fecha.month
        
        # Verano: Diciembre, Enero, Febrero (hemisferio sur)
        if mes >= MES_INICIO_VERANO or mes <= MES_FIN_VERANO:
            return ABSORCION_SEASONAL_VERANO
        else:
            return ABSORCION_SEASONAL_INVIERNO


################################################################################
# DIRECTORIO: python_forestacion/riego
################################################################################

# ==============================================================================
# ARCHIVO 46/69: __init__.py
# Directorio: python_forestacion/riego
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/riego/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: python_forestacion/riego/control
################################################################################

# ==============================================================================
# ARCHIVO 47/69: __init__.py
# Directorio: python_forestacion/riego/control
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/riego/control/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 48/69: control_riego_task.py
# Directorio: python_forestacion/riego/control
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/riego/control/control_riego_task.py
# ==============================================================================

import threading
import time
from typing import Optional, TYPE_CHECKING

from python_forestacion.patrones.observer.observer import Observer
from python_forestacion.constantes import (
    INTERVALO_CONTROL_RIEGO,
    TEMP_MIN_RIEGO,
    TEMP_MAX_RIEGO,
    HUMEDAD_MAX_RIEGO
)

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion
    from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
    from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
    from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask


class ControlRiegoTask(threading.Thread, Observer[float]):
    """
    Controlador automático de riego basado en condiciones ambientales.

    Observa lecturas de sensores de temperatura y humedad,
    y activa el riego cuando las condiciones lo requieren.
    """

    def __init__(
        self,
        sensor_temperatura: "TemperaturaReaderTask",
        sensor_humedad: "HumedadReaderTask",
        plantacion: "Plantacion",
        plantacion_service: "PlantacionService"
    ):
        super().__init__(daemon=True)

        self._plantacion = plantacion
        self._plantacion_service = plantacion_service

        self._ultima_temperatura: Optional[float] = None
        self._ultima_humedad: Optional[float] = None
        self._detenido = threading.Event()

        # Registro como observador (patrón Observer)
        sensor_temperatura.agregar_observador(self)
        sensor_humedad.agregar_observador(self)

    def actualizar(self, evento: float) -> None:
        """
        Recibe eventos de sensores.

        Args:
            evento: Lectura del sensor (puede ser temperatura o humedad)
        """
        if -50 <= evento <= 70:  # Temperatura (más rango por seguridad)
            self._ultima_temperatura = evento
        elif 0 <= evento <= 100:  # Humedad
            self._ultima_humedad = evento
        else:
            print(f"[WARN] Lectura fuera de rango ignorada: {evento}")

    def run(self) -> None:
        """Bucle principal de control automático."""
        print("[CONTROL] Riego automático iniciado ✅")

        while not self._detenido.is_set():
            try:
                if self._debe_regar():
                    self._ejecutar_riego()
            except Exception as e:
                print(f"[ERROR] Fallo en ControlRiegoTask: {e}")

            time.sleep(INTERVALO_CONTROL_RIEGO)

        print("[CONTROL] Riego automático detenido 📴")

    def _debe_regar(self) -> bool:
        """
        Evalúa si deben cumplirse las condiciones para regar.

        Returns:
            bool: True si debe activarse el riego.
        """
        if self._ultima_temperatura is None or self._ultima_humedad is None:
            return False

        temp_ok = TEMP_MIN_RIEGO <= self._ultima_temperatura <= TEMP_MAX_RIEGO
        humedad_ok = self._ultima_humedad < HUMEDAD_MAX_RIEGO

        return temp_ok and humedad_ok

    def _ejecutar_riego(self) -> None:
        """Ejecuta la acción de riego sobre la plantación."""
        print(
            f"\n[RIEGO AUTO] T={self._ultima_temperatura:.1f}°C | "
            f"H={self._ultima_humedad:.1f}% → REGANDO 💧"
        )
        self._plantacion_service.regar(self._plantacion)

    def detener(self) -> None:
        """Detiene el hilo de forma controlada."""
        self._detenido.set()



################################################################################
# DIRECTORIO: python_forestacion/riego/sensores
################################################################################

# ==============================================================================
# ARCHIVO 49/69: __init__.py
# Directorio: python_forestacion/riego/sensores
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/riego/sensores/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 50/69: humedad_reader_task.py
# Directorio: python_forestacion/riego/sensores
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/riego/sensores/humedad_reader_task.py
# ==============================================================================

import threading
import time
import random
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.constantes import (
    INTERVALO_SENSOR_HUMEDAD,
    HUMEDAD_MIN,
    HUMEDAD_MAX
)


class HumedadReaderTask(threading.Thread, Observable[float]):
    """Thread que simula lecturas de humedad y notifica a los observadores."""

    def __init__(self):
        super().__init__(daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()

    def run(self) -> None:
        """Bucle principal del sensor."""
        print("[SENSOR] Humedad iniciado 💧")

        try:
            while not self._detenido.is_set():
                humedad = self._leer_humedad()
                print(f"[SENSOR] Humedad actual: {humedad}%")
                self.notificar_observadores(humedad)
                time.sleep(INTERVALO_SENSOR_HUMEDAD)
        except Exception as e:
            print(f"[ERROR] Fallo en HumedadReaderTask: {e}")
        finally:
            print("[SENSOR] Humedad detenido 📴")

    def _leer_humedad(self) -> float:
        """Simula la lectura del sensor de humedad."""
        return round(random.uniform(HUMEDAD_MIN, HUMEDAD_MAX), 1)

    def detener(self) -> None:
        """Detiene el hilo de forma controlada."""
        self._detenido.set()


# ==============================================================================
# ARCHIVO 51/69: temperatura_reader_task.py
# Directorio: python_forestacion/riego/sensores
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/riego/sensores/temperatura_reader_task.py
# ==============================================================================

import threading
import time
import random
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.constantes import (
    INTERVALO_SENSOR_TEMPERATURA,
    TEMP_MIN,
    TEMP_MAX
)


class TemperaturaReaderTask(threading.Thread, Observable[float]):
    """Thread que simula lecturas de temperatura y notifica a los observadores."""

    def __init__(self):
        super().__init__(daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()

    def run(self) -> None:
        """Bucle principal del sensor."""
        print("[SENSOR] Temperatura iniciado 🌡️")

        try:
            while not self._detenido.is_set():
                temperatura = self._leer_temperatura()
                print(f"[SENSOR] Temperatura actual: {temperatura}°C")
                self.notificar_observadores(temperatura)
                time.sleep(INTERVALO_SENSOR_TEMPERATURA)
        except Exception as e:
            print(f"[ERROR] Fallo en TemperaturaReaderTask: {e}")
        finally:
            print("[SENSOR] Temperatura detenido 📴")

    def _leer_temperatura(self) -> float:
        """Simula la lectura del sensor."""
        return round(random.uniform(TEMP_MIN, TEMP_MAX), 1)

    def detener(self) -> None:
        """Detiene el hilo de forma controlada."""
        self._detenido.set()



################################################################################
# DIRECTORIO: python_forestacion/servicios
################################################################################

# ==============================================================================
# ARCHIVO 52/69: __init__.py
# Directorio: python_forestacion/servicios
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/servicios/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: python_forestacion/servicios/cultivos
################################################################################

# ==============================================================================
# ARCHIVO 53/69: __init__.py
# Directorio: python_forestacion/servicios/cultivos
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/servicios/cultivos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 54/69: arbol_service.py
# Directorio: python_forestacion/servicios/cultivos
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/servicios/cultivos/arbol_service.py
# ==============================================================================

from typing import TYPE_CHECKING
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.arbol import Arbol


class ArbolService(CultivoService):
    """Servicio base para árboles."""
    
    def mostrar_datos(self, cultivo: 'Arbol') -> None:
        """Muestra datos del árbol incluyendo altura."""
        super().mostrar_datos(cultivo)
        print(f"  Altura: {cultivo.get_altura():.2f}m")


# ==============================================================================
# ARCHIVO 55/69: cultivo_service.py
# Directorio: python_forestacion/servicios/cultivos
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/servicios/cultivos/cultivo_service.py
# ==============================================================================

from datetime import date
from typing import TYPE_CHECKING
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class CultivoService:
    """Servicio base para operaciones sobre cultivos."""
    
    def __init__(self, estrategia_absorcion: AbsorcionAguaStrategy):
        self._estrategia_absorcion = estrategia_absorcion
    
    def absorver_agua(self, cultivo: 'Cultivo', fecha: date = None,
                     temperatura: float = 20.0, humedad: float = 50.0) -> int:
        """
        Calcula agua absorbida usando la estrategia inyectada.
        
        Returns:
            Litros absorbidos
        """
        if fecha is None:
            fecha = date.today()
        
        litros = self._estrategia_absorcion.calcular_absorcion(
            fecha, temperatura, humedad, cultivo
        )
        
        agua_actual = cultivo.get_agua()
        cultivo.set_agua(agua_actual + litros)
        
        return litros
    
    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        """Muestra datos básicos del cultivo."""
        print(f"  Agua: {cultivo.get_agua()}L")
        print(f"  Superficie: {cultivo.get_superficie()}m2")


# ==============================================================================
# ARCHIVO 56/69: cultivo_service_registry.py
# Directorio: python_forestacion/servicios/cultivos
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/servicios/cultivos/cultivo_service_registry.py
# ==============================================================================

from threading import Lock
from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos.pino_service import PinoService
from python_forestacion.servicios.cultivos.olivo_service import OlivoService
from python_forestacion.servicios.cultivos.lechuga_service import LechugaService
from python_forestacion.servicios.cultivos.zanahoria_service import ZanahoriaService

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo
    from python_forestacion.entidades.cultivos.pino import Pino
    from python_forestacion.entidades.cultivos.olivo import Olivo
    from python_forestacion.entidades.cultivos.lechuga import Lechuga
    from python_forestacion.entidades.cultivos.zanahoria import Zanahoria


class CultivoServiceRegistry:
    """
    Registry de servicios de cultivos implementando Singleton.
    Thread-safe con double-checked locking.
    """
    
    _instance = None
    _lock = Lock()
    
    def __new__(cls):
        """Implementación thread-safe de Singleton."""
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        """Inicializa servicios y registros solo una vez."""
        if not hasattr(self, '_initialized'):
            # Servicios
            self._pino_service = PinoService()
            self._olivo_service = OlivoService()
            self._lechuga_service = LechugaService()
            self._zanahoria_service = ZanahoriaService()
            
            # Registry de handlers
            self._absorber_agua_handlers = {}
            self._mostrar_datos_handlers = {}
            self._crecer_handlers = {}
            
            self._registrar_handlers()
            self._initialized = True
    
    def _registrar_handlers(self):
        """Registra handlers por tipo de cultivo."""
        from python_forestacion.entidades.cultivos.pino import Pino
        from python_forestacion.entidades.cultivos.olivo import Olivo
        from python_forestacion.entidades.cultivos.lechuga import Lechuga
        from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
        
        # Absorber agua
        self._absorber_agua_handlers[Pino] = self._absorber_agua_pino
        self._absorber_agua_handlers[Olivo] = self._absorber_agua_olivo
        self._absorber_agua_handlers[Lechuga] = self._absorber_agua_lechuga
        self._absorber_agua_handlers[Zanahoria] = self._absorber_agua_zanahoria
        
        # Mostrar datos
        self._mostrar_datos_handlers[Pino] = self._mostrar_datos_pino
        self._mostrar_datos_handlers[Olivo] = self._mostrar_datos_olivo
        self._mostrar_datos_handlers[Lechuga] = self._mostrar_datos_lechuga
        self._mostrar_datos_handlers[Zanahoria] = self._mostrar_datos_zanahoria
        
        # Crecer (solo árboles)
        self._crecer_handlers[Pino] = self._crecer_pino
        self._crecer_handlers[Olivo] = self._crecer_olivo
    
    # Handlers específicos
    def _absorber_agua_pino(self, cultivo):
        return self._pino_service.absorver_agua(cultivo)
    
    def _absorber_agua_olivo(self, cultivo):
        return self._olivo_service.absorver_agua(cultivo)
    
    def _absorber_agua_lechuga(self, cultivo):
        return self._lechuga_service.absorver_agua(cultivo)
    
    def _absorber_agua_zanahoria(self, cultivo):
        return self._zanahoria_service.absorver_agua(cultivo)
    
    def _mostrar_datos_pino(self, cultivo):
        self._pino_service.mostrar_datos(cultivo)
    
    def _mostrar_datos_olivo(self, cultivo):
        self._olivo_service.mostrar_datos(cultivo)
    
    def _mostrar_datos_lechuga(self, cultivo):
        self._lechuga_service.mostrar_datos(cultivo)
    
    def _mostrar_datos_zanahoria(self, cultivo):
        self._zanahoria_service.mostrar_datos(cultivo)
    
    def _crecer_pino(self, cultivo):
        self._pino_service.crecer(cultivo)
    
    def _crecer_olivo(self, cultivo):
        self._olivo_service.crecer(cultivo)
    
    # API Pública con dispatch polimórfico
    def absorber_agua(self, cultivo: 'Cultivo') -> int:
        """Dispatch polimórfico para absorber agua."""
        tipo = type(cultivo)
        if tipo not in self._absorber_agua_handlers:
            raise ValueError(f"Tipo de cultivo desconocido: {tipo.__name__}")
        return self._absorber_agua_handlers[tipo](cultivo)
    
    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        """Dispatch polimórfico para mostrar datos."""
        tipo = type(cultivo)
        if tipo not in self._mostrar_datos_handlers:
            raise ValueError(f"Tipo de cultivo desconocido: {tipo.__name__}")
        self._mostrar_datos_handlers[tipo](cultivo)
    
    def crecer(self, cultivo: 'Cultivo') -> None:
        """Dispatch polimórfico para crecimiento (solo árboles)."""
        tipo = type(cultivo)
        if tipo in self._crecer_handlers:
            self._crecer_handlers[tipo](cultivo)
    
    @classmethod
    def get_instance(cls):
        """Obtiene la instancia única del registry."""
        return cls()

# ==============================================================================
# ARCHIVO 57/69: lechuga_service.py
# Directorio: python_forestacion/servicios/cultivos
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/servicios/cultivos/lechuga_service.py
# ==============================================================================

from typing import TYPE_CHECKING
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from python_forestacion.constantes import ABSORCION_CONSTANTE_LECHUGA

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.lechuga import Lechuga


class LechugaService(CultivoService):
    """Servicio para operaciones sobre Lechuga."""
    
    def __init__(self):
        super().__init__(AbsorcionConstanteStrategy(ABSORCION_CONSTANTE_LECHUGA))
    
    def mostrar_datos(self, cultivo: 'Lechuga') -> None:
        """Muestra datos específicos de la lechuga."""
        super().mostrar_datos(cultivo)
        print(f"  Variedad: {cultivo.get_variedad()}")
        print(f"  Invernadero: {'Si' if cultivo.tiene_invernadero() else 'No'}")


# ==============================================================================
# ARCHIVO 58/69: olivo_service.py
# Directorio: python_forestacion/servicios/cultivos
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/servicios/cultivos/olivo_service.py
# ==============================================================================

from typing import TYPE_CHECKING
from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from python_forestacion.constantes import CRECIMIENTO_OLIVO_POR_RIEGO

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.olivo import Olivo


class OlivoService(ArbolService):
    """Servicio para operaciones sobre Olivo."""
    
    def __init__(self):
        super().__init__(AbsorcionSeasonalStrategy())
    
    def crecer(self, olivo: 'Olivo') -> None:
        """Hace crecer el olivo según constante."""
        altura_actual = olivo.get_altura()
        olivo.set_altura(altura_actual + CRECIMIENTO_OLIVO_POR_RIEGO)
    
    def mostrar_datos(self, cultivo: 'Olivo') -> None:
        """Muestra datos específicos del olivo."""
        super().mostrar_datos(cultivo)
        print(f"  Tipo Aceituna: {cultivo.get_tipo_aceituna().value}")


# ==============================================================================
# ARCHIVO 59/69: pino_service.py
# Directorio: python_forestacion/servicios/cultivos
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/servicios/cultivos/pino_service.py
# ==============================================================================


from typing import TYPE_CHECKING
from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from python_forestacion.constantes import CRECIMIENTO_PINO_POR_RIEGO

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.pino import Pino


class PinoService(ArbolService):
    """Servicio para operaciones sobre Pino."""
    
    def __init__(self):
        super().__init__(AbsorcionSeasonalStrategy())
    
    def crecer(self, pino: 'Pino') -> None:
        """Hace crecer el pino según constante."""
        altura_actual = pino.get_altura()
        pino.set_altura(altura_actual + CRECIMIENTO_PINO_POR_RIEGO)
    
    def mostrar_datos(self, cultivo: 'Pino') -> None:
        """Muestra datos específicos del pino."""
        super().mostrar_datos(cultivo)
        print(f"  Variedad: {cultivo.get_variedad()}")



# ==============================================================================
# ARCHIVO 60/69: zanahoria_service.py
# Directorio: python_forestacion/servicios/cultivos
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/servicios/cultivos/zanahoria_service.py
# ==============================================================================

from typing import TYPE_CHECKING
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from python_forestacion.constantes import ABSORCION_CONSTANTE_ZANAHORIA

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.zanahoria import Zanahoria


class ZanahoriaService(CultivoService):
    """Servicio para operaciones sobre Zanahoria."""
    
    def __init__(self):
        super().__init__(AbsorcionConstanteStrategy(ABSORCION_CONSTANTE_ZANAHORIA))
    
    def mostrar_datos(self, cultivo: 'Zanahoria') -> None:
        """Muestra datos específicos de la zanahoria."""
        super().mostrar_datos(cultivo)
        print(f"  Baby Carrot: {'Si' if cultivo.es_baby() else 'No'}")




################################################################################
# DIRECTORIO: python_forestacion/servicios/negocio
################################################################################

# ==============================================================================
# ARCHIVO 61/69: __init__.py
# Directorio: python_forestacion/servicios/negocio
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/servicios/negocio/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 62/69: fincas_service.py
# Directorio: python_forestacion/servicios/negocio
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/servicios/negocio/fincas_service.py
# ==============================================================================


from typing import List, Type, TYPE_CHECKING
from python_forestacion.servicios.negocio.paquete import Paquete

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class FincasService:
    """Servicio de alto nivel para operaciones en fincas."""
    
    @staticmethod
    def cosechar_por_tipo(plantacion: 'Plantacion', 
                         tipo_cultivo: Type['Cultivo']) -> Paquete['Cultivo']:
        """
        Cosecha selectiva por tipo de cultivo.
        
        Args:
            plantacion: Plantación a cosechar
            tipo_cultivo: Tipo de cultivo a cosechar
            
        Returns:
            Paquete con cultivos del tipo especificado
        """
        paquete = Paquete[tipo_cultivo]()
        
        for cultivo in plantacion.get_cultivos():
            if isinstance(cultivo, tipo_cultivo):
                paquete.agregar(cultivo)
        
        print(f"[COSECHA] Empaquetados {paquete.cantidad()} {tipo_cultivo.__name__}(s)")
        return paquete
    
    @staticmethod
    def mostrar_paquete(paquete: Paquete, nombre_tipo: str) -> None:
        """Muestra el contenido de un paquete."""
        print(f"\n--- Paquete de {nombre_tipo} ---")
        print(f"Cantidad: {paquete.cantidad()}")
        
        from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
        registry = CultivoServiceRegistry.get_instance()
        
        for i, cultivo in enumerate(paquete.get_contenido(), 1):
            print(f"\n{nombre_tipo} #{i}:")
            registry.mostrar_datos(cultivo)


# ==============================================================================
# ARCHIVO 63/69: paquete.py
# Directorio: python_forestacion/servicios/negocio
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/servicios/negocio/paquete.py
# ==============================================================================


from typing import TypeVar, Generic, List

T = TypeVar('T')


class Paquete(Generic[T]):
    """Paquete genérico tipo-seguro para empaquetar cultivos."""
    
    def __init__(self):
        self._contenido: List[T] = []
    
    def agregar(self, item: T) -> None:
        """Agrega un item al paquete."""
        self._contenido.append(item)
    
    def get_contenido(self) -> List[T]:
        """Obtiene el contenido del paquete."""
        return self._contenido
    
    def cantidad(self) -> int:
        """Cantidad de items en el paquete."""
        return len(self._contenido)




################################################################################
# DIRECTORIO: python_forestacion/servicios/personal
################################################################################

# ==============================================================================
# ARCHIVO 64/69: __init__.py
# Directorio: python_forestacion/servicios/personal
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/servicios/personal/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 65/69: trabajador_service.py
# Directorio: python_forestacion/servicios/personal
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/servicios/personal/trabajador_service.py
# ==============================================================================

from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.personal.trabajador import Trabajador
    from python_forestacion.entidades.personal.herramienta import Herramienta


class TrabajadorService:
    """Servicio para operaciones sobre trabajadores."""
    
    def trabajar(self, trabajador: 'Trabajador', fecha_trabajo: date,
                herramienta: 'Herramienta') -> bool:
        """
        Ejecuta tareas del trabajador.
        
        Args:
            trabajador: Trabajador que ejecuta
            fecha_trabajo: Fecha de trabajo
            herramienta: Herramienta a usar
            
        Returns:
            True si trabajó, False si no tiene apto médico
        """
        if not trabajador.tiene_apto_medico():
            print(f"[!] {trabajador.get_nombre()} NO tiene apto medico - No puede trabajar")
            return False
        
        tareas = trabajador.get_tareas()
        if not tareas:
            print(f"[INFO] {trabajador.get_nombre()} no tiene tareas asignadas")
            return True
        
        # Ordenar por ID descendente
        tareas_ordenadas = sorted(tareas, key=lambda t: t.get_id(), reverse=True)
        
        for tarea in tareas_ordenadas:
            if tarea.get_fecha_programada() <= fecha_trabajo:
                print(f"[TAREA] {trabajador.get_nombre()} ejecuta: {tarea.get_descripcion()} "
                      f"con {herramienta.get_nombre()}")
                tarea.marcar_completada()
        
        return True


################################################################################
# DIRECTORIO: python_forestacion/servicios/terrenos
################################################################################

# ==============================================================================
# ARCHIVO 66/69: __init__.py
# Directorio: python_forestacion/servicios/terrenos
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/servicios/terrenos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 67/69: plantacion_service.py
# Directorio: python_forestacion/servicios/terrenos
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/servicios/terrenos/plantacion_service.py
# ==============================================================================

from typing import List, Type, TYPE_CHECKING
from datetime import date

from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
from python_forestacion.constantes import AGUA_MINIMA

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class PlantacionService:
    """Servicio para operaciones sobre Plantación."""
    
    def __init__(self):
        self._registry = CultivoServiceRegistry.get_instance()
    
    def plantar(self, plantacion: 'Plantacion', especie: str, cantidad: int) -> None:
        """
        Planta cultivos en la plantación usando Factory.
        
        Args:
            plantacion: Plantación destino
            especie: Tipo de cultivo
            cantidad: Cantidad a plantar
            
        Raises:
            SuperficieInsuficienteException: Si no hay espacio
        """
        # Crear un cultivo de ejemplo para calcular superficie
        cultivo_ejemplo = CultivoFactory.crear_cultivo(especie)
        superficie_requerida = cultivo_ejemplo.get_superficie() * cantidad
        superficie_disponible = plantacion.calcular_superficie_disponible()
        
        if superficie_requerida > superficie_disponible:
            raise SuperficieInsuficienteException(
                superficie_requerida,
                superficie_disponible
            )
        
        # Plantar todos los cultivos
        for _ in range(cantidad):
            cultivo = CultivoFactory.crear_cultivo(especie)
            plantacion.add_cultivo(cultivo)
        
        print(f"[OK] Plantados {cantidad} {especie}(s) - Superficie usada: {superficie_requerida:.2f}m2")
    
    def regar(self, plantacion: 'Plantacion', fecha: date = None) -> int:
        """
        Riega todos los cultivos de la plantación.
        
        Args:
            plantacion: Plantación a regar
            fecha: Fecha del riego (default: hoy)
            
        Returns:
            Total de litros consumidos
            
        Raises:
            AguaAgotadaException: Si no hay agua suficiente
        """
        if fecha is None:
            fecha = date.today()
        
        cultivos = plantacion.get_cultivos()
        if not cultivos:
            print("[INFO] No hay cultivos para regar")
            return 0
        
        # Calcular agua total necesaria
        agua_necesaria = 0
        for cultivo in cultivos:
            # Estimación basada en absorción promedio
            agua_necesaria += 3  # Promedio aproximado
        
        agua_disponible = plantacion.get_agua_disponible()
        
        if agua_disponible < agua_necesaria:
            raise AguaAgotadaException(agua_disponible, agua_necesaria)
        
        # Regar cada cultivo
        total_absorbido = 0
        for cultivo in cultivos:
            litros = self._registry.absorber_agua(cultivo)
            total_absorbido += litros
            
            # Hacer crecer si es árbol
            self._registry.crecer(cultivo)
        
        # Descontar agua
        nueva_agua = agua_disponible - total_absorbido
        plantacion.set_agua_disponible(max(nueva_agua, 0))
        
        print(f"[RIEGO] Consumidos {total_absorbido}L - Disponible: {plantacion.get_agua_disponible()}L")
        
        return total_absorbido
    
    def cosechar(self, plantacion: 'Plantacion') -> List['Cultivo']:
        """
        Cosecha todos los cultivos.
        
        Returns:
            Lista de cultivos cosechados
        """
        cultivos = plantacion.get_cultivos()
        print(f"[COSECHA] Cosechados {len(cultivos)} cultivos")
        return cultivos.copy()
    
    def fumigar(self, plantacion: 'Plantacion', plaguicida: str) -> None:
        """Aplica plaguicida a toda la plantación."""
        print(f"[FUMIGACION] Aplicado {plaguicida} a {len(plantacion.get_cultivos())} cultivos")
    
    def mostrar_estado(self, plantacion: 'Plantacion') -> None:
        """Muestra el estado completo de la plantación."""
        print(f"\n--- Plantacion: {plantacion.get_nombre()} ---")
        print(f"Superficie Total: {plantacion.get_superficie_total()}m2")
        print(f"Superficie Disponible: {plantacion.calcular_superficie_disponible():.2f}m2")
        print(f"Agua Disponible: {plantacion.get_agua_disponible()}L")
        print(f"Cultivos: {len(plantacion.get_cultivos())}")
        print(f"Trabajadores: {len(plantacion.get_trabajadores())}")


# ==============================================================================
# ARCHIVO 68/69: registro_forestal_service.py
# Directorio: python_forestacion/servicios/terrenos
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/servicios/terrenos/registro_forestal_service.py
# ==============================================================================

import pickle
import os
from pathlib import Path

from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.excepciones.persistencia_exception import PersistenciaException
from python_forestacion.constantes import DIRECTORIO_DATOS


class RegistroForestalService:
    """Servicio para persistir y recuperar registros forestales."""
    
    def __init__(self, directorio_datos: str = DIRECTORIO_DATOS):
        self._directorio = directorio_datos
        self._asegurar_directorio()
    
    def _asegurar_directorio(self) -> None:
        """Crea el directorio de datos si no existe."""
        Path(self._directorio).mkdir(parents=True, exist_ok=True)
    
    def _obtener_ruta_archivo(self, propietario: str) -> str:
        """Genera la ruta del archivo para un propietario."""
        nombre_archivo = f"{propietario}.dat"
        return os.path.join(self._directorio, nombre_archivo)
    
    def persistir(self, registro: RegistroForestal) -> None:
        """
        Persiste un registro forestal en disco usando Pickle.
        
        Args:
            registro: Registro a guardar
            
        Raises:
            PersistenciaException: Si falla el guardado
        """
        propietario = registro.get_propietario()
        ruta = self._obtener_ruta_archivo(propietario)
        
        try:
            with open(ruta, 'wb') as archivo:
                pickle.dump(registro, archivo)
            print(f"[PERSISTENCIA] Registro guardado: {ruta}")
        except Exception as e:
            raise PersistenciaException(f"guardar registro de {propietario}", e)
    
    @staticmethod
    def leer_registro(propietario: str, directorio: str = DIRECTORIO_DATOS) -> RegistroForestal:
        """
        Lee un registro forestal desde disco.
        
        Args:
            propietario: Nombre del propietario
            directorio: Directorio de datos
            
        Returns:
            Registro forestal recuperado
            
        Raises:
            PersistenciaException: Si falla la lectura
        """
        ruta = os.path.join(directorio, f"{propietario}.dat")
        
        if not os.path.exists(ruta):
            raise PersistenciaException(
                f"leer registro de {propietario}",
                FileNotFoundError(f"No existe: {ruta}")
            )
        
        try:
            with open(ruta, 'rb') as archivo:
                registro = pickle.load(archivo)
            print(f"[PERSISTENCIA] Registro leido: {ruta}")
            return registro
        except Exception as e:
            raise PersistenciaException(f"leer registro de {propietario}", e)
    
    def mostrar_datos(self, registro: RegistroForestal) -> None:
        """Muestra datos completos del registro."""
        print("\n" + "="*70)
        print(f"REGISTRO FORESTAL - Padron: {registro.get_id_padron()}")
        print("="*70)
        
        tierra = registro.get_tierra()
        print(f"\nTIERRA:")
        print(f"  Padron: {tierra.get_id_padron()}")
        print(f"  Superficie: {tierra.get_superficie()}m2")
        print(f"  Domicilio: {tierra.get_domicilio()}")
        
        plantacion = registro.get_plantacion()
        print(f"\nPLANTACION: {plantacion.get_nombre()}")
        print(f"  Cultivos totales: {len(plantacion.get_cultivos())}")
        print(f"  Agua disponible: {plantacion.get_agua_disponible()}L")
        
        print(f"\nPROPIETARIO: {registro.get_propietario()}")
        print(f"AVALUO: ${registro.get_avaluo():,.2f}")
        print("="*70)


# ==============================================================================
# ARCHIVO 69/69: tierra_service.py
# Directorio: python_forestacion/servicios/terrenos
# Ruta completa: /home/fabri/Parcial-forestacion/python_forestacion/servicios/terrenos/tierra_service.py
# ==============================================================================

from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.constantes import AGUA_INICIAL_PLANTACION


class TierraService:
    """Servicio para operaciones sobre Tierra."""
    
    def crear_tierra_con_plantacion(self, id_padron_catastral: int,
                                    superficie: float, domicilio: str,
                                    nombre_plantacion: str) -> Tierra:
        """
        Crea una tierra con su plantación asociada.
        
        Args:
            id_padron_catastral: ID del padrón
            superficie: Superficie en m²
            domicilio: Ubicación
            nombre_plantacion: Nombre de la plantación
            
        Returns:
            Tierra con plantación asociada
        """
        tierra = Tierra(id_padron_catastral, superficie, domicilio)
        
        plantacion = Plantacion(nombre_plantacion, superficie)
        plantacion.set_agua_disponible(AGUA_INICIAL_PLANTACION)
        
        tierra.set_finca(plantacion)
        
        return tierra


################################################################################
# FIN DEL INTEGRADOR FINAL
# Total de archivos: 69
# Generado: 2025-10-22 01:25:44
################################################################################
