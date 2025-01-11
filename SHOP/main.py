from random import randint
from fastapi import FastAPI, Path, Request, Response, Depends
from pydantic import BaseModel, Field 
from typing import Annotated

from db import models, schemas, crud
from db.database import sesion_local, engine
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from jose import jwt

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = sesion_local()
    try:
        yield db
    finally:
        db.close()

#створити функцію яка за GET запитом повертає всю бібліотеку(ф-ція без параметрів) 
@app.get("/authors") 
def get_all_author(db: Session = Depends(get_db)): 

    return crud.get_all_author(db)

@app.post("/create/author")
def create_author(new_author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    return crud.create_author(db, new_author)

@app.post("/create/commodity")
def create_commodity(new_commodity: schemas.CommodityCreate, id_author: int, db: Session = Depends(get_db)):
    crud.create_commodity(db, new_commodity, id_author)

@app.get("/commodity/author")
def get_commodities_by_author(author_id: int, db: Session = Depends(get_db)):
    return crud.get_commodity_by_author(db, author_id)

@app.get("/author/{id}", response_model=schemas.Author) 
def get_author(id: int, db: Session = Depends(get_db)): 
    return crud.get_author(db, id)