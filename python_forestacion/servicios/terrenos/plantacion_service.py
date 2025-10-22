from typing import List, Type, TYPE_CHECKING
from datetime import date

from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
from python_forestacion.constantes import AGUA_MINIMA

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class PlantacionService:
    """Servicio para operaciones sobre Plantación."""
    
    def __init__(self):
        self._registry = CultivoServiceRegistry.get_instance()
    
    def plantar(self, plantacion: 'Plantacion', especie: str, cantidad: int) -> None:
        """
        Planta cultivos en la plantación usando Factory.
        
        Args:
            plantacion: Plantación destino
            especie: Tipo de cultivo
            cantidad: Cantidad a plantar
            
        Raises:
            SuperficieInsuficienteException: Si no hay espacio
        """
        # Crear un cultivo de ejemplo para calcular superficie
        cultivo_ejemplo = CultivoFactory.crear_cultivo(especie)
        superficie_requerida = cultivo_ejemplo.get_superficie() * cantidad
        superficie_disponible = plantacion.calcular_superficie_disponible()
        
        if superficie_requerida > superficie_disponible:
            raise SuperficieInsuficienteException(
                superficie_requerida,
                superficie_disponible
            )
        
        # Plantar todos los cultivos
        for _ in range(cantidad):
            cultivo = CultivoFactory.crear_cultivo(especie)
            plantacion.add_cultivo(cultivo)
        
        print(f"[OK] Plantados {cantidad} {especie}(s) - Superficie usada: {superficie_requerida:.2f}m2")
    
    def regar(self, plantacion: 'Plantacion', fecha: date = None) -> int:
        """
        Riega todos los cultivos de la plantación.
        
        Args:
            plantacion: Plantación a regar
            fecha: Fecha del riego (default: hoy)
            
        Returns:
            Total de litros consumidos
            
        Raises:
            AguaAgotadaException: Si no hay agua suficiente
        """
        if fecha is None:
            fecha = date.today()
        
        cultivos = plantacion.get_cultivos()
        if not cultivos:
            print("[INFO] No hay cultivos para regar")
            return 0
        
        # Calcular agua total necesaria
        agua_necesaria = 0
        for cultivo in cultivos:
            # Estimación basada en absorción promedio
            agua_necesaria += 3  # Promedio aproximado
        
        agua_disponible = plantacion.get_agua_disponible()
        
        if agua_disponible < agua_necesaria:
            raise AguaAgotadaException(agua_disponible, agua_necesaria)
        
        # Regar cada cultivo
        total_absorbido = 0
        for cultivo in cultivos:
            litros = self._registry.absorber_agua(cultivo)
            total_absorbido += litros
            
            # Hacer crecer si es árbol
            self._registry.crecer(cultivo)
        
        # Descontar agua
        nueva_agua = agua_disponible - total_absorbido
        plantacion.set_agua_disponible(max(nueva_agua, 0))
        
        print(f"[RIEGO] Consumidos {total_absorbido}L - Disponible: {plantacion.get_agua_disponible()}L")
        
        return total_absorbido
    
    def cosechar(self, plantacion: 'Plantacion') -> List['Cultivo']:
        """
        Cosecha todos los cultivos.
        
        Returns:
            Lista de cultivos cosechados
        """
        cultivos = plantacion.get_cultivos()
        print(f"[COSECHA] Cosechados {len(cultivos)} cultivos")
        return cultivos.copy()
    
    def fumigar(self, plantacion: 'Plantacion', plaguicida: str) -> None:
        """Aplica plaguicida a toda la plantación."""
        print(f"[FUMIGACION] Aplicado {plaguicida} a {len(plantacion.get_cultivos())} cultivos")
    
    def mostrar_estado(self, plantacion: 'Plantacion') -> None:
        """Muestra el estado completo de la plantación."""
        print(f"\n--- Plantacion: {plantacion.get_nombre()} ---")
        print(f"Superficie Total: {plantacion.get_superficie_total()}m2")
        print(f"Superficie Disponible: {plantacion.calcular_superficie_disponible():.2f}m2")
        print(f"Agua Disponible: {plantacion.get_agua_disponible()}L")
        print(f"Cultivos: {len(plantacion.get_cultivos())}")
        print(f"Trabajadores: {len(plantacion.get_trabajadores())}")
