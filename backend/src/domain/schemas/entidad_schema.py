from pydantic import BaseModel, EmailStr

class EntidadCreate(BaseModel):
    nombre: str
    nit: str
    direccion: str | None = None
    telefono: str | None = None
    email: str | None = None
    tipo_entidad: str
    nivel: str
    descripcion: str | None = None