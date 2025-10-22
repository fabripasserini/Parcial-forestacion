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