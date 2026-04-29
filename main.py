from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "My first FastAPI Server"}

@app.get("/about")
def about():
    return {'data': 'This is about page'}

@app.get("/contact")
def contact():
    return {"email": "souwe34@gmail.com"}

@app.get("/add")
def add(a: int, b: int):
    return {"result": a+b}