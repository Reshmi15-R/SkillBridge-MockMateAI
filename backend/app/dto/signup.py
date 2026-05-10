from pydantic import BaseModel

class SignupRequest(BaseModel):
    email: str
    password: str
    name: str
    dob: str
    experience: int= None

class SignupResponse(BaseModel):
    name:str

    