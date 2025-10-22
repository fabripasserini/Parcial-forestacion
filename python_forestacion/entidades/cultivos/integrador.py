"""
Archivo integrador generado automaticamente
Directorio: /home/fabri/Parcial-forestacion/python_forestacion/entidades/cultivos
Fecha: 2025-10-22 01:25:44
Total de archivos integrados: 9
"""

# ================================================================================
# ARCHIVO 1/9: __init__.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/entidades/cultivos/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/9: arbol.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/entidades/cultivos/arbol.py
# ================================================================================



from python_forestacion.entidades.cultivos.cultivo import Cultivo


class Arbol(Cultivo):
    """Cultivo de tipo árbol con altura."""
    
    def __init__(self, agua: int, superficie: float, altura: float):
        super().__init__(agua, superficie)
        self._altura = altura
    
    def get_altura(self) -> float:
        return self._altura
    
    def set_altura(self, altura: float) -> None:
        self._altura = altura

# ================================================================================
# ARCHIVO 3/9: cultivo.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/entidades/cultivos/cultivo.py
# ================================================================================



from abc import ABC


class Cultivo(ABC):
    """Clase base para todos los cultivos."""
    
    def __init__(self, agua: int, superficie: float):
        self._agua = agua
        self._superficie = superficie
    
    def get_agua(self) -> int:
        return self._agua
    
    def set_agua(self, agua: int) -> None:
        self._agua = agua
    
    def get_superficie(self) -> float:
        return self._superficie
    
    def set_superficie(self, superficie: float) -> None:
        self._superficie = superficie

# ================================================================================
# ARCHIVO 4/9: hortaliza.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/entidades/cultivos/hortaliza.py
# ================================================================================



from python_forestacion.entidades.cultivos.cultivo import Cultivo


class Hortaliza(Cultivo):
    """Cultivo de tipo hortaliza."""
    
    def __init__(self, agua: int, superficie: float, invernadero: bool):
        super().__init__(agua, superficie)
        self._invernadero = invernadero
    
    def tiene_invernadero(self) -> bool:
        return self._invernadero
    
    def set_invernadero(self, invernadero: bool) -> None:
        self._invernadero = invernadero

# ================================================================================
# ARCHIVO 5/9: lechuga.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/entidades/cultivos/lechuga.py
# ================================================================================


from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import (
    AGUA_INICIAL_LECHUGA,
    SUPERFICIE_LECHUGA
)


class Lechuga(Hortaliza):
    """Hortaliza tipo Lechuga."""
    
    def __init__(self, variedad: str):
        super().__init__(
            agua=AGUA_INICIAL_LECHUGA,
            superficie=SUPERFICIE_LECHUGA,
            invernadero=True
        )
        self._variedad = variedad
    
    def get_variedad(self) -> str:
        return self._variedad
    
    def set_variedad(self, variedad: str) -> None:
        self._variedad = variedad

# ================================================================================
# ARCHIVO 6/9: olivo.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/entidades/cultivos/olivo.py
# ================================================================================


from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna
from python_forestacion.constantes import (
    AGUA_INICIAL_OLIVO,
    SUPERFICIE_OLIVO,
    ALTURA_INICIAL_OLIVO
)


class Olivo(Arbol):
    """Árbol tipo Olivo."""
    
    def __init__(self, tipo_aceituna: TipoAceituna):
        super().__init__(
            agua=AGUA_INICIAL_OLIVO,
            superficie=SUPERFICIE_OLIVO,
            altura=ALTURA_INICIAL_OLIVO
        )
        self._tipo_aceituna = tipo_aceituna
    
    def get_tipo_aceituna(self) -> TipoAceituna:
        return self._tipo_aceituna
    
    def set_tipo_aceituna(self, tipo: TipoAceituna) -> None:
        self._tipo_aceituna = tipo

# ================================================================================
# ARCHIVO 7/9: pino.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/entidades/cultivos/pino.py
# ================================================================================


from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.constantes import (
    AGUA_INICIAL_PINO,
    SUPERFICIE_PINO,
    ALTURA_INICIAL_PINO
)


class Pino(Arbol):
    """Árbol tipo Pino."""
    
    def __init__(self, variedad: str):
        super().__init__(
            agua=AGUA_INICIAL_PINO,
            superficie=SUPERFICIE_PINO,
            altura=ALTURA_INICIAL_PINO
        )
        self._variedad = variedad
    
    def get_variedad(self) -> str:
        return self._variedad
    
    def set_variedad(self, variedad: str) -> None:
        self._variedad = variedad

# ================================================================================
# ARCHIVO 8/9: tipo_aceituna.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/entidades/cultivos/tipo_aceituna.py
# ================================================================================



from enum import Enum


class TipoAceituna(Enum):
    """Tipos de aceitunas para olivos."""
    ARBEQUINA = "Arbequina"
    PICUAL = "Picual"
    MANZANILLA = "Manzanilla"

# ================================================================================
# ARCHIVO 9/9: zanahoria.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/entidades/cultivos/zanahoria.py
# ================================================================================


from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import (
    AGUA_INICIAL_ZANAHORIA,
    SUPERFICIE_ZANAHORIA
)


class Zanahoria(Hortaliza):
    """Hortaliza tipo Zanahoria."""
    
    def __init__(self, es_baby: bool):
        super().__init__(
            agua=AGUA_INICIAL_ZANAHORIA,
            superficie=SUPERFICIE_ZANAHORIA,
            invernadero=False
        )
        self._es_baby = es_baby
    
    def es_baby(self) -> bool:
        return self._es_baby
    
    def set_es_baby(self, es_baby: bool) -> None:
        self._es_baby = es_baby

