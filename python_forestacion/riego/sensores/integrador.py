"""
Archivo integrador generado automaticamente
Directorio: /home/fabri/Parcial-forestacion/python_forestacion/riego/sensores
Fecha: 2025-10-22 01:25:44
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/riego/sensores/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: humedad_reader_task.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/riego/sensores/humedad_reader_task.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/3: temperatura_reader_task.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/riego/sensores/temperatura_reader_task.py
# ================================================================================

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


