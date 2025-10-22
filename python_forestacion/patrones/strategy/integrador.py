"""
Archivo integrador generado automaticamente
Directorio: /home/fabri/Parcial-forestacion/python_forestacion/patrones/strategy
Fecha: 2025-10-22 01:25:44
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/patrones/strategy/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: absorcion_agua_strategy.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/patrones/strategy/absorcion_agua_strategy.py
# ================================================================================

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


