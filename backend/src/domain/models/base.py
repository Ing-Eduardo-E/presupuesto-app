from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.orm import declared_attr
from ...infrastructure.database import Base

class ModeloBase(Base):
    """
    Modelo base que contiene campos comunes para todas las entidades y
    soporte para multitenancy.
    """
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    fecha_actualizacion = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    estado = Column(String, default='activo')
    
    # Campo para multitenancy
    @declared_attr
    def entidad_id(cls):
        return Column(Integer, nullable=False, index=True)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()