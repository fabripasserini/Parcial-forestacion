from datetime import date
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy


class AbsorcionConstanteStrategy(AbsorcionAguaStrategy):
    """Absorción constante independiente de la estación."""
    
    def __init__(self, cantidad_constante: int):
        self._cantidad = cantidad_constante
    
    def calcular_absorcion(self, fecha: date, temperatura: float,
                          humedad: float, cultivo) -> int:
        return self._cantidad