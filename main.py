from fastapi import FastAPI, Depends  # <--- 1. Added Depends here
from schemas import detailcreate, details as detailschema
from sqlalchemy.orm import Session
from database import SessionLocal
from models import details
from database import Base, engine
from models import details
from fastapi import HTTPException, status
from schemas import detailupdate
Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
     db = SessionLocal()
     try:
          yield db
     finally:
          db.close()

@app.post("/details", response_model=detailschema)

def create(detail: detailcreate, db: Session = Depends(get_db)):
     
     db_detail = details(**detail.dict()) 
     
     db.add(db_detail)
     db.commit()
     db.refresh(db_detail)
     return db_detail

@app.get("/details/{id}",response_model=detailschema)
def getdetail(id:int,db:Session=Depends(get_db)):
   gets=db.get(details,id)
   
   db.commit()
   db.refresh(gets)
   return gets

@app.delete("/details/{id}",response_model=detailschema)
def removedetail(id:int,db:Session=Depends(get_db)):

     removed=db.query(details).filter(details.id == id).first()
     if not removed:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Detail not found"
        )
     db.delete(removed)
     db.commit()
     return removed

@app.put("/details/{id}",response_model=detailschema)
def update(id:int,request:detailupdate,db:Session=Depends(get_db)):
    update=db.query(details).filter(details.id==id).first()
    if not update:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Detail not found"
        )
    update_data = request.model_dump(exclude_unset=True)
    for key,value in update_data.items():
        setattr(update,key,value)

    db.commit()
    db.refresh(update)
    return update

       