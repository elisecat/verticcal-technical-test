from fastapi import FastAPI
from app.infraestructure.controller.weather_controller import router as weather_router

app = FastAPI()

# Registrar el controlador de clima
app.include_router(weather_router, prefix="/api", tags=["Weather"])
