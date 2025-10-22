from typing import TYPE_CHECKING
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from python_forestacion.constantes import ABSORCION_CONSTANTE_LECHUGA

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.lechuga import Lechuga


class LechugaService(CultivoService):
    """Servicio para operaciones sobre Lechuga."""
    
    def __init__(self):
        super().__init__(AbsorcionConstanteStrategy(ABSORCION_CONSTANTE_LECHUGA))
    
    def mostrar_datos(self, cultivo: 'Lechuga') -> None:
        """Muestra datos específicos de la lechuga."""
        super().mostrar_datos(cultivo)
        print(f"  Variedad: {cultivo.get_variedad()}")
        print(f"  Invernadero: {'Si' if cultivo.tiene_invernadero() else 'No'}")
