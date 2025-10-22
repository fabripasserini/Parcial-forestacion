from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones.mensajes_exception import MensajesException


class SuperficieInsuficienteException(ForestacionException):
    """Excepción lanzada cuando la superficie disponible es insuficiente."""
    
    def __init__(self, superficie_requerida: float, superficie_disponible: float):
        self._superficie_requerida = superficie_requerida
        self._superficie_disponible = superficie_disponible
        
        super().__init__(
            MensajesException.SUPERFICIE_INSUFICIENTE_USUARIO,
            f"{MensajesException.SUPERFICIE_INSUFICIENTE_TECNICO}: "
            f"requerida={superficie_requerida}m², disponible={superficie_disponible}m²"
        )
    
    def get_superficie_requerida(self) -> float:
        return self._superficie_requerida
    
    def get_superficie_disponible(self) -> float:
        return self._superficie_disponible

