import csv
from copy import copy
from collections import defaultdict


class Aircraft:
    def __init__(self, insignia="", typeId=""):
        self.insignia = insignia
        self.typeId = typeId

    def __str__(self):
        return self.insignia + ", " + self.typeId

    def __repr__(self):
        return self.__str__()

class AircraftType:
    def __init__(self, planeTypeId, manufacturer, model, capacity, emptyWeight,
                 maxTakeoffWeight, unitThrust, serviceCeiling, length, height,
                 wingspan):
        self.planeTypeId = planeTypeId
        self.manufacturer = manufacturer
        self.model = model
        self.capacity = int(capacity)
        self.emptyWeight = float(emptyWeight)
        self.maxTakeoffWeight = float(maxTakeoffWeight)
        self.unitThrust = float(unitThrust)
        self.serviceCeiling = float(serviceCeiling)
        self.length = float(length)
        self.height = float(height)
        self.wingspan = float(wingspan)

    def __str__(self):
        return self.planeTypeId + ", " + self.manufacturer + ", " + self.model + ", " + str(self.capacity) + ", " + str(self.emptyWeight) + ", " + str(self.maxTakeoffWeight) + ", " + str(self.unitThrust) + ", " + str(self.serviceCeiling) + ", " + str(self.length) + ", " + str(self.height) + ", " + str(self.wingspan)

    def __repr__(self):
        return self.__str__()

class AircraftContainer:
    def __init__(self):
        with open("../UPDATEDSTUDENTDATA/Aircraft.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            self._aircraft = {}
            self._typeIds = defaultdict(set)
            for row in reader:
                newAircraft = Aircraft(row[reader.fieldnames[0]],
                                       row[reader.fieldnames[1]])
                self._aircraft[newAircraft.insignia] = newAircraft
                self._typeIds[newAircraft.typeId].add(newAircraft.insignia)

        with open("../UPDATEDSTUDENTDATA/AircraftType.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            self._aircraftTypes = {}
            for row in reader:
                newAircraftType = AircraftType(*[row[reader.fieldnames[i]] for i in range(11)])
                self._aircraftTypes[row[reader.fieldnames[0]]] = newAircraftType

    def __str__(self):
        return "".join([str(k) + ": " + str(v) + "\n" for (k, v) in self._aircraft.items()])

print( AircraftContainer() )
