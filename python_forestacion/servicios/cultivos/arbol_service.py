from typing import TYPE_CHECKING
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.arbol import Arbol


class ArbolService(CultivoService):
    """Servicio base para árboles."""
    
    def mostrar_datos(self, cultivo: 'Arbol') -> None:
        """Muestra datos del árbol incluyendo altura."""
        super().mostrar_datos(cultivo)
        print(f"  Altura: {cultivo.get_altura():.2f}m")
