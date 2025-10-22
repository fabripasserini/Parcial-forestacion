
from typing import TYPE_CHECKING
from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from python_forestacion.constantes import CRECIMIENTO_PINO_POR_RIEGO

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.pino import Pino


class PinoService(ArbolService):
    """Servicio para operaciones sobre Pino."""
    
    def __init__(self):
        super().__init__(AbsorcionSeasonalStrategy())
    
    def crecer(self, pino: 'Pino') -> None:
        """Hace crecer el pino según constante."""
        altura_actual = pino.get_altura()
        pino.set_altura(altura_actual + CRECIMIENTO_PINO_POR_RIEGO)
    
    def mostrar_datos(self, cultivo: 'Pino') -> None:
        """Muestra datos específicos del pino."""
        super().mostrar_datos(cultivo)
        print(f"  Variedad: {cultivo.get_variedad()}")

