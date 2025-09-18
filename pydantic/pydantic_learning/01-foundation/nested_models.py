from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']]

Comment.model_rebuild()

address = Address(
    street = "Shewrapara to Taltola road",
    city = "Dhaka",
    postal_code = "1216"
)

user = User(
    id = 1,
    name = "Roy",
    address = address
)

comment = Comment(
    id = 1,
    content = "First Comment",
    replies = [
        Comment(id=2, content = "First reply"),
        Comment(id=3, content = "Second reply"),
    ]
)