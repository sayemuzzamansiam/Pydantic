#### step 1:

"""first install pydantic then we will build a pydantic model to build schema for  data """
from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator   #these are specific to pydantic
# we have to do pip install pydantic[email] for email
from typing import List, Dict, Optional, Annotated


# validation - define your ideal schema 
class Patient(BaseModel):
    name: Annotated[str, Field(max_length=15, title = "name of the patient", description="give the name of the patient in less than 50 chars", examples=['siam','midul'])] # here we are telling the mode name should be str and age should be intiger. we can also add meta data using Annotate and Field together. just like how we used it in here.
    email: EmailStr
    linkedin: AnyUrl 
    age: int
    weight: Annotated[float, Field(gt=0, strict=True)] # now no one can set the value of weight to negetive value. so using Field we can customized the data. can add different level of constraint. Field fucntion is really cool. it can attached meta data also.
    # strict will supress the power of pydentince type convergence 

    married: Optional[bool] =None # making this value optional with the help of Optional and None.
    allergies: List[str] # list of strings for this we need to import List from typing module
    contract_details: Dict[str, str]

# required, optional and default field we can make it all.
# field validator - we've created a field validtor on email to supre customise it.
    @field_validator('email')
    @classmethod
    def email_validator(cls,value):

        valid_domains =['hdfc.com','icici.com'] 
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError("Not a valid Domain")
        return value

# let's say you want to set your patient's name to capital letter. - performing transformation
    @field_validator('name',mode ='after') # default mode is after.
    @classmethod
    def transfrom_name(cls,  value):
        return value.upper()
    
    @field_validator('age', mode = 'after') # we can operate it in two mode.
    @classmethod
    def validation_age(cls,value):
        if 0<value<100:
            return value
        else:
            raise ValueError("Age should be in between 0 and 100")




## step 2:

""" here we will create an obj of this pydantic model """

patient_info = {'name': 'siam','email':'abc@hdfc.com', 'linkedin':'http://linkedin.com/1234','age':25, 'weight': 25.5,  'allergies':['pollen', 'dust'], 'contract_details': {'phone':'017895'} }

patient1 = Patient (**patient_info) # here we're creating an instance of Patient class and then applying that on our patient_info to type validate it - ** to unpack dictionary



## step 3:

# our insert_patient_data function is getting a pydantic obj called patient
def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print('inserted')

# now i can create multiple funtion like this one and use the same data validation for that without repeating all the work 
def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print('update')


insert_patient_data(patient1)
update_patient_data(patient1)
# now the type validation is done by pydantic. now if anyone type tweenty instade of 20 it will catch an error.

#field validator is only for one field but what if you need to vlidated on the base of two field to validate your data. then we use model validator