import datetime

class Destinations:
    def __init__():
        self.destinations = []

    def add_destination(country, airport, flight_time, distance, contact_id):
        self.destinations.append(Destination(self.destinations.len(), country, airport, flight_time, distance, contact_id))

class Destination:
    def __init__(id, country, airport, flight_time, distance, contact_id):
        self.id = id
        self.country = country
        self.airport = airport
        self.flight_time = flight_time
        self.distance = distance
        self.contact_id = contact_id

    def __str__():
        return "destination: " + self.country + self.airport + self.flight_time + self.distance + self.contact_id
