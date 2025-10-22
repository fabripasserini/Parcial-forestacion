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