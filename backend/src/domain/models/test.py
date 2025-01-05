from sqlalchemy import Column, Integer, String
from datetime import datetime
from sqlalchemy import DateTime
from ...infrastructure.database import Base

class TestItem(Base):
    """Modelo de prueba para verificar la configuración de la base de datos"""
    __tablename__ = "test_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)