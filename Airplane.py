class Airplane:

    def __init__(self, info_dict={"name": "", "manufacturer": "", "plane_type": "", "seat_cap": "", "time_table": ""}):
        self.info_dict = info_dict


    def get_header(self):
        return ["Name" ,"Manufacturer", "Plane Type", "Seat Capacity"]


    def get_keys(self):
        return ["name" ,"manufacturer", "plane_type", "seat_cap"]


    def get_summary(self):
        return "{} {} ({})".format(self.info_dict["manufacturer"], self.info_dict["plane_type"], self.info_dict["seat_cap"])
