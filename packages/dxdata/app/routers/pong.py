from fastapi import APIRouter

import httpx
import asyncio


router = APIRouter(
    prefix="/pong",
    tags=["pong"],
    #dependencies=[], # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Pong Not found"}},
)


@router.get("/pong/")
async def read_pong():
    await asyncio.sleep(1)
    return {"ping_id": 99}


async def request(client, id):
    url = f'http://127.0.0.1:8000/pong/ping/{id}'
    response = await client.get(url)
    return response.text


async def do_ping(ping_id: int) -> str:
    async with httpx.AsyncClient() as client:
        response = await request(client, ping_id)
    return response


async def do_big_ping(ping_id: int):
    async with httpx.AsyncClient() as client:
        tasks = [request(client, i) for i in range(100)]
        result = await asyncio.gather(*tasks)
    return result


@router.get("/pong/{ping_id}")
async def read_pong(ping_id: int):
    await asyncio.sleep(0)
    result = await do_ping(ping_id)
    return {"ping_id": result}


@router.get("/bigpong/{ping_id}")
async def read_bigpong(ping_id: int):
    result = await do_big_ping(ping_id)
    return {"ping_id": result}


@router.get("/ping/{ping_id}")
async def read_pong(ping_id: int):
    await asyncio.sleep(1)
    return {"ping_id": ping_id + 3}


@router.post("/ping/")
async def do_pong(ping_id: int):
    await asyncio.sleep(1)
    return {"ping_id": ping_id + 2}
