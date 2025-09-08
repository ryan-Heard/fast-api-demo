from fastapi import FastAPI

app = FastAPI()
print("Starting FastAPI application...")


@app.get("/")
async def root():
    return {"message": "Hello World"}
