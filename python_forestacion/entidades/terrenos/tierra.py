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
