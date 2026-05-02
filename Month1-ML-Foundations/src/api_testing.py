from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"msg": "Hey there welcome to my app."}

@app.get("/info")
def info():
    return {"Name": "Sourav Kumar Sahu",
            "City": "Sambalpur",
            "Contact": "9090800765"}