from pydantic import BaseModel
class detailBase(BaseModel):
    first_name:str
    second_name:str
    Class:str
    Sec:str

class detailcreate(detailBase):
    pass
class detailupdate(detailBase):
    pass

class details(detailBase):
    id:int
    class Config:
        orm_mode=True

        
