"""
Archivo integrador generado automaticamente
Directorio: /home/fabri/Parcial-forestacion/python_forestacion/patrones/strategy/impl
Fecha: 2025-10-22 01:25:44
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/patrones/strategy/impl/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: absorcion_constante_strategy.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/patrones/strategy/impl/absorcion_constante_strategy.py
# ================================================================================

from datetime import date
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy


class AbsorcionConstanteStrategy(AbsorcionAguaStrategy):
    """Absorción constante independiente de la estación."""
    
    def __init__(self, cantidad_constante: int):
        self._cantidad = cantidad_constante
    
    def calcular_absorcion(self, fecha: date, temperatura: float,
                          humedad: float, cultivo) -> int:
        return self._cantidad

# ================================================================================
# ARCHIVO 3/3: absorcion_seasonal_strategy.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/patrones/strategy/impl/absorcion_seasonal_strategy.py
# ================================================================================

from datetime import date
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
from python_forestacion.constantes import (
    MES_INICIO_VERANO,
    MES_FIN_VERANO,
    ABSORCION_SEASONAL_VERANO,
    ABSORCION_SEASONAL_INVIERNO
)


class AbsorcionSeasonalStrategy(AbsorcionAguaStrategy):
    """Absorción diferenciada por estación del año."""
    
    def calcular_absorcion(self, fecha: date, temperatura: float, 
                          humedad: float, cultivo) -> int:
        mes = fecha.month
        
        # Verano: Diciembre, Enero, Febrero (hemisferio sur)
        if mes >= MES_INICIO_VERANO or mes <= MES_FIN_VERANO:
            return ABSORCION_SEASONAL_VERANO
        else:
            return ABSORCION_SEASONAL_INVIERNO

