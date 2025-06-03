from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict, Optional

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: Optional [bool] = None
    allergies: List[str]
    contract_details: Dict[str,str]


    # now this time we'll check if age is > 60 then in your contract_details you will have to add emergency number.
    @model_validator(mode = 'after')
    def validate_emergency_contact(cls, model):
        
        if model.age>60 and 'emergency'  not in model.contract_details:
            raise ValueError("Patients older than 60 must have an emergency contract")
        return model

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print('update')

patient_info = {'name': 'siam','email':'abc@hdfc.com', 'linkedin':'http://linkedin.com/1234','age':25, 'weight': 25.5,  'allergies':['pollen', 'dust'], 'contract_details': {'phone':'017895'} }

patient1 = Patient (**patient_info)

update_patient_data(patient1)
