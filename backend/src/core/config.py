from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    """
    Configuraciones de la aplicación utilizando Pydantic Settings.
    Permite la validación de configuraciones y carga desde variables de entorno.
    """
    APP_TITLE: str = "Sistema de Presupuestos"
    APP_DESCRIPTION: str = "API para gestión de presupuestos en entidades descentralizadas"
    APP_VERSION: str = "1.0.0"
    APP_ENV: str = "development"
    
    # Configuración de base de datos
    DATABASE_URL: str = "sqlite:///./presupuesto.db"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

@lru_cache()
def get_settings() -> Settings:
    """
    Obtiene una instancia de configuración cacheada.
    Utiliza lru_cache para evitar lecturas múltiples del archivo .env
    """
    return Settings()

# Instancia global de configuraciones
settings = get_settings()