from fastapi import FastAPI, Request
import time

app = FastAPI()


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
