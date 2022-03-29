import requests
import json
from urllib.parse import urlencode
from utils import getByStatus, getDateParams

class LondonCityAirportAPI:
    def __init__(self):
        self.base_url = 'https://wifi.londoncityairport.com/api'

    def getUrl(self, direction):
        params = {
            **getDateParams(),
            'direction': direction,
            'page': 0
        }
        query_str = urlencode(params)

        return f'{self.base_url}/flight/status/day?{query_str}'

    def getFlights(self, direction, status=None):
        res = requests.get(url=self.getUrl(direction=direction))
        flights = res.json()['flights']

        if status is not None:
            return getByStatus(flights, status)

        return flights
    
    def getArrivals(self, status=None):
        return self.getFlights(direction='arrival', status=status)

    def getDepartures(self, status=None):
        return self.getFlights(direction='departure', status=status)

