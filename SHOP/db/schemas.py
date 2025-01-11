from pydantic import BaseModel, Field
from typing import Annotated


class CommodityBase(BaseModel): 
    title: str 
    price: Annotated[int, Field(ge=1, description="Мінімум 1 грн") ]

class CommodityUpdate(CommodityBase):
    pass

class CommodityCreate(CommodityBase):
    pass

class Commodity(CommodityBase):
    id: int
    author_id: int

    class Config:
        from_attributes = True

class AuthorBase(BaseModel):
    name: Annotated[str, Field(
                            min_length=3,
                            max_length=30,
                            description="Імя автора 1-30 символів"
                        )]
    
class AuthorCreate(AuthorBase):
    pass

class AuthorUpdate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int
    commodities: list[Commodity] = []

    class Config:
        from_attributes = True