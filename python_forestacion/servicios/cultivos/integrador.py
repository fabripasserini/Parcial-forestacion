"""
Archivo integrador generado automaticamente
Directorio: /home/fabri/Parcial-forestacion/python_forestacion/servicios/cultivos
Fecha: 2025-10-22 01:25:44
Total de archivos integrados: 8
"""

# ================================================================================
# ARCHIVO 1/8: __init__.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/servicios/cultivos/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/8: arbol_service.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/servicios/cultivos/arbol_service.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/8: cultivo_service.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/servicios/cultivos/cultivo_service.py
# ================================================================================

from datetime import date
from typing import TYPE_CHECKING
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class CultivoService:
    """Servicio base para operaciones sobre cultivos."""
    
    def __init__(self, estrategia_absorcion: AbsorcionAguaStrategy):
        self._estrategia_absorcion = estrategia_absorcion
    
    def absorver_agua(self, cultivo: 'Cultivo', fecha: date = None,
                     temperatura: float = 20.0, humedad: float = 50.0) -> int:
        """
        Calcula agua absorbida usando la estrategia inyectada.
        
        Returns:
            Litros absorbidos
        """
        if fecha is None:
            fecha = date.today()
        
        litros = self._estrategia_absorcion.calcular_absorcion(
            fecha, temperatura, humedad, cultivo
        )
        
        agua_actual = cultivo.get_agua()
        cultivo.set_agua(agua_actual + litros)
        
        return litros
    
    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        """Muestra datos básicos del cultivo."""
        print(f"  Agua: {cultivo.get_agua()}L")
        print(f"  Superficie: {cultivo.get_superficie()}m2")


# ================================================================================
# ARCHIVO 4/8: cultivo_service_registry.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/servicios/cultivos/cultivo_service_registry.py
# ================================================================================

from threading import Lock
from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos.pino_service import PinoService
from python_forestacion.servicios.cultivos.olivo_service import OlivoService
from python_forestacion.servicios.cultivos.lechuga_service import LechugaService
from python_forestacion.servicios.cultivos.zanahoria_service import ZanahoriaService

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo
    from python_forestacion.entidades.cultivos.pino import Pino
    from python_forestacion.entidades.cultivos.olivo import Olivo
    from python_forestacion.entidades.cultivos.lechuga import Lechuga
    from python_forestacion.entidades.cultivos.zanahoria import Zanahoria


class CultivoServiceRegistry:
    """
    Registry de servicios de cultivos implementando Singleton.
    Thread-safe con double-checked locking.
    """
    
    _instance = None
    _lock = Lock()
    
    def __new__(cls):
        """Implementación thread-safe de Singleton."""
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        """Inicializa servicios y registros solo una vez."""
        if not hasattr(self, '_initialized'):
            # Servicios
            self._pino_service = PinoService()
            self._olivo_service = OlivoService()
            self._lechuga_service = LechugaService()
            self._zanahoria_service = ZanahoriaService()
            
            # Registry de handlers
            self._absorber_agua_handlers = {}
            self._mostrar_datos_handlers = {}
            self._crecer_handlers = {}
            
            self._registrar_handlers()
            self._initialized = True
    
    def _registrar_handlers(self):
        """Registra handlers por tipo de cultivo."""
        from python_forestacion.entidades.cultivos.pino import Pino
        from python_forestacion.entidades.cultivos.olivo import Olivo
        from python_forestacion.entidades.cultivos.lechuga import Lechuga
        from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
        
        # Absorber agua
        self._absorber_agua_handlers[Pino] = self._absorber_agua_pino
        self._absorber_agua_handlers[Olivo] = self._absorber_agua_olivo
        self._absorber_agua_handlers[Lechuga] = self._absorber_agua_lechuga
        self._absorber_agua_handlers[Zanahoria] = self._absorber_agua_zanahoria
        
        # Mostrar datos
        self._mostrar_datos_handlers[Pino] = self._mostrar_datos_pino
        self._mostrar_datos_handlers[Olivo] = self._mostrar_datos_olivo
        self._mostrar_datos_handlers[Lechuga] = self._mostrar_datos_lechuga
        self._mostrar_datos_handlers[Zanahoria] = self._mostrar_datos_zanahoria
        
        # Crecer (solo árboles)
        self._crecer_handlers[Pino] = self._crecer_pino
        self._crecer_handlers[Olivo] = self._crecer_olivo
    
    # Handlers específicos
    def _absorber_agua_pino(self, cultivo):
        return self._pino_service.absorver_agua(cultivo)
    
    def _absorber_agua_olivo(self, cultivo):
        return self._olivo_service.absorver_agua(cultivo)
    
    def _absorber_agua_lechuga(self, cultivo):
        return self._lechuga_service.absorver_agua(cultivo)
    
    def _absorber_agua_zanahoria(self, cultivo):
        return self._zanahoria_service.absorver_agua(cultivo)
    
    def _mostrar_datos_pino(self, cultivo):
        self._pino_service.mostrar_datos(cultivo)
    
    def _mostrar_datos_olivo(self, cultivo):
        self._olivo_service.mostrar_datos(cultivo)
    
    def _mostrar_datos_lechuga(self, cultivo):
        self._lechuga_service.mostrar_datos(cultivo)
    
    def _mostrar_datos_zanahoria(self, cultivo):
        self._zanahoria_service.mostrar_datos(cultivo)
    
    def _crecer_pino(self, cultivo):
        self._pino_service.crecer(cultivo)
    
    def _crecer_olivo(self, cultivo):
        self._olivo_service.crecer(cultivo)
    
    # API Pública con dispatch polimórfico
    def absorber_agua(self, cultivo: 'Cultivo') -> int:
        """Dispatch polimórfico para absorber agua."""
        tipo = type(cultivo)
        if tipo not in self._absorber_agua_handlers:
            raise ValueError(f"Tipo de cultivo desconocido: {tipo.__name__}")
        return self._absorber_agua_handlers[tipo](cultivo)
    
    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        """Dispatch polimórfico para mostrar datos."""
        tipo = type(cultivo)
        if tipo not in self._mostrar_datos_handlers:
            raise ValueError(f"Tipo de cultivo desconocido: {tipo.__name__}")
        self._mostrar_datos_handlers[tipo](cultivo)
    
    def crecer(self, cultivo: 'Cultivo') -> None:
        """Dispatch polimórfico para crecimiento (solo árboles)."""
        tipo = type(cultivo)
        if tipo in self._crecer_handlers:
            self._crecer_handlers[tipo](cultivo)
    
    @classmethod
    def get_instance(cls):
        """Obtiene la instancia única del registry."""
        return cls()

