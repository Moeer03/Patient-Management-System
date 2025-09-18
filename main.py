from fastapi import FastAPI, Path, HTTPException, Query
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
from fastapi.responses import JSONResponse
import json

app = FastAPI()

class Patient(BaseModel):
    
    id: Annotated[str, Field(..., description="ID of the patient", example="P001")]
    name: Annotated[str, Field(..., description="Name of the patient")]
    city: Annotated[str, Field(..., description="City where the patient is living")]
    age: Annotated[int, Field(..., gt=0, lt=120, description="Age of the patient")]
    gender: Annotated[Literal['male', 'female', 'others'], Field(..., description="Gender of the patient")]
    height: Annotated[float, Field(..., gt=0, description="Height of the patient in mtrs")]
    weight: Annotated[float, Field(..., gt=0, description="Weight of the patient in kgs")]
    
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2), 2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal"
        elif self.bmi < 30:
            return "Overweight"
        else:
            return "Obese"

class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None, gt=0)]
    gender: Annotated[Optional[Literal['male', 'female']], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None, gt=0)]
    weight: Annotated[Optional[float], Field(default=None, gt=0)]

def load_data():
    with open('patients.json', 'r') as file:
        return json.load(file)

def save_data(data):
    with open('patients.json', 'w+') as file:
        json.dump(data, file)
    
@app.get("/")
def hello():
    return {"message": 'Pateint Management System'}

@app.get("/about")
def about():
    return {"message": "This is a fully functional api to manage your pateints."}

@app.get('/view')
def view():
    return load_data()

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description="The ID of the patient to retrieve", example="P001")):
    patient_id = patient_id.upper()
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    return HTTPException(status_code=404, detail="Patient not found")

@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description="sort on the basis of height, weight, bmi"), order: str = Query('asc', description="asc or desc")):
    valid_feilds = ['height', 'weight', 'bmi']
    if sort_by not in valid_feilds:
        return HTTPException(status_code=400, detail=f"Invalid sort field select drom {valid_feilds}")
    
    if order not in ['asc', 'desc']:
        return HTTPException(status_code=400, detail="Order must be 'asc' or 'desc'")
    
    data = load_data()
    
    sort_order = True if order == 'desc' else False
    sorted_data = sorted(data.values(), key=lambda x:x.get(sort_by, 0), reverse = sort_order)
    return sorted_data

@app.post('/create')
def create_patient(patient: Patient):
    data = load_data()

    # check if the patient already exists
    if patient.id in data:
        raise HTTPException(status_code=400, detail='Patient already exists')

    # new patient add to the database
    data[patient.id] = patient.model_dump(exclude=['id'])

    # save into the json file
    save_data(data)

    return JSONResponse(status_code=201, content={'message':'patient created successfully'})

@app.put('/edit/{patient_id}')
def update_pateint(patient_id: str, pateint_update: PatientUpdate):
    
    data = load_data()
    
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    excisting_patient_info = data[patient_id]
    
    updated_patient_info = pateint_update.model_dump(exclude_unset=True)
    
    for key, value in updated_patient_info.items():
        excisting_patient_info[key] = value
    
    # excisting_patient_info -> pydantic object -> updated bmi + verdict -> pydantic obj. -> dict
    
    excisting_patient_info['id'] = patient_id
    patient_pydantic_obj = Patient(**excisting_patient_info)
    excisting_patient_info = patient_pydantic_obj.model_dump(exclude=['id'])
    
    data[patient_id] = excisting_patient_info
    
    save_data(data)
    
    return JSONResponse(status_code=200, content={'message':'patient updated successfully'})

@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):

    # load data
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')
    
    del data[patient_id]

    save_data(data)

    return JSONResponse(status_code=200, content={'message':'patient deleted'})