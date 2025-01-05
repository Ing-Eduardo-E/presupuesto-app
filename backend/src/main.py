from fastapi import FastAPI

app = FastAPI(
    title="Sistema de Presupuestos",
    description="API para gestión de presupuestos en entidades descentralizadas",
    version="1.0.0"
)

@app.get("/")
async def root():
    """
    Endpoint de prueba para verificar que la API está funcionando.
    """
    return {
        "mensaje": "¡Bienvenido al Sistema de Presupuestos!",
        "estado": "activo",
        "version": "1.0.0"
    }

@app.get("/prueba")
async def prueba():
    """
    Endpoint adicional de prueba.
    """
    return {
        "mensaje": "Endpoint de prueba funcionando correctamente"
    }