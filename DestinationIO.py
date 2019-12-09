import csv
from Destination import Destination

class DestinationIO:

    def __init__(self):
        self.destination_list = []
    

    def add_destination(self, destination):
        self.destination_list.append(destination)
        self.save_destinations()

        
    def save_destinations(self):
        with open("VerklegtNam1/CSVFolder/destinations.csv", "w") as destination_file:
            fieldnames = ["country" ,"airport", "abrev", "flight_time", "flight_dist", "contact_name", "contact_num"]
            
            csv_writer = csv.DictWriter(destination_file, fieldnames=fieldnames)
            csv_writer.writeheader()

            for destination in self.destination_list:
                csv_writer.writerow(destination.info_dict)

    
    def load_destinations(self):
        if self.destination_list == []:
            
            with open("VerklegtNam1/CSVFolder/destinations.csv", "r") as destination_file:
                csv_reader = csv.DictReader(destination_file)

                for info_dict in csv_reader:
                    destination = Destination(dict(info_dict))
                    
                    self.destination_list.append(destination)
        
        return self.destination_list
