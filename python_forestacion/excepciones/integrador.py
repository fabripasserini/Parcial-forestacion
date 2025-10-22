"""
Archivo integrador generado automaticamente
Directorio: /home/fabri/Parcial-forestacion/python_forestacion/excepciones
Fecha: 2025-10-22 01:25:44
Total de archivos integrados: 6
"""

# ================================================================================
# ARCHIVO 1/6: __init__.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/excepciones/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/6: agua_agotada_exception.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/excepciones/agua_agotada_exception.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/6: forestacion_exception.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/excepciones/forestacion_exception.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 4/6: mensajes_exception.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/excepciones/mensajes_exception.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 5/6: persistencia_exception.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/excepciones/persistencia_exception.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 6/6: superficie_insuficiente_exception.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/excepciones/superficie_insuficiente_exception.py
# ================================================================================

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



