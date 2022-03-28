from datetime import datetime

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
