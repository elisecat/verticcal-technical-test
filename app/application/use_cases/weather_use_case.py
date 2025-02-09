from app.domain.ports.weather_port import WeatherPort
from app.domain.dto.weather_dto_response import WeatherResponseDTO

class WeatherUseCase:
    def __init__(self, weather_port: WeatherPort):
        self.weather_port = weather_port

    def get_weather_for_city(self, city: str) -> WeatherResponseDTO:
        """Obtiene los datos del clima de una ciudad."""
        return self.weather_port.get_weather(city)
