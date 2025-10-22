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
