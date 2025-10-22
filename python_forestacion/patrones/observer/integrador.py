"""
Archivo integrador generado automaticamente
Directorio: /home/fabri/Parcial-forestacion/python_forestacion/patrones/observer
Fecha: 2025-10-22 01:25:44
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/patrones/observer/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: observable.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/patrones/observer/observable.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/3: observer.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/patrones/observer/observer.py
# ================================================================================

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


