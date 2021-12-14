from typing import List
from fastapi import APIRouter, Depends, HTTPException
import aiofiles
import json

router = APIRouter(
    prefix="/d365",
    tags=["d365"],
    responses={404: {"description": "d365 not found"}},
)


@router.get("/getBaseData")
async def read_getbasedata():
    # Opening JSON file
    async with aiofiles.open('./app/data/d365/GetBaseData.json', mode='r') as f:
        contents = await f.read()
    d365_getbasedata = json.loads(contents)
    return d365_getbasedata


@router.get("/getItem")
async def read_getitem():
    async with aiofiles.open('./app/data/d365/GetItems.json', mode='r') as f:
        contents = await f.read()
    d365_getitems = json.loads(contents)
    return d365_getitems
