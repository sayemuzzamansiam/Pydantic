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

print(patient1)
print(patient1.address.city)
print(patient1.address.state)
print(patient1.address.pin)

# last thing:
# how can we export this pydantic model obj to json or python dict
# pydantic has built-in methods that give us to to power to export our existing pydantic model obj as json or python dict. 

