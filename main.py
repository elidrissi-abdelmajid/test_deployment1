from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def func():
    return {
        "message1": "hello world",
        "AI1" : "comment tu vas mon frère ? ",
        "message2" : "je suis trés bien hmdullah et toi  comment allez vous ?",
        "AI2": "super, merci",
        "message3":"iwa mzyan assidi",
        "AI3": "layhfdk abro"
    }