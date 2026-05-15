from pydantic import BaseModel,ConfigDict

class SignupRequest(BaseModel):
    email: str
    password: str
    name: str
    dob: str
    experience: int

class SignupResponse(BaseModel):
    name:str
    model_config=ConfigDict(from_attributes=True)