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