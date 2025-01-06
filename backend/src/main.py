from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from .core.config import settings
from .infrastructure.database import get_db, create_tables
from .domain.models.entidad import Entidad
from .domain.models.presupuesto import Rubro, CDP, RegistroPresupuestal, TipoRubro, EstadoPresupuestal
from .domain.schemas.entidad_schema import EntidadCreate

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
    create_tables()

@app.get("/")
async def root():
    return {
        "mensaje": "¡Bienvenido al Sistema de Presupuestos!",
        "estado": "activo",
        "version": settings.APP_VERSION,
        "ambiente": settings.APP_ENV
    }

@app.post("/test/entidad")
async def test_entidad(entidad: EntidadCreate, db: Session = Depends(get_db)):
    try:
        nueva_entidad = Entidad(
            nombre=entidad.nombre,
            nit=entidad.nit,
            direccion=entidad.direccion,
            telefono=entidad.telefono,
            email=entidad.email,
            tipo_entidad=entidad.tipo_entidad,
            nivel=entidad.nivel,
            descripcion=entidad.descripcion
        )
        db.add(nueva_entidad)
        db.commit()
        db.refresh(nueva_entidad)
        
        return {
            "mensaje": "Entidad creada correctamente",
            "entidad": {
                "id": nueva_entidad.id,
                "nombre": nueva_entidad.nombre,
                "nit": nueva_entidad.nit,
                "fecha_creacion": nueva_entidad.fecha_creacion
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/test/rubro/{entidad_id}")
async def test_rubro(entidad_id: int, db: Session = Depends(get_db)):
    """Prueba de creación de rubro"""
    try:
        rubro = Rubro(
            entidad_id=entidad_id,
            codigo="1.1.1",
            nombre="Rubro de Prueba",
            descripcion="Rubro para pruebas",
            tipo=TipoRubro.INGRESO,
            presupuesto_inicial=1000000.00
        )
        db.add(rubro)
        db.commit()
        db.refresh(rubro)
        
        return {
            "mensaje": "Rubro creado correctamente",
            "rubro": {
                "id": rubro.id,
                "codigo": rubro.codigo,
                "nombre": rubro.nombre,
                "tipo": rubro.tipo.value,
                "presupuesto": float(rubro.presupuesto_inicial)
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/test/cdp/{entidad_id}/{rubro_id}")
async def test_cdp(entidad_id: int, rubro_id: int, db: Session = Depends(get_db)):
    """Prueba de creación de CDP"""
    try:
        cdp = CDP(
            entidad_id=entidad_id,
            rubro_id=rubro_id,
            numero="CDP-2025-001",
            fecha="2025-01-05",
            concepto="CDP de prueba",
            valor=500000.00,
            estado=EstadoPresupuestal.APROBADO
        )
        db.add(cdp)
        db.commit()
        db.refresh(cdp)
        
        return {
            "mensaje": "CDP creado correctamente",
            "cdp": {
                "id": cdp.id,
                "numero": cdp.numero,
                "valor": float(cdp.valor),
                "estado": cdp.estado.value
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))