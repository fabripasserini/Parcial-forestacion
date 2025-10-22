import time
from datetime import date, timedelta

from python_forestacion.servicios.terrenos.tierra_service import TierraService
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.servicios.terrenos.registro_forestal_service import RegistroForestalService
from python_forestacion.servicios.personal.trabajador_service import TrabajadorService
from python_forestacion.servicios.negocio.fincas_service import FincasService
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry

from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.entidades.personal.trabajador import Trabajador
from python_forestacion.entidades.personal.tarea import Tarea
from python_forestacion.entidades.personal.apto_medico import AptoMedico
from python_forestacion.entidades.personal.herramienta import Herramienta
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.olivo import Olivo

from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask
from python_forestacion.riego.control.control_riego_task import ControlRiegoTask

from python_forestacion.excepciones.forestacion_exception import ForestacionException



def imprimir_separador(titulo: str = "", ancho: int = 70):
    if titulo:
        print(f"\n{'-'*ancho}\n  {titulo}\n{'-'*ancho}")
    else:
        print("="*ancho)


def inicializar_servicios():
    imprimir_separador("PATRON SINGLETON: Inicializando servicios")
    registry1 = CultivoServiceRegistry.get_instance()
    registry2 = CultivoServiceRegistry.get_instance()
    if registry1 is registry2:
        print("[OK] Todos los servicios comparten la misma instancia del Registry")

    return (
        TierraService(),
        PlantacionService(),
        TrabajadorService(),
        RegistroForestalService(),
        FincasService()
    )


def crear_infraestructura(tierra_service, plantacion_service):
    imprimir_separador("Creando infraestructura")
    terreno = tierra_service.crear_tierra_con_plantacion(
        id_padron_catastral=123456,
        superficie=10000.0,
        domicilio="Ruta 40 Km 1080, Agrelo, Mendoza",
        nombre_plantacion="Finca del Madero"
    )
    plantacion = terreno.get_finca()
    print(f"[OK] Tierra creada: Padron {terreno.get_id_padron()}")
    print(f"[OK] Plantacion '{plantacion.get_nombre()}' con {plantacion.get_superficie_total()}m2")
    return terreno, plantacion


def plantar_cultivos(plantacion_service, plantacion):
    imprimir_separador("PATRON FACTORY METHOD: Plantando cultivos")
    try:
        plantacion_service.plantar(plantacion, "Pino", 40)
        plantacion_service.plantar(plantacion, "Olivo", 30)
        plantacion_service.plantar(plantacion, "Lechuga", 100)
        plantacion_service.plantar(plantacion, "Zanahoria", 150)
        plantacion_service.mostrar_estado(plantacion)
    except ForestacionException as e:
        print(f"[ERROR] {e.get_full_message()}")


def gestionar_personal(plantacion, trabajador_service):
    imprimir_separador("Gestion de Personal")

    apto_pepe = AptoMedico(date.today() - timedelta(days=30), "Apto para trabajos agricolas")
    tarea1 = Tarea(1, "Mantenimiento de pinos", date.today())
    tarea2 = Tarea(2, "Riego manual de hortalizas", date.today())

    trabajador1 = Trabajador(12345678, "Pepe Fernandez", [tarea1, tarea2], apto_pepe)
    trabajador2 = Trabajador(87654321, "Maria Gomez", [], None)

    plantacion.add_trabajador(trabajador1)
    plantacion.add_trabajador(trabajador2)

    herramienta = Herramienta(1, "Pala de jardineria", True)

    print(f"[OK] Trabajador: {trabajador1.get_nombre()} - Apto medico: SI")
    print(f"[OK] Trabajador: {trabajador2.get_nombre()} - Apto medico: NO")

    # Ejecutar tareas
    print("\n[INFO] Ejecutando tareas...")
    trabajador_service.trabajar(trabajador1, date.today(), herramienta)
    trabajador_service.trabajar(trabajador2, date.today(), herramienta)


def riego_automatizado(plantacion, plantacion_service, duracion: int = 15):
    imprimir_separador("PATRON OBSERVER: Sistema de riego automatizado")
    print("[INFO] Iniciando sensores y controlador de riego...")

    sensor_temp = TemperaturaReaderTask()
    sensor_hum = HumedadReaderTask()

    controlador = ControlRiegoTask(sensor_temp, sensor_hum, plantacion, plantacion_service)

    sensor_temp.start()
    sensor_hum.start()
    controlador.start()

    print(f"[INFO] Sistema funcionando durante {duracion} segundos...")
    time.sleep(duracion)

    print("\n[INFO] Deteniendo sistema de riego...")
    sensor_temp.detener()
    sensor_hum.detener()
    controlador.detener()

    sensor_temp.join(timeout=2)
    sensor_hum.join(timeout=2)
    controlador.join(timeout=2)


def cosecha_y_fumigacion(fincas_service, plantacion_service, plantacion):
    imprimir_separador("Cosecha y Fumigacion")

    paquete_pinos = fincas_service.cosechar_por_tipo(plantacion, Pino)
    paquete_olivos = fincas_service.cosechar_por_tipo(plantacion, Olivo)
    fincas_service.mostrar_paquete(paquete_pinos, "Pino")
    fincas_service.mostrar_paquete(paquete_olivos, "Olivo")

    print("\n[INFO] Fumigando plantacion...")
    plantacion_service.fumigar(plantacion, "Fungicida Organico XYZ")


def persistencia(registro_service, terreno, plantacion):
    imprimir_separador("Persistencia con Pickle")

    registro = RegistroForestal(
        id_padron=terreno.get_id_padron(),
        tierra=terreno,
        plantacion=plantacion,
        propietario="Pepe Fernandez",
        avaluo=50309233.55
    )

    print("\n[INFO] Persistiendo registro en disco...")
    try:
        registro_service.persistir(registro)
        print("[OK] Registro guardado exitosamente")
    except ForestacionException as e:
        print(f"[ERROR] {e.get_full_message()}")

    print("\n[INFO] Recuperando registro desde disco...")
    try:
        registro_leido = RegistroForestalService.leer_registro("Pepe Fernandez")
        registro_service.mostrar_datos(registro_leido)
        print("[OK] Registro recuperado exitosamente")
    except ForestacionException as e:
        print(f"[ERROR] {e.get_full_message()}")


def main():
    imprimir_separador("SISTEMA DE GESTION FORESTAL - DEMO PATRONES DE DISEÑO", 70)

    tierra_service, plantacion_service, trabajador_service, registro_service, fincas_service = inicializar_servicios()

    terreno, plantacion = crear_infraestructura(tierra_service, plantacion_service)

    plantar_cultivos(plantacion_service, plantacion)

    gestionar_personal(plantacion, trabajador_service)

    riego_automatizado(plantacion, plantacion_service, duracion=15)

    cosecha_y_fumigacion(fincas_service, plantacion_service, plantacion)

    persistencia(registro_service, terreno, plantacion)

    imprimir_separador()
    print("              DEMO COMPLETADA EXITOSAMENTE")
    imprimir_separador()
    print("[INFO] Revise el archivo de datos persistidos")
    print("[INFO] Sistema finalizado correctamente\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Programa interrumpido por el usuario")