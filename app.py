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


"""# Hospital Management System API
This API provides endpoints to manage hospital room statuses, patient information, and real-time updates via Web
doctors = ["Dr. Smaith", "Dr. Minha", ""]

room_states = [
    {
      "ecInstanceId": "0x20000001756",
      "roomId": "ConsultationA",
      "status": "occupied",
      "currentPatientId": "P001",
      "estimatedReleaseTime": str(datetime.now().isoformat()),
      "needsCleaning": False,
      "assignedDoctor": "Dr. Smith",
      "floor": "1",
    },
    {
      "ecInstanceId": "0x200000018cb",
      "status": "available",
      "currentPatientId": 'null',
      "estimatedReleaseTime": 'null',
      "needsCleaning": False,
      "assignedDoctor": "Dr. Lee",
      "floor": "1"
    }
]

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
"""
# Doctors list
doctors = ["Dr. Smith", "Dr. Minha", "Dr. Lee"]

# Example status values
STATUS_OPTIONS = ["occupied", "available", "cleaning"]
# Example patient ID
DEFAULT_PATIENT_ID = "P001"

# ECInstanceIds
INSTANCE_IDS = {
    "ConsultationA": "0x20000001956",
    "ConsultationB": "0x20000001957",
    "ConsultationC": "0x20000001986",
    "ConsultationD": "0x20000001987",
    "ConsultationE": "0x200000019d6",
    "ConsultationF": "0x200000019d7",
    "ConsultationG": "0x200000019d8",
    "ConsultationH": "0x200000019d9",
    "ConsultationI": "0x20000001a08",
    "ConsultationJ": "0x20000001a09",
    "ConsultationK": "0x20000001a58",
    "ConsultationL": "0x20000001a59",
    "ConsultationM": "0x20000001a5a",
    "ConsultationN": "0x20000001a5b",
    "ConsultationO": "0x20000001b8c",
    "ConsultationP": "0x20000001b8d",
    "ConsultationQ": "0x20000001b8e",
    "ConsultationR": "0x20000001b8f",
    "ConsultationS": "0x20000001b90",
    "ConsultationT": "0x20000001d40",
    "ConsultationU": "0x20000001d41",
    "ConsultationV": "0x20000001d42",
    "ConsultationW": "0x20000001d43",
    "ConsultationX": "0x20000001d44",
    "ConsultationY": "0x20000001d8a",
    "ConsultationZ": "0x20000001dd7",
    "ConsultationAA": "0x20000001dd9",
    "ConsultationAB": "0x20000001de6",
    "ConsultationAC": "0x20000001de9",
    "ConsultationAD": "0x20000001dea",
    "ConsultationAE": "0x20000001deb",
    "ConsultationAF": "0x20000001dee",
    "ConsultationAG": "0x20000001def"
}

# Room states
def generate_room_states():
    states = []
    for room_name, ec_id in INSTANCE_IDS.items():
        status = random.choice(STATUS_OPTIONS)
        assigned_doctor = random.choice(doctors)
        needs_cleaning = status == "cleaning"
        patient_id = "P00" + str(random.randint(1, 9)) if status == "occupied" else None
        estimated_time = (
            (datetime.now() + timedelta(minutes=random.randint(10, 60))).isoformat()
            if status == "occupied"
            else None
        )
        states.append(
            {
                "ecInstanceId": ec_id,
                "roomId": room_name,
                "status": status,
                "currentPatientId": patient_id,
                "estimatedReleaseTime": estimated_time,
                "needsCleaning": needs_cleaning,
                "assignedDoctor": assigned_doctor,
                "floor": str(random.choice([1, 2])),
            }
        )
    return states

@app.get("/")
async def root():
    return {"message": "Welcome to the Hospital Management System API"}

@app.get("/rooms")
async def get_room_status():
    # Generate fresh states every time
    dynamic_states = generate_room_states()
    return JSONResponse(content=dynamic_states)

@app.get("/patient/{pid}")
async def get_patient_status(pid: str):
    return {
        "patientId": pid,
        "currentLocation": random.choice(["Entrance", "Queue", "Corridor"]),
        "appointmentTime": datetime.now().isoformat(),
        "assignedDoctor": random.choice(doctors),
        "roomNumber": "201",
        "priorityLevel": random.choice(["normal", "urgent"]),
    }

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        patient_data = {
            "patientId": DEFAULT_PATIENT_ID,
            "location": random.choice(["WaitingArea", "ConsultationA", "Corridor"]),
            "timestamp": datetime.now().isoformat(),
        }
        await websocket.send_json(patient_data)