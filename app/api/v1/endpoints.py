from app.core.config import CITIES
from app.services.weather_service import WeatherDataFetch
from app.services.open_meteo_client import Session, future_data_api


get_data = WeatherDataFetch(cities=CITIES,session=Session, url=future_data_api)
print(get_data.fetch_data())
