from datetime import date, timedelta
from typing import Callable
from statistics import mean

class WeatherDataFetch:
    def __init__ (self, cities: list[dict], url: str, session: Callable):
        self.cities = cities
        self.url = url
        self.session = session

    def fetch_data (self, start_date: date = None, end_date: date = None) -> dict[str,dict]:
        if not self.cities:
            raise ValueError ("no cities provided")

        # fetching data from old URl + changing dates range on yesterday if no start date provided
        if not start_date:
            start_date = date.today () - timedelta (days=1)
            end_date = start_date
            self.url = "https://archive-api.open-meteo.com/v1/archive"

        # gathering all cities lat and long coordinates
        lats = [city["lat"] for city in self.cities]
        long = [city["lon"] for city in self.cities]

        # settings of data which we want to fetch
        params = {"latitude": lats,
                  "longitude": long,
                  "hourly": ["temperature_2m", "wind_speed_10m", "relative_humidity_2m", "cloud_cover"],
                  "start_date": str (start_date),
                  "end_date": str (end_date),
                  "timezone": "auto"}

        try:
            response =  self.session.weather_api(url=self.url,params=params)
        except Exception as e:
            raise ValueError(f"Failed Weather Get request: {e}")

        storage = {}

        for i, res in enumerate(response):
            city_name = self.cities[i]["name"]
            hourly = res.Hourly()

            temp_data = hourly.Variables (0).ValuesAsNumpy()
            wind_data = hourly.Variables (1).ValuesAsNumpy()
            humidity_data = hourly.Variables (2).ValuesAsNumpy()
            cloud_data = hourly.Variables (3).ValuesAsNumpy()
            # by using method "mean" we can calculate average date with floating number
            storage[city_name] = {"temperature_avg": float(mean(temp_data)),
                                  "wind_speed_avg":  float(mean(wind_data)),
                                  "humidity_avg":    float(mean(humidity_data)),
                                  "cloud_cover_avg": float(mean(cloud_data))}
        return storage


