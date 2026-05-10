from app.exception.dbexception import DatabaseConnectionException
from app.exception.handler import db_exception_handler
from fastapi import FastAPI

from backend.app.dto.signup import SignupRequest

app=FastAPI()

app.add_exception_handler(DatabaseConnectionException, db_exception_handler)

from sqlalchemy import text
from app.config.database import engine
from app.exception.dbexception import DatabaseConnectionException

@app.on_event("startup")
def startup_db_check():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        print("Database connection successful ")
    except Exception as e:
        raise DatabaseConnectionException(str(e))
    

# @app.post("/signup")
# def signup(user:SignupRequest ):
    
