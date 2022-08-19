from fastapi import FastAPI
from pydantic import BaseModel
from kaiTemp import summarize_laser_egg

class StatusJson(BaseModel):
    status: bool
    id: str

app=FastAPI()

def estadoActual(status: bool):
    newStatus = ""
    if status:
        newStatus = "ON"
    else:
        newStatus = "OFF"
    return newStatus

@app.get('/')
def read_root():
    id = summarize_laser_egg("dd85475c-a5ef-4a15-b00f-206e408528b2")
    return {"welcome": "welcome to  API, la temperatura del LST es: {id}".format(id = id)}

@app.get('/ac-status/{estado}')
def muestra_estado_AC(estado: str):
    return {"message": "Estado AC {estado}".format(estado = estado)}

@app.post('/ac-status')
async def cambiar_Estado_AC(statusJson: StatusJson):
    newStatus = estadoActual(statusJson.status)
    return {"message": "Estado de AC: {status}".format(status = newStatus)}