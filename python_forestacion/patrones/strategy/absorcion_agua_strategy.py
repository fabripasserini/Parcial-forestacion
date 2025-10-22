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
