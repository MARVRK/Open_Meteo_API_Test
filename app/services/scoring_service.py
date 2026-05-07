class ScoringService:
    WEIGHTS = {"temperature": 0.35,
               "wind_speed": 0.20,
               "humidity": 0.20,
               "cloud_cover": 0.25}


    def calculate_scores (self, weather_data: dict) -> list:
        results = []

        for city, metrics in weather_data.items ():
            score = self._calculate_city_score (metrics)
            results.append ({"city": city,**metrics, "total_score": score})

        return results

    def _calculate_city_score (self, metrics: dict) -> float:
        temp_score = self._temp_score (metrics["temperature_avg"])
        wind_score = self._wind_score (metrics["wind_speed_avg"])
        humidity_score = self._humidity_score (metrics["humidity_avg"])
        cloud_score = self._cloud_score (metrics["cloud_cover_avg"])

        total = (temp_score * self.WEIGHTS["temperature"] + wind_score * self.WEIGHTS["wind_speed"] + humidity_score * self.WEIGHTS[
            "humidity"] + cloud_score * self.WEIGHTS["cloud_cover"])
        return total

    def _temp_score (self, temp: float) -> float:
        deviation = abs (temp - 24)
        return max (0, 10 - deviation)

    def _wind_score (self, wind: float) -> float:
        return max(0, 10 - wind)

    def _humidity_score (self, humidity: float) -> float:
        deviation = abs (humidity - 50)
        score = 10 - (deviation / 50) * 10
        return max (0, score)

    def _cloud_score (self, cloud: float) -> float:
        if cloud <= 25:
            return (cloud / 25) *10
        else:
            return 10 - ((cloud - 25) / 75) * 10
