from datetime import datetime, date
import pandas as pd

def getDateParams():
    now = datetime.now()

    return {
        'day': now.day,
        'month': now.month,
        'year': now.year
    }

def getByStatus(flights, status):
    flights_with_status = {}
    for flight in flights:
        if flight['flightAction']['status'] == status:
            flights_with_status.update(flight)

    return flights_with_status

def formatData(data):
    arrival_airport = []
    departure_airport = []
    flight_status = []
    flight_number = []
    actual_time = []
    scheduled_time = []

    for flight in data:
        arrival_airport.append(flight['arrivalAirport']['code'])
        departure_airport.append(flight['departureAirport']['code'])
        flight_status.append(flight['flightAction']['status'])
        flight_number.append(flight['flightNumber'])
        scheduled_time.append(datetime.fromisoformat(flight['flightTimeInformation']['scheduledTime']['time']))

        if flight['flightTimeInformation']['actualTime'] is not None:
            actual_time.append(datetime.fromisoformat(flight['flightTimeInformation']['actualTime']['time']))
        else:
            actual_time.append(None)

    flight_dict = {
        'flight_number': flight_number,
        'arrival_airport': arrival_airport,
        'departure_airport': departure_airport,
        'flight_status': flight_status,
        'actual_time': actual_time,
        'scheduled_time': scheduled_time,
    }

    return pd.DataFrame(flight_dict, columns=flight_dict.keys())

if __name__ == '__main__':
    pass