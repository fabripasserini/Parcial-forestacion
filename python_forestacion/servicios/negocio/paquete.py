
from typing import TypeVar, Generic, List

T = TypeVar('T')


class Paquete(Generic[T]):
    """Paquete genérico tipo-seguro para empaquetar cultivos."""
    
    def __init__(self):
        self._contenido: List[T] = []
    
    def agregar(self, item: T) -> None:
        """Agrega un item al paquete."""
        self._contenido.append(item)
    
    def get_contenido(self) -> List[T]:
        """Obtiene el contenido del paquete."""
        return self._contenido
    
    def cantidad(self) -> int:
        """Cantidad de items en el paquete."""
        return len(self._contenido)

