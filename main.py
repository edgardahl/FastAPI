from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!", }

@app.post("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!", "test": "This is a test!"}