"""
Archivo integrador generado automaticamente
Directorio: /home/fabri/Parcial-forestacion/python_forestacion/servicios/personal
Fecha: 2025-10-22 01:25:44
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/servicios/personal/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: trabajador_service.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/servicios/personal/trabajador_service.py
# ================================================================================

from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.personal.trabajador import Trabajador
    from python_forestacion.entidades.personal.herramienta import Herramienta


class TrabajadorService:
    """Servicio para operaciones sobre trabajadores."""
    
    def trabajar(self, trabajador: 'Trabajador', fecha_trabajo: date,
                herramienta: 'Herramienta') -> bool:
        """
        Ejecuta tareas del trabajador.
        
        Args:
            trabajador: Trabajador que ejecuta
            fecha_trabajo: Fecha de trabajo
            herramienta: Herramienta a usar
            
        Returns:
            True si trabajó, False si no tiene apto médico
        """
        if not trabajador.tiene_apto_medico():
            print(f"[!] {trabajador.get_nombre()} NO tiene apto medico - No puede trabajar")
            return False
        
        tareas = trabajador.get_tareas()
        if not tareas:
            print(f"[INFO] {trabajador.get_nombre()} no tiene tareas asignadas")
            return True
        
        # Ordenar por ID descendente
        tareas_ordenadas = sorted(tareas, key=lambda t: t.get_id(), reverse=True)
        
        for tarea in tareas_ordenadas:
            if tarea.get_fecha_programada() <= fecha_trabajo:
                print(f"[TAREA] {trabajador.get_nombre()} ejecuta: {tarea.get_descripcion()} "
                      f"con {herramienta.get_nombre()}")
                tarea.marcar_completada()
        
        return True

