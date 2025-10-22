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
