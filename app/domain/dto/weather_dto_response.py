from pydantic import BaseModel
from typing import List, Optional

class RequestDTO(BaseModel):
    type: str
    query: str
    language: str
    unit: str

class ErrorDTO(BaseModel):
    code: int
    type: str
    info: str    

class LocationDTO(BaseModel):
    name: str
    country: str
    region: str
    lat: str
    lon: str
    timezone_id: str
    localtime: str
    localtime_epoch: int
    utc_offset: str

class CurrentDTO(BaseModel):
    observation_time: str
    temperature: int
    weather_code: int
    weather_icons: List[str]
    weather_descriptions: List[str]
    wind_speed: int
    wind_degree: int
    wind_dir: str
    pressure: int
    precip: float
    humidity: int
    cloudcover: int
    feelslike: int
    uv_index: int
    visibility: int
    is_day: str

class WeatherResponseDTO(BaseModel):
    success: Optional[bool] = True
    error: Optional[ErrorDTO] = None
    request: Optional[RequestDTO] = None
    location: Optional[LocationDTO] = None
    current: Optional[CurrentDTO] = None
