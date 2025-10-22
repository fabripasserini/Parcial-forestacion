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
