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
