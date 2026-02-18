from pydantic import BaseModel

class UserSchema(BaseModel):
    name: str

    class Config:
        from_attributes = True
