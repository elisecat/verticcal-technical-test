from pydantic import BaseModel

class FilterRequestDTO(BaseModel):
    city: str
    attribute: str
