from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: float
    weight: float # kg
    height: float # meter
    allergies: List[str]
    contract_details: Dict[str,str]

# here we are computing bmi using two different fields
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print('BMI', patient.bmi)

patient_info = {'name': 'siam','email':'abc@hdfc.com', 'linkedin':'http://linkedin.com/1234','age':25, 'weight': 25.5, 'height':1.72,  'allergies':['pollen', 'dust'], 'contract_details': {'phone':'017895'} }

patient1 = Patient(**patient_info)

update_patient_data(patient1)