# ================================================================================
# ARCHIVO 5/8: lechuga_service.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/servicios/cultivos/lechuga_service.py
# ================================================================================

from typing import TYPE_CHECKING
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from python_forestacion.constantes import ABSORCION_CONSTANTE_LECHUGA

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.lechuga import Lechuga


class LechugaService(CultivoService):
    """Servicio para operaciones sobre Lechuga."""
    
    def __init__(self):
        super().__init__(AbsorcionConstanteStrategy(ABSORCION_CONSTANTE_LECHUGA))
    
    def mostrar_datos(self, cultivo: 'Lechuga') -> None:
        """Muestra datos específicos de la lechuga."""
        super().mostrar_datos(cultivo)
        print(f"  Variedad: {cultivo.get_variedad()}")
        print(f"  Invernadero: {'Si' if cultivo.tiene_invernadero() else 'No'}")


# ================================================================================
# ARCHIVO 6/8: olivo_service.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/servicios/cultivos/olivo_service.py
# ================================================================================

from typing import TYPE_CHECKING
from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from python_forestacion.constantes import CRECIMIENTO_OLIVO_POR_RIEGO

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.olivo import Olivo


class OlivoService(ArbolService):
    """Servicio para operaciones sobre Olivo."""
    
    def __init__(self):
        super().__init__(AbsorcionSeasonalStrategy())
    
    def crecer(self, olivo: 'Olivo') -> None:
        """Hace crecer el olivo según constante."""
        altura_actual = olivo.get_altura()
        olivo.set_altura(altura_actual + CRECIMIENTO_OLIVO_POR_RIEGO)
    
    def mostrar_datos(self, cultivo: 'Olivo') -> None:
        """Muestra datos específicos del olivo."""
        super().mostrar_datos(cultivo)
        print(f"  Tipo Aceituna: {cultivo.get_tipo_aceituna().value}")


# ================================================================================
# ARCHIVO 7/8: pino_service.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/servicios/cultivos/pino_service.py
# ================================================================================


from typing import TYPE_CHECKING
from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from python_forestacion.constantes import CRECIMIENTO_PINO_POR_RIEGO

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.pino import Pino


class PinoService(ArbolService):
    """Servicio para operaciones sobre Pino."""
    
    def __init__(self):
        super().__init__(AbsorcionSeasonalStrategy())
    
    def crecer(self, pino: 'Pino') -> None:
        """Hace crecer el pino según constante."""
        altura_actual = pino.get_altura()
        pino.set_altura(altura_actual + CRECIMIENTO_PINO_POR_RIEGO)
    
    def mostrar_datos(self, cultivo: 'Pino') -> None:
        """Muestra datos específicos del pino."""
        super().mostrar_datos(cultivo)
        print(f"  Variedad: {cultivo.get_variedad()}")



# ================================================================================
# ARCHIVO 8/8: zanahoria_service.py
# Ruta: /home/fabri/Parcial-forestacion/python_forestacion/servicios/cultivos/zanahoria_service.py
# ================================================================================

from typing import TYPE_CHECKING
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from python_forestacion.constantes import ABSORCION_CONSTANTE_ZANAHORIA

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.zanahoria import Zanahoria


class ZanahoriaService(CultivoService):
    """Servicio para operaciones sobre Zanahoria."""
    
    def __init__(self):
        super().__init__(AbsorcionConstanteStrategy(ABSORCION_CONSTANTE_ZANAHORIA))
    
    def mostrar_datos(self, cultivo: 'Zanahoria') -> None:
        """Muestra datos específicos de la zanahoria."""
        super().mostrar_datos(cultivo)
        print(f"  Baby Carrot: {'Si' if cultivo.es_baby() else 'No'}")



