from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
import time
import pandas as pd
import models.models as m
import config as cfg
from sqlalchemy import create_engine

@asynccontextmanager
async def lifespan():
    #establish connection to the db
    engine = create_engine(url=cfg.AFFIX_DB_URL)
    yield
    

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
async def hello(name: str):
    return {"name": name, "greeting": f"hello {name}, how ya doing?"}


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = (time.perf_counter() - start_time) * 1000 #milliseconds
    response.headers["X-Process-Time"] = str(f"{process_time} ms")
    return response

@app.post("/data")
async def send_data(request: Request, data: m.DataSubmit):
    """
    This routes accept tabular data that is encoded in some way
    and saves the information to the DB
    """
    #for now assume input is a giant string for the CSV

    

