from typing import Optional
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    """
    Configuraciones de la aplicación.
    
    Attributes:
        APP_TITLE: Nombre de la aplicación
        APP_DESCRIPTION: Descripción de la aplicación
        APP_VERSION: Versión actual de la aplicación
        APP_ENV: Entorno de ejecución (development, production, testing)
        DATABASE_URL: URL de conexión a la base de datos
        ASYNC_DATABASE_URL: URL para conexiones asíncronas
        DATABASE_ECHO: Habilitar logging de SQL
    """
    # Configuración de la aplicación
    APP_TITLE: str = "Sistema de Presupuestos"
    APP_DESCRIPTION: str = "API para gestión de presupuestos en entidades descentralizadas"
    APP_VERSION: str = "1.0.0"
    APP_ENV: str = "development"
    
    # Configuración de la base de datos
    DATABASE_URL: str = "sqlite:///./presupuesto.db"
    ASYNC_DATABASE_URL: Optional[str] = None
    DATABASE_ECHO: bool = False
    
    # Configuración de seguridad (para implementar más adelante)
    SECRET_KEY: str = "development_secret_key"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    class Config:
        env_file = ".env"
        case_sensitive = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.ASYNC_DATABASE_URL is None:
            # Convertir DATABASE_URL a versión asíncrona si es necesario
            self.ASYNC_DATABASE_URL = (
                self.DATABASE_URL.replace("sqlite:///", "sqlite+aiosqlite:///")
                if "sqlite" in self.DATABASE_URL
                else self.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")
            )

@lru_cache()
def get_settings() -> Settings:
    """
    Obtiene una instancia cacheada de las configuraciones.
    
    Returns:
        Settings: Instancia única de configuraciones
    """
    return Settings()

# Instancia global de configuraciones
settings = get_settings()