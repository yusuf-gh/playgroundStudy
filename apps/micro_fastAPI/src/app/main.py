from fastapi import FastAPI

app = FastAPI(title="My Async Service")

@app.get("/")
async def health_check():
    return {"status": "ok"}

