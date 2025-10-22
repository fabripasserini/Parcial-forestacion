class ForestacionException(Exception):
    """
    Excepción base del sistema forestal.
    
    Proporciona soporte para mensajes separados (usuario y técnico)
    y permite el encadenamiento opcional de causas.
    """

    def __init__(
        self,
        mensaje_usuario: str,
        mensaje_tecnico: str,
        causa: Exception | None = None
    ) -> None:
        self._mensaje_usuario = mensaje_usuario
        self._mensaje_tecnico = mensaje_tecnico
        self._causa = causa
        super().__init__(mensaje_tecnico)

    @property
    def mensaje_usuario(self) -> str:
        """Mensaje amigable destinado a mostrar al usuario final."""
        return self._mensaje_usuario

    @property
    def mensaje_tecnico(self) -> str:
        """Mensaje detallado para logs o diagnóstico técnico."""
        return self._mensaje_tecnico

    @property
    def causa(self) -> Exception | None:
        """Causa original que produjo la excepción, si existe."""
        return self._causa

    def __str__(self) -> str:
        """Devuelve el mensaje técnico (útil para logging estándar)."""
        return self._mensaje_tecnico

    def __repr__(self) -> str:
        """Representación detallada para debugging."""
        return (
            f"{self.__class__.__name__}("
            f"usuario='{self._mensaje_usuario}', "
            f"tecnico='{self._mensaje_tecnico}', "
            f"causa={repr(self._causa)})"
        )

    def get_full_message(self) -> str:
        """Construye un mensaje combinado y legible."""
        partes = [
            f"Usuario: {self._mensaje_usuario}",
            f"Técnico: {self._mensaje_tecnico}"
        ]
        if self._causa:
            partes.append(f"Causa: {self._causa}")
        return "\n".join(partes)
