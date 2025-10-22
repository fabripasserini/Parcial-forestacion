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