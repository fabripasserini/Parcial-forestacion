class MensajesException:
    """
    Contenedor centralizado de mensajes de error del sistema de forestación.

    Distingue entre mensajes orientados al usuario final (amigables)
    y mensajes técnicos para registro o depuración.
    """

    # ==========================================================
    # 🌱 Superficie
    # ==========================================================
    SUPERFICIE_INSUFICIENTE_USUARIO = (
        "No hay suficiente superficie disponible para completar la plantación."
    )
    SUPERFICIE_INSUFICIENTE_TECNICO = (
        "La superficie requerida excede la disponible en el sistema."
    )

    # ==========================================================
    # 💧 Agua
    # ==========================================================
    AGUA_AGOTADA_USUARIO = (
        "El agua disponible en la plantación se ha agotado. "
        "Revise el sistema de riego o las reservas."
    )
    AGUA_AGOTADA_TECNICO = (
        "Cantidad de agua insuficiente para completar la operación de riego."
    )

    # ==========================================================
    # 💾 Persistencia
    # ==========================================================
    PERSISTENCIA_ERROR_USUARIO = (
        "Se produjo un error al guardar o recuperar los datos. "
        "Por favor, intente nuevamente."
    )
    PERSISTENCIA_ERROR_TECNICO = (
        "Error en la operación de persistencia (por ejemplo, con Pickle o acceso a disco)."
    )

    # ==========================================================
    # ⚙️ Genéricos / Futuros
    # ==========================================================
    ERROR_DESCONOCIDO_USUARIO = "Ocurrió un error inesperado en el sistema."
    ERROR_DESCONOCIDO_TECNICO = "Excepción no manejada detectada en la capa de aplicación."
