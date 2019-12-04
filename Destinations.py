from datetime import date
import csv


class Destination(dict):
    def nosdf(self):
        pass


class DestinationContainer:
    def __init__(self):
        self._destinations = {}
        self.load_csv()

    def __str__(self):
        return "".join([
            str(k) + ": " + str(v) + "\n"
            for (k, v) in self._destinations.items()
        ])

    def add(self, destination):
        self._destinations["id"] = destination

    def load_csv(self):
        with open("../UPDATEDSTUDENTDATA/Destinations.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.add(Destination(row))


print(DestinationContainer())
