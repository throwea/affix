from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Request
import time
import pandas as pd
import models.models as m
import config as cfg
from sqlalchemy import create_engine
from middleware.logger import logger
from llm.pipelines import execute_pipeline

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

@app.post("/chat", response_model=m.ChatResponse)
async def chat(request: Request, data: m.ChatRequest):
    """
    This routes accept tabular data that is encoded in some way
    and saves the information to the DB
    """
    try:
        res = execute_pipeline(data.user_msg)
        response = m.ChatResponse(response=res, success=True)
        return response
    except Exception as e:
        logger.error(f"chat failed. User msg: {data.user_msg}, User ID: {data.user_id}")
        raise HTTPException(status_code=500, detail="internal failure") #TODO: add error class to capture and propagate errors to frontend



    

