import csv
from Voyage import Voyage


class VoyageIO:
    def __init__(self):
        self.voyages = []
        self.load()

    def get_by_id(self, item_id):
        return self.voyages[item_id]

    def get_all(self):
        return self.load()

    def add(self, voyage):
        self.voyages.append(voyage)

        self.save()

    def save(self):
        with open("CSVFolder/voyages.csv", "w",
                  encoding="utf8") as voyage_file:
            csv_writer = csv.writer(voyage_file)

            for voyage in list(self.voyages.values()):
                csv_writer.writerow(voyage.get_save_info())

    def load(self):
        if self.voyages == {}:

            with open("CSVFolder/voyages.csv", "r",
                      encoding="utf8") as voyage_file:
                csv_reader = csv.reader(voyage_file)

                for line in csv_reader:
                    destination, departure_time, arrival_time, airplane, pilot_list, attendant_list, seats_sold = line
                    voyage = Voyage(destination, departure_time, arrival_time, airplane, pilot_list, attendant_list, seats_sold)

                    self.add(voyage)

        return self.voyages
