from pydantic import BaseModel

class UserSchema(BaseModel):
    name: str
    email: str
    age: int
    Roll_number: int
    Department: str

    class Config:
        from_attributes = True

class UserUpdateAPIKey(BaseModel):
    api_key: str        
