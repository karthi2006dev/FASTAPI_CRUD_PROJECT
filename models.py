from sqlalchemy import Column,Integer,String
from database import  Base

class details(Base):
    __tablename__="details"
    id=Column(Integer,primary_key=True,index=True)
    first_name=Column(String,nullable=False)
    second_name=Column(String,nullable=False)
    Class=Column(String,nullable=False)
    Sec=Column(String,nullable=False)
    
