from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"Hello and Welcome to task two"}