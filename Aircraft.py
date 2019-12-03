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
    def __init__(self, planeTypeId, planeType, model, capacity, emptyWeight,
                 maxTakeoffWeight, unitThrust, serviceCeiling, length, height,
                 wingspan):
        self.planeTypeId = planeTypeId
        self.planeType = planeType
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
        return self.planeTypeId + ", " + self.planeType + ", " + self.model + ", " + str(self.capacity) + ", " + str(self.emptyWeight) + ", " + str(self.maxTakeoffWeight) + ", " + str(self.unitThrust) + ", " + str(self.serviceCeiling) + ", " + str(self.length) + ", " + str(self.height) + ", " + str(self.wingspan)

    def __repr__(self):
        return self.__str__()
class AircraftContainer:
    def __init__(self):
        with open("../STUDENTDATA/Aircraft.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            self._aircraft = {}
            self._insignia = {}
            self._typeIds = defaultdict(set)

            for row in reader:
                newAircraft = Aircraft(row[reader.fieldnames[0]],
                                       row[reader.fieldnames[1]])

                self._aircraft[id(newAircraft)] = newAircraft
                self._insignia[newAircraft.insignia] = id(newAircraft)
                self._typeIds[newAircraft.typeId].add(id(newAircraft))
        with open("../STUDENTDATA/AircraftType.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            self._aircraftTypes = {}

            for row in reader:
                print("the row is: " + str(row))
                newAircraftType = AircraftType(*[row[reader.fieldnames[i]] for i in range(11)])
                self._aircraftTypes[row[reader.fieldnames[0]]] = newAircraftType
            print(self._aircraftTypes)





AircraftContainer()
