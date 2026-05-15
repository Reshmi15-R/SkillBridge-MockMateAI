from pydantic import BaseModel
from typing import Generic , TypeVar
from app.dto.signup import SignupResponse

T = TypeVar('T')

class ApiResponse(BaseModel,Generic[T]):
    data: T
    message:str

class SignupApiResponse(ApiResponse[SignupResponse]):
    message:str="User Redistered Succesfully"