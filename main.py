from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API працює"}

@app.get("/calculate")
def calculate(km: float, liters: float):
    if km <= 0:
        return JSONResponse(
            status_code=400,
            content={"error": "km must be > 0"}
        )
    consumption = liters / km * 100
    return {"consumption": round(consumption, 2)}

# НЕ потрібно запускати uvicorn тут для Render
# Render сам виконає команду uvicorn через Start Command