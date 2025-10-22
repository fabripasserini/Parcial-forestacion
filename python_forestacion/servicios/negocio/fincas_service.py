
from typing import List, Type, TYPE_CHECKING
from python_forestacion.servicios.negocio.paquete import Paquete

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class FincasService:
    """Servicio de alto nivel para operaciones en fincas."""
    
    @staticmethod
    def cosechar_por_tipo(plantacion: 'Plantacion', 
                         tipo_cultivo: Type['Cultivo']) -> Paquete['Cultivo']:
        """
        Cosecha selectiva por tipo de cultivo.
        
        Args:
            plantacion: Plantación a cosechar
            tipo_cultivo: Tipo de cultivo a cosechar
            
        Returns:
            Paquete con cultivos del tipo especificado
        """
        paquete = Paquete[tipo_cultivo]()
        
        for cultivo in plantacion.get_cultivos():
            if isinstance(cultivo, tipo_cultivo):
                paquete.agregar(cultivo)
        
        print(f"[COSECHA] Empaquetados {paquete.cantidad()} {tipo_cultivo.__name__}(s)")
        return paquete
    
    @staticmethod
    def mostrar_paquete(paquete: Paquete, nombre_tipo: str) -> None:
        """Muestra el contenido de un paquete."""
        print(f"\n--- Paquete de {nombre_tipo} ---")
        print(f"Cantidad: {paquete.cantidad()}")
        
        from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
        registry = CultivoServiceRegistry.get_instance()
        
        for i, cultivo in enumerate(paquete.get_contenido(), 1):
            print(f"\n{nombre_tipo} #{i}:")
            registry.mostrar_datos(cultivo)
