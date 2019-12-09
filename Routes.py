import csv
from datetime import date, timedelta
from collections import defaultdict
from copy import deepcopy


class Flight(dict):
    def asdofij():
        pass

class Route(dict):
    def repeat_after(self, time=timedelta(0)):
        pass
        # newRoute = deepcopy(self)

        # newRoute.outboundDeparture += t
        # newRoute.returningDeparture += time

    # def is_valid(self):
    #     return self.pilots.len() >= 2 and self.assistants.len(
    #     ) >= 1 and self.headPilot != 0 and self.headAssistant != 0 and self.headPilot in self.pilots and self.headAssistant in self.assistants


class RouteContainer:
    def __init__(self):
        self._flights = {}

    def __str__(self):
        return "".join([str(k) + ": " + str(v) + "\n" for (k,v) in self._flights.items()])

    def load(self):
        self._load_csv()

    def add(self, flight):
        self._flights[flight["flightNumber"]] = flight

    def _load_csv(self):
        with open("../UPDATEDSTUDENTDATA/PastFlights.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.add(Flight(row))
        with open("../UPDATEDSTUDENTDATA/UpcomingFlights.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.add(Flight(row))

    def add_route(self, route):
        route.id = self._routes.len()
        self._routes.append(route)


print(RouteContainer())
