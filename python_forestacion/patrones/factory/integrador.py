"""
Archivo integrador generado automaticamente
Directorio: /home/fabri/Parcial-forestacion/python_forestacion/patrones/factory
Fecha: 2025-10-22 01:25:44
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/patrones/factory/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: cultivo_factory.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/patrones/factory/cultivo_factory.py
# ================================================================================

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class CultivoFactory:
    """Factory para crear instancias de cultivos."""
    
    @staticmethod
    def crear_cultivo(especie: str) -> 'Cultivo':
        """
        Crea un cultivo según la especie.
        
        Args:
            especie: Tipo de cultivo ("Pino", "Olivo", "Lechuga", "Zanahoria")
            
        Returns:
            Instancia del cultivo solicitado
            
        Raises:
            ValueError: Si la especie es desconocida
        """
        factories = {
            "Pino": CultivoFactory._crear_pino,
            "Olivo": CultivoFactory._crear_olivo,
            "Lechuga": CultivoFactory._crear_lechuga,
            "Zanahoria": CultivoFactory._crear_zanahoria
        }
        
        if especie not in factories:
            raise ValueError(f"Especie desconocida: {especie}")
        
        return factories[especie]()
    
    @staticmethod
    def _crear_pino() -> 'Cultivo':
        from python_forestacion.entidades.cultivos.pino import Pino
        return Pino(variedad="Paraná")
    
    @staticmethod
    def _crear_olivo() -> 'Cultivo':
        from python_forestacion.entidades.cultivos.olivo import Olivo
        from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna
        return Olivo(tipo_aceituna=TipoAceituna.ARBEQUINA)
    
    @staticmethod
    def _crear_lechuga() -> 'Cultivo':
        from python_forestacion.entidades.cultivos.lechuga import Lechuga
        return Lechuga(variedad="Crespa")
    
    @staticmethod
    def _crear_zanahoria() -> 'Cultivo':
        from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
        return Zanahoria(es_baby=False)

