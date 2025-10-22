"""
Archivo integrador generado automaticamente
Directorio: /home/fabri/Parcial-forestacion/python_forestacion/servicios/terrenos
Fecha: 2025-10-22 01:25:44
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/servicios/terrenos/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: plantacion_service.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/servicios/terrenos/plantacion_service.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/4: registro_forestal_service.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/servicios/terrenos/registro_forestal_service.py
# ================================================================================

import pickle
import os
from pathlib import Path

from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.excepciones.persistencia_exception import PersistenciaException
from python_forestacion.constantes import DIRECTORIO_DATOS


class RegistroForestalService:
    """Servicio para persistir y recuperar registros forestales."""
    
    def __init__(self, directorio_datos: str = DIRECTORIO_DATOS):
        self._directorio = directorio_datos
        self._asegurar_directorio()
    
    def _asegurar_directorio(self) -> None:
        """Crea el directorio de datos si no existe."""
        Path(self._directorio).mkdir(parents=True, exist_ok=True)
    
    def _obtener_ruta_archivo(self, propietario: str) -> str:
        """Genera la ruta del archivo para un propietario."""
        nombre_archivo = f"{propietario}.dat"
        return os.path.join(self._directorio, nombre_archivo)
    
    def persistir(self, registro: RegistroForestal) -> None:
        """
        Persiste un registro forestal en disco usando Pickle.
        
        Args:
            registro: Registro a guardar
            
        Raises:
            PersistenciaException: Si falla el guardado
        """
        propietario = registro.get_propietario()
        ruta = self._obtener_ruta_archivo(propietario)
        
        try:
            with open(ruta, 'wb') as archivo:
                pickle.dump(registro, archivo)
            print(f"[PERSISTENCIA] Registro guardado: {ruta}")
        except Exception as e:
            raise PersistenciaException(f"guardar registro de {propietario}", e)
    
    @staticmethod
    def leer_registro(propietario: str, directorio: str = DIRECTORIO_DATOS) -> RegistroForestal:
        """
        Lee un registro forestal desde disco.
        
        Args:
            propietario: Nombre del propietario
            directorio: Directorio de datos
            
        Returns:
            Registro forestal recuperado
            
        Raises:
            PersistenciaException: Si falla la lectura
        """
        ruta = os.path.join(directorio, f"{propietario}.dat")
        
        if not os.path.exists(ruta):
            raise PersistenciaException(
                f"leer registro de {propietario}",
                FileNotFoundError(f"No existe: {ruta}")
            )
        
        try:
            with open(ruta, 'rb') as archivo:
                registro = pickle.load(archivo)
            print(f"[PERSISTENCIA] Registro leido: {ruta}")
            return registro
        except Exception as e:
            raise PersistenciaException(f"leer registro de {propietario}", e)
    
    def mostrar_datos(self, registro: RegistroForestal) -> None:
        """Muestra datos completos del registro."""
        print("\n" + "="*70)
        print(f"REGISTRO FORESTAL - Padron: {registro.get_id_padron()}")
        print("="*70)
        
        tierra = registro.get_tierra()
        print(f"\nTIERRA:")
        print(f"  Padron: {tierra.get_id_padron()}")
        print(f"  Superficie: {tierra.get_superficie()}m2")
        print(f"  Domicilio: {tierra.get_domicilio()}")
        
        plantacion = registro.get_plantacion()
        print(f"\nPLANTACION: {plantacion.get_nombre()}")
        print(f"  Cultivos totales: {len(plantacion.get_cultivos())}")
        print(f"  Agua disponible: {plantacion.get_agua_disponible()}L")
        
        print(f"\nPROPIETARIO: {registro.get_propietario()}")
        print(f"AVALUO: ${registro.get_avaluo():,.2f}")
        print("="*70)


# ================================================================================
# ARCHIVO 4/4: tierra_service.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/servicios/terrenos/tierra_service.py
# ================================================================================

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

