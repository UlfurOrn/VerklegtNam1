from datetime import date
import csv


class Destination:
    def __init__(self,
                 airport="",
                 country="",
                 flightTime=date(1, 1, 1),
                 distance=0,
                 contactId=""):
        self.airport = airport
        self.country = country
        self.flightTime = flightTime
        self.distance = distance
        self.contactId = contactId

    def __str__(self):
        return "Destination: " + ", " + self.airport + ", " + self.country + ", " + str(
            self.flightTime) + ", " + str(
                self.distance) + ", " + self.contactId


class DestinationContainer:
    def __init__(self):
        self._destinations = {}
        with open("../UPDATEDSTUDENTDATA/Destinations.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                newDestination = Destination(row[reader.fieldnames[0]],
                                             row[reader.fieldnames[1]])
                self._destinations[newDestination.airport] = newDestination

    def __str__(self):
        return "".join([
            str(k) + ": " + str(v) + "\n"
            for (k, v) in self._destinations.items()
        ])


print(DestinationContainer())
