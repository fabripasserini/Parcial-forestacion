from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones.mensajes_exception import MensajesException


class AguaAgotadaException(ForestacionException):
    """
    Excepción lanzada cuando el agua disponible es insuficiente
    para cumplir con un requerimiento de riego.
    """

    def __init__(self, agua_disponible: int, agua_requerida: int) -> None:
        self._agua_disponible = agua_disponible
        self._agua_requerida = agua_requerida

        mensaje_usuario = MensajesException.AGUA_AGOTADA_USUARIO
        mensaje_tecnico = (
            f"{MensajesException.AGUA_AGOTADA_TECNICO}: "
            f"disponible={agua_disponible}L, requerida={agua_requerida}L"
        )

        super().__init__(mensaje_usuario, mensaje_tecnico)

    @property
    def agua_disponible(self) -> int:
        """Cantidad actual de agua disponible (en litros)."""
        return self._agua_disponible

    @property
    def agua_requerida(self) -> int:
        """Cantidad de agua requerida (en litros)."""
        return self._agua_requerida

    def __str__(self) -> str:
        """Representación legible de la excepción."""
        return (
            f"AguaAgotadaException("
            f"disponible={self._agua_disponible}L, "
            f"requerida={self._agua_requerida}L)"
        )
