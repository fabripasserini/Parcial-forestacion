from typing import TYPE_CHECKING
from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from python_forestacion.constantes import CRECIMIENTO_OLIVO_POR_RIEGO

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.olivo import Olivo


class OlivoService(ArbolService):
    """Servicio para operaciones sobre Olivo."""
    
    def __init__(self):
        super().__init__(AbsorcionSeasonalStrategy())
    
    def crecer(self, olivo: 'Olivo') -> None:
        """Hace crecer el olivo según constante."""
        altura_actual = olivo.get_altura()
        olivo.set_altura(altura_actual + CRECIMIENTO_OLIVO_POR_RIEGO)
    
    def mostrar_datos(self, cultivo: 'Olivo') -> None:
        """Muestra datos específicos del olivo."""
        super().mostrar_datos(cultivo)
        print(f"  Tipo Aceituna: {cultivo.get_tipo_aceituna().value}")
