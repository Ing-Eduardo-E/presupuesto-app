from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from .core.config import settings
from .infrastructure.database import get_db, create_tables
from .domain.models.test import TestItem

def create_application() -> FastAPI:
    """Función de fábrica para crear la aplicación FastAPI."""
    application = FastAPI(
        title=settings.APP_TITLE,
        description=settings.APP_DESCRIPTION,
        version=settings.APP_VERSION
    )

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return application

app = create_application()

@app.on_event("startup")
async def startup_event():
    """Evento que se ejecuta al iniciar la aplicación"""
    create_tables()  # Crear las tablas en la base de datos

@app.get("/")
async def root():
    """Endpoint raíz"""
    return {
        "mensaje": "¡Bienvenido al Sistema de Presupuestos!",
        "estado": "activo",
        "version": settings.APP_VERSION,
        "ambiente": settings.APP_ENV
    }

@app.get("/health")
async def health_check():
    """Endpoint de verificación de salud"""
    return {
        "status": "healthy",
        "version": settings.APP_VERSION
    }

@app.post("/test-db")
async def test_database(db: Session = Depends(get_db)):
    """
    Endpoint para probar la conexión a la base de datos.
    Crea un item de prueba y lo retorna.
    """
    try:
        # Crear un nuevo item
        test_item = TestItem(name="Test Item")
        db.add(test_item)
        db.commit()
        db.refresh(test_item)
        
        return {
            "message": "Base de datos funcionando correctamente",
            "item_created": {
                "id": test_item.id,
                "name": test_item.name,
                "created_at": test_item.created_at
            }
        }
    except Exception as e:
        return {
            "error": "Error al conectar con la base de datos",
            "details": str(e)
        }