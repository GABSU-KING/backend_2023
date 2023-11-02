from fastapi import FastAPI
from core.db import database

app = FastAPI()
sleep_time = 10


@app.on_event("startup")
async def startup():
    await database.connect()
    print("okok")


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/")
def root():
    return {
        "message": "/"
    }

async def get_all_hellogabsu():
    query = "SELECT * FROM hellogabsu"
    data = await database.fetch_all(query)
    return [{**i} for i in data]


@app.get("/dbconnect")
async def dbconnect():
    temp = await get_all_hellogabsu()
    print("temp", temp) 
    return {
        "message": temp
    }
