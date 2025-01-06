from sqlalchemy import Column, String, Text
from .base import ModeloBase

class Entidad(ModeloBase):
    """
    Modelo para representar una entidad (empresa/organización).
    Cada entidad tendrá su propio conjunto de datos presupuestales.
    """
    __tablename__ = 'entidades'

    nombre = Column(String(100), nullable=False)
    nit = Column(String(20), unique=True, index=True, nullable=False)
    direccion = Column(String(200))
    telefono = Column(String(50))
    email = Column(String(100))
    descripcion = Column(Text)
    tipo_entidad = Column(String(50))  # Ejemplo: "Pública", "Privada", etc.
    nivel = Column(String(50))  # Ejemplo: "Municipal", "Departamental", etc.
    
    # Sobrescribimos para que entidad_id no sea requerido en este modelo
    entidad_id = None