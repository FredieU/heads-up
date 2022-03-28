from lca_api import LondonCityAirportAPI
import pprint

if __name__ == '__main__':
    api = LondonCityAirportAPI()
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(api.getArrivals())
    # pp.pprint(api.getDepartures())