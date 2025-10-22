

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