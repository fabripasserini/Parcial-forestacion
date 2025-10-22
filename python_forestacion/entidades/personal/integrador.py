"""
Archivo integrador generado automaticamente
Directorio: /home/fabri/Parcial-forestacion/python_forestacion/entidades/personal
Fecha: 2025-10-22 01:25:44
Total de archivos integrados: 5
"""

# ================================================================================
# ARCHIVO 1/5: __init__.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/entidades/personal/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/5: apto_medico.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/entidades/personal/apto_medico.py
# ================================================================================

# python_forestacion/entidades/personal/apto_medico.py
"""
Entidad AptoMedico - Certificación médica.
"""

from datetime import date


class AptoMedico:
    """Certificación médica de un trabajador."""
    
    def __init__(self, fecha_emision: date, observaciones: str = ""):
        self._fecha_emision = fecha_emision
        self._observaciones = observaciones
    
    def get_fecha_emision(self) -> date:
        return self._fecha_emision
    
    def get_observaciones(self) -> str:
        return self._observaciones

# ================================================================================
# ARCHIVO 3/5: herramienta.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/entidades/personal/herramienta.py
# ================================================================================

# python_forestacion/entidades/personal/herramienta.py
"""
Entidad Herramienta - Herramienta de trabajo.
"""


class Herramienta:
    """Herramienta con certificación H&S."""
    
    def __init__(self, id_herramienta: int, nombre: str, certificacion_hs: bool):
        self._id = id_herramienta
        self._nombre = nombre
        self._certificacion_hs = certificacion_hs
    
    def get_id(self) -> int:
        return self._id
    
    def get_nombre(self) -> str:
        return self._nombre
    
    def tiene_certificacion_hs(self) -> bool:
        return self._certificacion_hs

# ================================================================================
# ARCHIVO 4/5: tarea.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/entidades/personal/tarea.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 5/5: trabajador.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/entidades/personal/trabajador.py
# ================================================================================

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

