# python_forestacion/entidades/personal/trabajador.py
"""
Entidad Trabajador - Trabajador agrícola.
"""

from typing import List, Optional
from python_forestacion.entidades.personal.tarea import Tarea
from python_forestacion.entidades.personal.apto_medico import AptoMedico


class Trabajador:
    """Trabajador con tareas y certificación médica."""
    
    def __init__(self, dni: int, nombre: str, tareas: List[Tarea], 
                 apto_medico: Optional[AptoMedico] = None):
        self._dni = dni
        self._nombre = nombre
        self._tareas = tareas
        self._apto_medico = apto_medico
    
    def get_dni(self) -> int:
        return self._dni
    
    def get_nombre(self) -> str:
        return self._nombre
    
    def get_tareas(self) -> List[Tarea]:
        return self._tareas
    
    def add_tarea(self, tarea: Tarea) -> None:
        self._tareas.append(tarea)
    
    def get_apto_medico(self) -> Optional[AptoMedico]:
        return self._apto_medico
    
    def set_apto_medico(self, apto: AptoMedico) -> None:
        self._apto_medico = apto
    
    def tiene_apto_medico(self) -> bool:
        return self._apto_medico is not None