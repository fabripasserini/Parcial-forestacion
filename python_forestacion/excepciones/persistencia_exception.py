from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones.mensajes_exception import MensajesException


class PersistenciaException(ForestacionException):
    """
    Excepción lanzada cuando ocurre un error en la capa de persistencia de datos.
    
    Aporta contexto adicional sobre la operación que falló (por ejemplo: 'guardar', 'leer', 'actualizar').
    """

    def __init__(self, operacion: str, causa: Exception | None = None) -> None:
        self._operacion = operacion

        mensaje_usuario = MensajesException.PERSISTENCIA_ERROR_USUARIO
        mensaje_tecnico = (
            f"{MensajesException.PERSISTENCIA_ERROR_TECNICO} "
            f"during operation '{operacion}'"
        )

        super().__init__(mensaje_usuario, mensaje_tecnico, causa)

    @property
    def operacion(self) -> str:
        """Operación de persistencia que produjo el error (ej. 'insertar', 'actualizar', 'eliminar')."""
        return self._operacion

    def __str__(self) -> str:
        """Devuelve una descripción técnica legible del error."""
        return f"PersistenciaException(operacion='{self._operacion}') → {self.mensaje_tecnico}"
