# Weather Scoring API

FastAPI application that retrieves weather data for European cities and ranks them based on a weighted scoring algorithm.

## Tech Stack

- **Python 3.11** + **FastAPI**
- **Open-Meteo API** (historical weather data)
- **Docker** + **Docker Compose**
- **uv** (dependency management)

## Quick Start

### With Docker:
```bash
docker-compose up --build
```

### Without Docker:
```bash
uv sync
uv run uvicorn app.main:app --reload
```

API: `http://localhost:8000/docs`

## API Endpoints

### `GET /api/v1/cities-scores`

Returns ranked cities by weather score for specified date range.

**Query Parameters:**
- `start_date` (optional): Start date (YYYY-MM-DD), defaults to yesterday
- `end_date` (optional): End date (YYYY-MM-DD), defaults to yesterday

**Example:**
```bash
GET /api/v1/cities-scores?start_date=2024-05-01&end_date=2024-05-01
```

**Response:**
```json
{
  "start_date": "2024-05-01",
  "end_date": "2024-05-01",
  "cities": [
    {
      "city": "Krakow",
      "temperature_avg": 22.5,
      "wind_speed_avg": 4.2,
      "humidity_avg": 48.3,
      "cloud_cover_avg": 30.1,
      "total_score": 8.5
    }
  ]
}
```

## Scoring Algorithm

**Optimal conditions:**
- Temperature: 24°C (10 points, -1 per degree deviation)
- Wind Speed: 0 m/s (10 points, linear decrease)
- Humidity: 50% (10 points, 0 at 0%/100%)
- Cloud Cover: 25% (10 points, 0 at 0%/100%)

**Weights:**
- Temperature: 35%
- Wind Speed: 20%
- Humidity: 20%
- Cloud Cover: 25%
