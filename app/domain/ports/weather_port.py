from typing import Protocol
from app.domain.dto.weather_dto_response import WeatherResponseDTO

class WeatherPort(Protocol):
    def get_weather(self, city: str) -> WeatherResponseDTO:
        """Define el contrato para obtener el clima de una ciudad."""
