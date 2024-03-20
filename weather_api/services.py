from typing import Optional

import requests
from django.conf import settings


def get_geolocation(city_name: str) -> tuple[Optional[str], Optional[str]]:
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={settings.OPENWEATHERMAP_API_KEY}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        lat, lon = data[0].get('lat'), data[0].get('lon')
        return lat, lon
    else:
        return None, None