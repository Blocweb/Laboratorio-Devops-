# Laboratorio Devops

Sistema de Gestión de Reservas de Salas – FastAPI

Descripción del proyecto

Este proyecto es un microservicio desarrollado con FastAPI y Pydantic que permite registrar y consultar reservas de salas utilizadas en actividades académicas.

- Cada reserva almacena la siguiente información:
- Sala que será utilizada (id_sala)
- Usuario que realiza la reserva (id_usuario)
- Fecha de la reserva (fecha)
- Hora de inicio y hora de fin (hora_inicio, hora_fin)
- Número de personas que asistirán (personas)
- Estado de la reserva (estado)

El servicio permite:

Registrar nuevas reservas mediante POST /reservas
Consultar todas las reservas mediante GET /reservas

Las reservas se almacenan temporalmente en memoria, sin utilizar una base de datos real. Los datos se reciben y devuelven en formato JSON.

Instalación:

Clonar el repositorio:

git clone <https://github.com/Blocweb/Laboratorio-Devops-.git>
cd Laboratorio-Devops-

Crear un entorno virtual (opcional pero recomendado):

python -m venv venv
# Linux / macOS
source venv/bin/activate
# Windows
venv\Scripts\activate

Instalar dependencias:

pip install fastapi uvicorn pydantic

pip install -r requirements.txt

Ejecución

Ejecutar el microservicio con Uvicorn:

uvicorn main:app --reload

Por defecto, el servicio estará disponible en:

http://127.0.0.1:8000

Para acceder a la documentación interactiva (Swagger UI):

http://127.0.0.1:8000/docs
Endpoints disponibles
1. GET /reservas

Obtiene todas las reservas registradas en memoria.

Ejemplo de respuesta:

[
  {
    "id_reserva": 1,
    "id_sala": 101,
    "id_usuario": 2001,
    "fecha": "2026-03-05",
    "hora_inicio": "08:00",
    "hora_fin": "10:00",
    "personas": 25,
    "estado": "confirmada"
  }
]
2. POST /reservas

Registra una nueva reserva.

Ejemplo de request:

{
  "id_sala": 102,
  "id_usuario": 2002,
  "fecha": "2026-03-06",
  "hora_inicio": "10:00",
  "hora_fin": "12:00",
  "personas": 15,
  "estado": "pendiente"
}

Ejemplo de respuesta:

{
  "id_reserva": 2,
  "id_sala": 102,
  "id_usuario": 2002,
  "fecha": "2026-03-06",
  "hora_inicio": "10:00",
  "hora_fin": "12:00",
  "personas": 15,
  "estado": "pendiente"
}

Si los datos enviados no cumplen con la validación de Pydantic, FastAPI devolverá un error 422 indicando qué campos tienen problemas.

Datos de prueba adjuntados en reservas_prueba.json

