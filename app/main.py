from fastapi import FastAPI
import uvicorn
from app.api.v1.endpoints import router as weather_endpoint


app = FastAPI(title="Weather Scoring API", version="1.0.0")
app.include_router(router=weather_endpoint, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)