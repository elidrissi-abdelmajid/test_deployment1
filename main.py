from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def func():
    return {
        "message":"Bonjour !"
    }
@app.get("/predict")
def hello():
    return {
        "message":"hello again"
    }