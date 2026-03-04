
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.post("/api/empleados")
def crear_empleado(nombre: str, area: str):
    return {"mensaje": f"Empleado {nombre} registrado en {area}"}