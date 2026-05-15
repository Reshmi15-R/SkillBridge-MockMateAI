from sqlalchemy.orm import Session
from app.exception.dbexception import DatabaseConnectionException
from app.exception.handler import db_exception_handler
from fastapi import Depends, FastAPI, status
from app.dto.signup import SignupRequest
from app.models.user import User
from sqlalchemy import text
from app.config.database import Base, engine, get_db
from app.services.Userservice import UserService
from app.exception.dbexception import DatabaseConnectionException
from app.dto.apiresponse import *
app=FastAPI()

app.add_exception_handler(DatabaseConnectionException, db_exception_handler)

Base.metadata.create_all(bind=engine)
@app.on_event("startup")
def startup_db_check():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        print("Database connection successful ")
    except Exception as e:
        raise DatabaseConnectionException(str(e))
    

@app.post("/signup",response_model=SignupApiResponse,status_code=status.HTTP_201_CREATED)
def signup(a:SignupRequest,db: Session = Depends(get_db)):
    user=UserService(db,a)
    new_user=user.create_user()
    return {"data":new_user}

    
@app.get("/login")
def login():
    pass   

