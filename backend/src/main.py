from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .core.config import settings  # Cambiado a import relativo

def create_application() -> FastAPI:
    """
    Función de fábrica para crear la aplicación FastAPI.
    Permite una mejor gestión de la configuración y middleware.
    """
    application = FastAPI(
        title=settings.APP_TITLE,
        description=settings.APP_DESCRIPTION,
        version=settings.APP_VERSION
    )

    # Configuración de CORS
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Configurar apropiadamente en producción
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return application

app = create_application()

@app.get("/")
async def root():
    """
    Endpoint raíz para verificar el estado de la API.
    Returns:
        dict: Información básica sobre la API
    """
    return {
        "mensaje": "¡Bienvenido al Sistema de Presupuestos!",
        "estado": "activo",
        "version": settings.APP_VERSION,
        "ambiente": settings.APP_ENV
    }

@app.get("/health")
async def health_check():
    """
    Endpoint para verificar la salud del servicio.
    Útil para monitoreo y kubernetes liveness probes.
    """
    return {
        "status": "healthy",
        "version": settings.APP_VERSION
    }