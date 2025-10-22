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