from fastapi import FastAPI
from routers import router

app = FastAPI()


@app.get('/')
def hello_world():
    return 'Hello world'

app.include_router(router)