from pydantic import BaseModel
from app.dto.signup import SignupResponse
class ApiResponse(BaseModel):
    data:SignupResponse
    message:str