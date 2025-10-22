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
