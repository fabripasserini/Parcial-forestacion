from datetime import date
from typing import TYPE_CHECKING
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class CultivoService:
    """Servicio base para operaciones sobre cultivos."""
    
    def __init__(self, estrategia_absorcion: AbsorcionAguaStrategy):
        self._estrategia_absorcion = estrategia_absorcion
    
    def absorver_agua(self, cultivo: 'Cultivo', fecha: date = None,
                     temperatura: float = 20.0, humedad: float = 50.0) -> int:
        """
        Calcula agua absorbida usando la estrategia inyectada.
        
        Returns:
            Litros absorbidos
        """
        if fecha is None:
            fecha = date.today()
        
        litros = self._estrategia_absorcion.calcular_absorcion(
            fecha, temperatura, humedad, cultivo
        )
        
        agua_actual = cultivo.get_agua()
        cultivo.set_agua(agua_actual + litros)
        
        return litros
    
    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        """Muestra datos básicos del cultivo."""
        print(f"  Agua: {cultivo.get_agua()}L")
        print(f"  Superficie: {cultivo.get_superficie()}m2")
