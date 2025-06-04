# if we start to use a model pydantic  inside another model pydantic as a field then it would be nested model

from pydantic import BaseModel


# created this model for address 
class Address(BaseModel):
        city: str
        state: str
        pin: int
        
        
class Patient(BaseModel):
    
    name: str
    gender: str
    age: int
    address: Address
    # what if we only want the city name then it would be complex -or like this the address itself is a very complex data
    # in this kinda situation we have to create another model for address then use it inside the patient model
    
address_dic = {'city': 'dhaka', 'state': 'dhaka', 'pin': 1219}
address1 = Address(**address_dic)


patient_dic ={'name': 'siam', 'gender': 'male', 'age': 25, 'address': address1}

patient1 = Patient(**patient_dic)

temp = patient1.model_dump(include =['name']) # for python dict
temp2 = patient1.model_dump_json(exclude = ['name','gender']) # for json
temp3 = patient1.model_dump_json(exclude = {'address':['state']}) # removing state from address in json



print(temp)
print(type(temp)) 

print(temp2) 
print(type(temp2))

print(temp3)