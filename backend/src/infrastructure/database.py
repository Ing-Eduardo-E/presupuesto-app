from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.pool import StaticPool
from ..core.config import settings

class Base(DeclarativeBase):
    """Clase base para modelos SQLAlchemy."""
    pass

# Crear el motor de base de datos
engine = create_engine(
    settings.DATABASE_URL,
    # Estas configuraciones son específicas para SQLite y desarrollo
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
    echo=settings.APP_ENV == "development"  # SQL logging en desarrollo
)

# Crear fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency para FastAPI
async def get_db():
    """
    Dependencia que provee una sesión de base de datos.
    
    Yields:
        Session: Sesión de SQLAlchemy
    
    Example:
        @app.get("/items")
        async def read_items(db: Session = Depends(get_db)):
            items = db.query(Item).all()
            return items
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Función para crear todas las tablas
def create_tables() -> None:
    """
    Crea todas las tablas en la base de datos.
    Debe ser llamada después de definir todos los modelos.
    """
    Base.metadata.create_all(bind=engine)