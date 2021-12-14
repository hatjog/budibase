from typing import List

from fastapi import APIRouter, Depends, HTTPException
from ..dependencies import get_token_header
from app.models.items import Item, ItemCreate, ListItems

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.db import get_session


router = APIRouter(
    prefix="/items",
    tags=["items"],
#    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


item_catalog = [
        Item(name="IPhone12", description="Old", price=1000, tax=0.20),
        Item(name="IPhone13", description="New", price=1250, tax=0.20),
    ]


@router.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@router.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


@router.get("/", response_model=List[Item])
async def read_item():
    return item_catalog


@router.get("", response_model=List[Item])
async def get_songs(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Item))
    items = result.scalars().all()
    return items # [Item(name=song.name, artist=song.artist, id=song.id) for song in songs]


@router.get("/list_items/", response_model=ListItems)
async def read_list_items():
    listitems = ListItems(list_items=item_catalog)
    return listitems


@router.post("")
async def add_item(item: ItemCreate, session: AsyncSession = Depends(get_session)):
    item = Item(name=item.name, tax=item.tax, price=item.price, description=item.description)
    session.add(item)
    await session.commit()
    await session.refresh(item)
    return item


# @router.post("/")
# async def create_item(item: Item):
#     item_dict = item.dict()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax})
#     return item_dict


@router.get("/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@router.put(
    "/{item_id}",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
)
async def update_item(item_id: str):
    if item_id != "plumbus":
        raise HTTPException(
            status_code=403, detail="You can only update the item: plumbus"
        )
    return {"item_id": item_id, "name": "The great Plumbus"}
