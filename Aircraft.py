import csv
from copy import copy
from collections import defaultdict


class Aircraft(dict):
    def sadflkjasdf(self):
        pass


class AircraftType(dict):
    def asdlfkj(self):
        pass


class AircraftContainer:
    def __init__(self):
        self._aircraft = {}
        self._typeIds = defaultdict(set)
        self._aircraftTypes = {}
        self.load_csv()

    def __str__(self):
        return "Aircraft: " + "".join([
            str(k) + ": " + str(v) + "\n"
            for (k, v) in self._aircraft.items()
        ]) + "Type ids: " + "".join([
            str(k) + ": " + str(v) + "\n"
            for (k, v) in self._typeIds.items()
        ]) + "Aircraft Types: " + "".join([
            str(k) + ": " + str(v) + "\n"
            for (k, v) in self._aircraftTypes.items()
        ])

    def add_aircraft(self, aircraft):
        self._aircraft[aircraft["planeInsignia"]] = aircraft
        self._typeIds[aircraft["planeTypeId"]].add(aircraft["planeInsignia"])

    def add_types(self, aircraftType):
        self._aircraftTypes[aircraftType["planeTypeId"]] = aircraftType

    def load_csv(self):
        with open("../UPDATEDSTUDENTDATA/Aircraft.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.add_aircraft(Aircraft(row))

        with open("../UPDATEDSTUDENTDATA/AircraftType.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.add_types(AircraftType(row))


print(AircraftContainer())
