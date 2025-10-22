from typing import TYPE_CHECKING
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from python_forestacion.constantes import ABSORCION_CONSTANTE_ZANAHORIA

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.zanahoria import Zanahoria


class ZanahoriaService(CultivoService):
    """Servicio para operaciones sobre Zanahoria."""
    
    def __init__(self):
        super().__init__(AbsorcionConstanteStrategy(ABSORCION_CONSTANTE_ZANAHORIA))
    
    def mostrar_datos(self, cultivo: 'Zanahoria') -> None:
        """Muestra datos específicos de la zanahoria."""
        super().mostrar_datos(cultivo)
        print(f"  Baby Carrot: {'Si' if cultivo.es_baby() else 'No'}")

