import csv
from Destination import Destination

class DestinationIO:
    """
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
                csv_writer.writerow(dict(destination))

    
    def load_destinations(self):
        if self.destination_list == []:
            
            with open("VerklegtNam1/CSVFolder/destinations.csv", "r") as destination_file:
                csv_reader = csv.DictReader(destination_file)

                for info_dict in csv_reader:
                    destination = Destination(dict(info_dict))
                    
                    self.destination_list.append(destination)
        
        return self.destination_list
    """
    def __init__(self):
        self._destinations = {}
        self._load_csv()

    def __str__(self):
        return "".join([
            str(k) + ": " + str(v) + "\n"
            for (k, v) in self._destinations.items()
        ])

    def save_destinations(self):
        with open("VerklegtNam1/CSVFolder/destinations.csv", "w") as destination_file:
            fieldnames = ["country" ,"airport", "abrev", "flight_time", "flight_dist", "contact_name", "contact_num"]
            
            csv_writer = csv.DictWriter(destination_file, fieldnames=fieldnames)
            csv_writer.writeheader()

            for destination in self.destination_list:
                csv_writer.writerow(dict(destination))

    def load(self):
        self._load_csv()

    def add(self, destination):
        self._destinations[destination["abrev"]] = destination

    def get_all(self):
        return list(self._destinations.values())

    def _load_csv(self):
        with open("CSVFolder/destinations.csv", "r", encoding="utf8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.add(Destination(dict(row)))
