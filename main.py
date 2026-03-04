from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Modelo de datos
class Reserva(BaseModel):
    id_reserva: int
    id_sala: int
    id_usuario: int
    fecha: str
    hora_inicio: str
    hora_fin: str
    personas: int
    estado: str

# Lista en memoria
reservas: List[Reserva] = []

# Endpoint POST
@app.post("/reservas")
def crear_reserva(reserva: Reserva):
    reservas.append(reserva)
    return {
        "mensaje": "Reserva registrada correctamente",
        "reserva": reserva
    }