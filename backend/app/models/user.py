from app.config.database import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    dob = Column(String(10))
    email = Column(String(255), unique=True, index=True) 
    password = Column(String(255))
    exp = Column("experience", Integer)
