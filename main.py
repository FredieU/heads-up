from lca_api import LondonCityAirportAPI
from utils import formatData
import pprint

if __name__ == '__main__':
    api = LondonCityAirportAPI()
    pp = pprint.PrettyPrinter(indent=2)
    # data = api.getArrivals()
    data = api.getDepartures()
    print(formatData(data))