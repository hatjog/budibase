from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# get_token_header,
from app.routers import items, pong, song, d365

from app.db.db import init_db
import uvicorn

# app = FastAPI(dependencies=[Depends(get_query_token)])
app = FastAPI()

app.mount("/assets", StaticFiles(directory="./assets"), name="assets")

app.include_router(pong.router)
app.include_router(items.router)
app.include_router(song.router)
app.include_router(d365.router)


# app.include_router(
#     admin.router,
#     prefix="/admin",
#     tags=["admin"],
#     dependencies=[Depends(get_token_header)],
#     responses={418: {"description": "I'm a teapot"}},
# )


# @app.on_event("startup")
# async def on_startup():
#     await init_db()


@app.get("/")
async def root():
    return {"message": "Hello DXData dxfastapi Application!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8000)

