import csv
from Destination import Destination

import csv
from Destination import Destination

class DestinationIO:

    def __init__(self):
        self.destination_list = []
    
    def add_destination(self, destination):
        self.destination_list.append(destination)
        self.save_destinations()

        
    def save_destinations(self):
        with open("VerklegtNam1/CSVFolder/destinations.csv", "w", encoding="utf8") as destination_file:
            csv_writer = csv.writer(destination_file)

            for destination in self.destination_list:
                csv_writer.writerow(destination.get_save_info())

    
    def load_destinations(self):
        if self.destination_list == []:
            
            with open("VerklegtNam1/CSVFolder/destinations.csv", "r", encoding="utf8") as destination_file:
                csv_reader = csv.reader(destination_file)

                for line in csv_reader:
                    country, airport, abrev, flight_time, flight_dist, contact_name, contact_num = line
                    destination = Destination(country, airport, abrev, flight_time, flight_dist, contact_name, contact_num)
                    
                    self.destination_list.append(destination)
        
        return self.destination_list
