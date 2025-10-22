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
