from fastapi import FastAPI, WebSocket
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timedelta
import random
import uvicorn

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Or ["*"] for dev only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



doctors = ["Dr. Smaith", "Dr. Minha", ""]
room_states =   {
    "roomId": "ConsultationA",
    "status": "occupied",
    "currentPatientId": "P001",
    "estimatedReleaseTime": str(datetime.now().isoformat()),
    "needsCleaning": True,
    "assignedDoctor": "Dr. Smith",
    "floor": "1",
  }

@app.get("/")
async def root():
    return {"message": "Welcome to the Hospital Management System API"}

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