# python_forestacion/entidades/personal/tarea.py
"""
Entidad Tarea - Tarea asignada a trabajador.
"""

from datetime import date
from enum import Enum


class EstadoTarea(Enum):
    """Estados posibles de una tarea."""
    PENDIENTE = "Pendiente"
    COMPLETADA = "Completada"


class Tarea:
    """Tarea asignada a un trabajador."""
    
    def __init__(self, id_tarea: int, descripcion: str, fecha_programada: date):
        self._id = id_tarea
        self._descripcion = descripcion
        self._fecha_programada = fecha_programada
        self._estado = EstadoTarea.PENDIENTE
    
    def get_id(self) -> int:
        return self._id
    
    def get_descripcion(self) -> str:
        return self._descripcion
    
    def get_fecha_programada(self) -> date:
        return self._fecha_programada
    
    def get_estado(self) -> EstadoTarea:
        return self._estado
    
    def marcar_completada(self) -> None:
        self._estado = EstadoTarea.COMPLETADA
