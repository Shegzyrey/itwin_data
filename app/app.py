from fastapi import FastAPI, WebSocket
from fastapi.responses import JSONResponse
from datetime import datetime, timedelta
import random
import uvicorn

app = FastAPI()
doctors = ["Dr. Smaith", "Dr. Minha", ""]
room_states = {
    "Room101": {"status": "available", "lastUpdated": str(datetime.now().isoformat())},
    "ConsultationA": {"status": "occupied", "currentPatientId": "P001"},
    "ConsultationB": {"status": "cleaning"},
}

@app.get("/rooms")
async def get_room_status():
    return JSONResponse(content=room_states)

@app.get("/patient/{pid}")
async def get_patient_status(pid: str):
    return {
        "patientId": pid,
        "currentLocation": random.choice(["Entrance", "Queue", "Corridor"]),
        "appointmentTime": str(datetime.now().isoformat()),
        "assignedDoctor": "Dr. Smith",
        "roomNumber": "201",
        "priorityLevel": "normal",
    }

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        # Simulate patient movement
        patient_data = {
            "patientId": "P001",
            "location": random.choice(["WaitingArea", "ConsultationA", "Corridor"]),
            "timestamp": str(datetime.now().isoformat())
        }
        await websocket.send_json(patient_data)