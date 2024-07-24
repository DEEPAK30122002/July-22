from fastapi import FastAPI
from settings import settings
import uvicorn

app = FastAPI()

@app.get('/')
def first():
    return "Your are now in dynamic space the /value and /a or some other"

@app.get("/{variable}")
def read_variable(variable: str):
    value = settings.get_attribute(variable)
    return {variable: value}

