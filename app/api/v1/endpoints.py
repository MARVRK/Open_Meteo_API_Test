from datetime import date, timedelta

from app.core.config import CITIES
from app.services.weather_service import WeatherDataFetch
from app.services.open_meteo_client import Session, future_data_api
from app.services.scoring_service import ScoringService
from fastapi import APIRouter, Query

router = APIRouter()

@router.get('/cities-scores')
async def get_citiies_scores(start_date: date = Query(default=None),
                             end_date: date = Query(default=None)):

    get_data = WeatherDataFetch (cities=CITIES, session=Session, url=future_data_api)
    scores = ScoringService ().calculate_scores (weather_data=get_data.fetch_data (start_date=start_date,
                                                                              end_date=end_date))

    if not start_date:
        yesterday = date.today () - timedelta (days=1)
        start_date = yesterday
        end_date = yesterday

    return {"start_date": f"{start_date}", "end_date": f"{end_date}", "cities": scores}
