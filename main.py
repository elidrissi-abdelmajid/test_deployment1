from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def func():
    return {
        "message": "hello world",
        "AI" : "comment tu vas mon frère ? ",
        "message" : "je suis trés bien hmdullah et toi  comment allez vous ?",
        "AI": "super, merci"
    }