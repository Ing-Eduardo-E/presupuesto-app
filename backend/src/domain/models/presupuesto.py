from sqlalchemy import Column, String, Numeric, ForeignKey, Integer, Text, Enum as SQLEnum
from sqlalchemy.orm import relationship, backref
import enum
from .base import ModeloBase

class TipoRubro(enum.Enum):
    """Tipos de rubros presupuestales"""
    INGRESO = "ingreso"
    GASTO = "gasto"

class EstadoPresupuestal(enum.Enum):
    """Estados para documentos presupuestales"""
    BORRADOR = "borrador"
    APROBADO = "aprobado"
    ANULADO = "anulado"
    EJECUTADO = "ejecutado"

class Rubro(ModeloBase):
    """Modelo para los rubros presupuestales"""
    codigo = Column(String(20), nullable=False, index=True)
    nombre = Column(String(200), nullable=False)
    descripcion = Column(Text)
    tipo = Column(SQLEnum(TipoRubro), nullable=False)
    presupuesto_inicial = Column(Numeric(precision=18, scale=2), default=0)
    presupuesto_definitivo = Column(Numeric(precision=18, scale=2), default=0)
    
    # Relaciones
    rubro_padre_id = Column(Integer, ForeignKey('rubro.id'), nullable=True)
    rubros_hijos = relationship(
        "Rubro",
        backref=backref("rubro_padre", remote_side="[Rubro.id]"),
        cascade="all, delete-orphan"
    )
    
    __table_args__ = (
        # Código único por entidad
        # UniqueConstraint('codigo', 'entidad_id', name='uix_1'),
    )

class CDP(ModeloBase):
    """Certificado de Disponibilidad Presupuestal"""
    numero = Column(String(20), nullable=False, index=True)
    fecha = Column(String(10), nullable=False)  # YYYY-MM-DD
    concepto = Column(Text, nullable=False)
    valor = Column(Numeric(precision=18, scale=2), nullable=False)
    estado = Column(SQLEnum(EstadoPresupuestal), default=EstadoPresupuestal.BORRADOR)
    
    # Relaciones
    rubro_id = Column(Integer, ForeignKey('rubro.id'), nullable=False)
    rubro = relationship("Rubro", backref="cdps")
    
    __table_args__ = (
        # Número único por entidad
        # UniqueConstraint('numero', 'entidad_id', name='uix_1'),
    )

class RegistroPresupuestal(ModeloBase):
    """Registro Presupuestal (RP)"""
    numero = Column(String(20), nullable=False, index=True)
    fecha = Column(String(10), nullable=False)  # YYYY-MM-DD
    concepto = Column(Text, nullable=False)
    valor = Column(Numeric(precision=18, scale=2), nullable=False)
    estado = Column(SQLEnum(EstadoPresupuestal), default=EstadoPresupuestal.BORRADOR)
    
    # Relaciones
    cdp_id = Column(Integer, ForeignKey('cdp.id'), nullable=False)
    cdp = relationship("CDP", backref="registros")
    
    __table_args__ = (
        # Número único por entidad
        # UniqueConstraint('numero', 'entidad_id', name='uix_1'),
    )