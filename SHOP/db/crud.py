from sqlalchemy.orm import Session

from . import models, schemas


def get_author(db: Session, author_id: int):
    """ SELECT * FROM author WHERE author.id == [?]"""

    return db.query(models.Author).filter(models.Author.id == author_id).first() 

def get_all_author(db: Session):
    return db.query(models.Author).all()

def get_commodity_by_author(db: Session, author_id: int):
    return db.query(models.Commodity).filter(models.Commodity.author_id == author_id).all()

def create_author(db:Session, new_author: schemas.AuthorCreate):
    """ INSERT INTO author VALUES (?, ?)"""
    created_author = models.Author(name=new_author.name)
    db.add(created_author)
    db.commit()

    db.refresh(created_author)
    return created_author

def create_commodity(db: Session, new_commodity: schemas.CommodityCreate, author_id: int):
    db.add(models.Commodity(**new_commodity.model_dump(), author_id=author_id))
    db.commit()