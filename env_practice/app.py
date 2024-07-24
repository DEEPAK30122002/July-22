from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv()


a = os.getenv('a')
b = os.getenv('b')
c = os.getenv('c')
d = os.getenv('d')
e = os.getenv('e')

app = FastAPI()

@app.get("/")
def read_root():
    return {"a": a, "b": b, "c": c, "d": d, "e": e}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
