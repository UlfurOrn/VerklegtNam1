import csv
from datetime import date, timedelta
from collections import defaultdict
from copy import deepcopy


class Flight:
    def __init__(self,
                 flightNumber="",
                 departingFrom="",
                 arrivingAt="",
                 departure=date(1, 1, 1),
                 arrival=date(1, 1, 1),
                 aircraftID="",
                 captain=0,
                 pilots=[],
                 headAssistant=0,
                 assistants=[]):
        self.flightNumber = flightNumber
        self.departingFrom = departingFrom
        self.arrivingAt = arrivingAt
        self.departure = departure
        self.arrival = arrival
        self.aircraftID = aircraftID
        self.captain = captain
        self.pilots = pilots
        self.headAssistant = headAssistant
        self.assistants = assistants

    def __str__(self):
        return "Flight: " + str(self.flightNumber) + ", " + str(
            self.departingFrom) + ", " + str(self.arrivingAt) + ", " + str(
                self.departure) + ", " + str(self.arrival) + ", " + str(
                    self.aircraftID) + ", " + str(self.captain) + ", " + str(
                        self.pilots) + ", " + str(
                            self.headAssistant) + ", " + str(self.assistants)

    def __repr__(self):
        return self.__str__()


class Route:
    def __init__(self,
                 destinationId=0,
                 flightNumber="",
                 outboundDeparture=date(1, 1, 1),
                 returningDeparture=date(1, 1, 1),
                 employees=[],
                 pilots=[],
                 headPilot=0,
                 assistants=[],
                 headAssistant=[]):
        self.destinationId = destinationId
        self.outboundDeparture = outb
        self.returningDeparture = returningDeparture
        self.employees = employees
        self.pilots = pilots
        self.headPilot = headPilot
        self.assistants = assistants
        self.headAssistant = headAssistant

    def repeat_after(self, time=timedelta(0)):
        newRoute = deepcopy(self)

        newRoute.outboundDeparture += t
        newRoute.returningDeparture += time

    def is_valid(self):
        return self.pilots.len() >= 2 and self.assistants.len(
        ) >= 1 and self.headPilot != 0 and self.headAssistant != 0 and self.headPilot in self.pilots and self.headAssistant in self.assistants


class Routes:
    def __init__(self):
        self._flights = {}
        with open("../STUDENTDATA/PastFlights.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                newFlight = Flight(
                    *[row[reader.fieldnames[i]]
                      for i in range(6)], row["captain"], [row["copilot"]],
                    row["fsm"], [row["fa1"], row["fa2"]]
                )  # including the captain in the pilots list might be better, same for assistants

                self._flights[newFlight.flightNumber] = newFlight
        with open("../STUDENTDATA/UpcomingFlights.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                newFlight = Flight(
                    *[row[reader.fieldnames[i]] for i in range(5)])

                self._flights[newFlight.flightNumber] = newFlight
        print(self._flights)

    def add_route(self, route):
        route.id = self._routes.len()
        self._routes.append(route)


Routes()
