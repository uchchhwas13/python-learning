from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class Cart(BaseModel):
    user_id: int
    items: List[str]
    quantities: Dict[str, int]

class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None

class Employee(BaseModel):
    id: int
    name: str = Field(
        ..., 
        min_length = 3,
        max_length = 15,
        description = "Employee name",
        example="John doe"
        )
    department: Optional[str] = 'General'
    salary: float = Field(..., gt=10000)

input_data = {'id':101, 'name': 'John doe', 'salary': 11000}
employee = Employee(**input_data)

print(employee)