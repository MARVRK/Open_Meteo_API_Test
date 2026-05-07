from pydantic import BaseModel
from datetime import date

class GetWeather(BaseModel):
    start_date: date
    end_date: date