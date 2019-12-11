import csv
from Destination import Destination


class DestinationIO:
    def __init__(self):
        self.destinations = {}

    def get_all(self):
        return self.load()

    def add(self, destination):
        self.destinations[destination.abrev] = destination

    def save(self):
        with open("CSVFolder/destinations.csv", "w",
                  encoding="utf8") as destination_file:
            csv_writer = csv.writer(destination_file)

            for destination in self.destination_list:
                csv_writer.writerow(destination.get_save_info())

    def load(self):
        if self.destinations == {}:

            with open("CSVFolder/destinations.csv", "r",
                      encoding="utf8") as destination_file:
                csv_reader = csv.reader(destination_file)

                for line in csv_reader:
                    country, airport, abrev, flight_time, flight_dist, contact_name, contact_num = line
                    destination = Destination(country, airport, abrev,
                                              flight_time, flight_dist,
                                              contact_name, contact_num)

                    self.add(destination)

        return list(self.destinations.values())
