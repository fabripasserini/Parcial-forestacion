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