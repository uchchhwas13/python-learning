from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    created_at: datetime
    address: Address
    tags: List[str] = []
    
    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')}
    )


user = User(
    id = 1,
    name =  "John Doe",
    email = "johndoe@gmail.com",
    created_at = datetime(2024, 3, 15, 14, 30),
    address = Address(
        street = "street",
        city = "city",
        zip_code = "zip_code"
        
    ),
    tags = ["premium", "subscriber"]
)

#Using model_dump() -> dict

python_dict = user.model_dump()
print(python_dict)

print("\n\n=====================\n\n")
#Using model_dump_json()
json_str = user.model_dump_json()
print("Json string:", json_str)
