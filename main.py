from fastapi import FastAPI
import json

from models import Patient

app = FastAPI()

with open("patients.json", "r") as f:
    patient_list = json.load(f)

patients: list[Patient] = []

for patient in patient_list:
    patients.append(Patient(**patient))


@app.get("/patients")
async def get_patients() -> list[Patient]:
    return patients

@app.post("/patients")
async def add_patient(patient_details: Patient):
    patients.append(patient_details)

@app.put("/patient/{first_name}")
async def update_patient(first_name: str, updated_patient: Patient):
    for i, patient in enumerate(patients):
        if patient.first_name == first_name:
            patients[i] = updated_patient
            return

@app.delete("/patients/{first_name}")
async def delete_patient(first_name: str):
    for i, patient in enumerate(patients):
        if patient.first_name == first_name:
            patients.pop(i)
            return



# Use the first name as the unique identifier. For example, in the PUT route, you'd have something like this: "/patients/{first_name}"
