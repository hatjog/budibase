from sqlmodel import SQLModel, Field
from typing import Optional, List
from pydantic import BaseModel


class ItemBase(SQLModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class Item(ItemBase, table=True):
    id: int = Field(default=None, primary_key=True)


class ItemCreate(ItemBase):
    pass


class ListItems(BaseModel):
    list_items: List[Item]



