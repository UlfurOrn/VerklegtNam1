import csv
import json
from ModelFolder.Voyage import Voyage


class VoyageIO:
    def __init__(self):
        self.voyages = {}
        self.load()

    def get_by_id(self, item_id):
        return self.voyages[item_id]

    def get_all(self):
        return self.load()

    def add(self, voyage):
        self.voyages[voyage.get_id()] = voyage

    def save(self):
        with open("Data/voyages.json", "w") as voyage_file:
            voyage_file.write(
                json.dumps(
                    [voy.get_save_info() for voy in self.voyages.values()]))

    def load(self):
        if self.voyages == {}:
            with open("Data/voyages.json", "r") as voyage_file:
                for line in json.loads(voyage_file.read()):
                    destination, departure_time, arrival_time, airplane, pilot_list, attendant_list, seats_sold = line
                    voyage = Voyage(destination, departure_time, arrival_time,
                                    airplane, pilot_list, attendant_list,
                                    seats_sold)
                    self.add(voyage)

        return list(self.voyages.values())
