import requests
import os
from app.domain.dto.weather_dto_response import ErrorDTO, WeatherResponseDTO
from app.domain.ports.weather_port import WeatherPort
from dotenv import load_dotenv
load_dotenv()

WEATHERSTACK_API_KEY = os.getenv("WEATHERSTACK_API_KEY", "your_default_api_key")
WEATHERSTACK_URL = "http://api.weatherstack.com/current"

class ExternalWeatherService(WeatherPort):
    def get_weather(self, city: str):
        """Obtiene los datos del clima de una ciudad usando Weatherstack."""
        params = {"query": city, "access_key": WEATHERSTACK_API_KEY}
        try:
            response = requests.get(WEATHERSTACK_URL, params=params)
            response.raise_for_status()
            data = response.json()
            # Si no hay clave "success", asumimos que la respuesta fue exitosa
            if not data.get("success", True):
                error = data.get("error", {})
                return WeatherResponseDTO(
                    success=False,
                    error=ErrorDTO(
                        code=error.get("code", 0),
                        type=error.get("type", "unknown_error"),
                        info=error.get("info", "No error details provided")
                    )
                )
            # Mapear datos válidos al DTO
            return WeatherResponseDTO(
                success=True,
                request=data.get("request"),
                location=data.get("location"),
                current=data.get("current")
            )
        except requests.HTTPError as e:
            raise ValueError(f"HTTP error: {e.response.status_code}")
        except requests.RequestException as e:
            raise ValueError(f"Request error: {str(e)}")

