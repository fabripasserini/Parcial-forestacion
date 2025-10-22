"""
Archivo integrador generado automaticamente
Directorio: /home/fabri/Parcial-forestacion/python_forestacion/entidades/terrenos
Fecha: 2025-10-22 01:25:44
Total de archivos integrados: 5
"""

# ================================================================================
# ARCHIVO 1/5: __init__.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/entidades/terrenos/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/5: plantacion.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/entidades/terrenos/plantacion.py
# ================================================================================

# python_forestacion/entidades/terrenos/plantacion.py
"""
Entidad Plantacion - Conjunto de cultivos.
"""

from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo
    from python_forestacion.entidades.personal.trabajador import Trabajador


class Plantacion:
    """Representa una plantación agrícola."""
    
    def __init__(self, nombre: str, superficie: float):
        self._nombre = nombre
        self._superficie_total = superficie
        self._cultivos: List['Cultivo'] = []
        self._trabajadores: List['Trabajador'] = []
        self._agua_disponible = 0
    
    def get_nombre(self) -> str:
        return self._nombre
    
    def get_superficie_total(self) -> float:
        return self._superficie_total
    
    def get_cultivos(self) -> List['Cultivo']:
        return self._cultivos
    
    def add_cultivo(self, cultivo: 'Cultivo') -> None:
        self._cultivos.append(cultivo)
    
    def get_trabajadores(self) -> List['Trabajador']:
        return self._trabajadores
    
    def add_trabajador(self, trabajador: 'Trabajador') -> None:
        if trabajador not in self._trabajadores:
            self._trabajadores.append(trabajador)
    
    def get_agua_disponible(self) -> int:
        return self._agua_disponible
    
    def set_agua_disponible(self, agua: int) -> None:
        self._agua_disponible = agua
    
    def calcular_superficie_disponible(self) -> float:
        """Calcula superficie no ocupada por cultivos."""
        superficie_ocupada = sum(c.get_superficie() for c in self._cultivos)
        return self._superficie_total - superficie_ocupada

# ================================================================================
# ARCHIVO 3/5: registro_florestal.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/entidades/terrenos/registro_florestal.py
# ================================================================================



# ================================================================================
# ARCHIVO 4/5: registro_forestal.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/entidades/terrenos/registro_forestal.py
# ================================================================================

# python_forestacion/entidades/terrenos/registro_forestal.py
"""
Entidad RegistroForestal - Registro completo persistible.
"""

from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion


class RegistroForestal:
    """Registro forestal completo con tierra y plantación."""
    
    def __init__(self, id_padron: int, tierra: Tierra, 
                 plantacion: Plantacion, propietario: str, avaluo: float):
        self._id_padron = id_padron
        self._tierra = tierra
        self._plantacion = plantacion
        self._propietario = propietario
        self._avaluo = avaluo
    
    def get_id_padron(self) -> int:
        return self._id_padron
    
    def get_tierra(self) -> Tierra:
        return self._tierra
    
    def get_plantacion(self) -> Plantacion:
        return self._plantacion
    
    def get_propietario(self) -> str:
        return self._propietario
    
    def get_avaluo(self) -> float:
        return self._avaluo

# ================================================================================
# ARCHIVO 5/5: tierra.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/entidades/terrenos/tierra.py
# ================================================================================

# python_forestacion/entidades/terrenos/tierra.py
"""
Entidad Tierra - Terreno catastral.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion


class Tierra:
    """Representa un terreno con padrón catastral."""
    
    def __init__(self, id_padron_catastral: int, superficie: float, domicilio: str):
        self._id_padron = id_padron_catastral
        self._superficie = superficie
        self._domicilio = domicilio
        self._finca: 'Plantacion' = None
    
    def get_id_padron(self) -> int:
        return self._id_padron
    
    def get_superficie(self) -> float:
        return self._superficie
    
    def get_domicilio(self) -> str:
        return self._domicilio
    
    def get_finca(self) -> 'Plantacion':
        return self._finca
    
    def set_finca(self, finca: 'Plantacion') -> None:
        self._finca = finca


