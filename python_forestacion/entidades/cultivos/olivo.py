
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