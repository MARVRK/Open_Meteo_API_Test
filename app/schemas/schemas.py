from pydantic import BaseModel
from datetime import date

class GetWeather(BaseModel):
    start_date: date | None = None
    end_date: date | None = None