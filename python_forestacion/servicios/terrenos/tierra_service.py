from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.constantes import AGUA_INICIAL_PLANTACION


class TierraService:
    """Servicio para operaciones sobre Tierra."""
    
    def crear_tierra_con_plantacion(self, id_padron_catastral: int,
                                    superficie: float, domicilio: str,
                                    nombre_plantacion: str) -> Tierra:
        """
        Crea una tierra con su plantación asociada.
        
        Args:
            id_padron_catastral: ID del padrón
            superficie: Superficie en m²
            domicilio: Ubicación
            nombre_plantacion: Nombre de la plantación
            
        Returns:
            Tierra con plantación asociada
        """
        tierra = Tierra(id_padron_catastral, superficie, domicilio)
        
        plantacion = Plantacion(nombre_plantacion, superficie)
        plantacion.set_agua_disponible(AGUA_INICIAL_PLANTACION)
        
        tierra.set_finca(plantacion)
        
        return tierra