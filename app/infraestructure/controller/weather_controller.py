from fastapi import APIRouter, HTTPException, Depends
from app.application.use_cases.weather_use_case import WeatherUseCase
from app.domain.dto.weather_dto_request import FilterRequestDTO
from app.services.adapters.external_service import ExternalWeatherService
from app.domain.dto.weather_dto_response import WeatherResponseDTO

router = APIRouter()

# Inicializar los servicios y casos de uso 
external_weather_service = ExternalWeatherService()
weather_use_case = WeatherUseCase(external_weather_service)

@router.get("/external-data", response_model=WeatherResponseDTO)
def get_external_data(city: str):
    """
    Devuelve los datos consumidos de la API pública.
    """
    try:
        return weather_use_case.get_weather_for_city(city)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/external-data/filter")
def filter_external_data(request: FilterRequestDTO):
    """
    Filtra o procesa los datos descargados de la API pública según un atributo.
    
    Ejemplo de atributos: temperature, humidity, wind_speed.
    """
    try:
        data = weather_use_case.get_weather_for_city(request.city)
        current = data.current.dict() if data.current else {}

        if request.attribute not in current:
            raise HTTPException(status_code=400, detail=f"Atributo '{request.attribute}' no encontrado en los datos actuales.")

        return {"city": request.city, "attribute": request.attribute, "value": current[request.attribute]}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))