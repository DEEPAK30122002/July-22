from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return{'example':'This is a example'}