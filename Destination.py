class Destination:

    def __init__(self, info_dict={"country": "", "airport": "", "abrev": "", "flight_time": "", "flight_dist": "", "contact_name": "", "contact_num": ""}):
        self.info_dict = info_dict


    def get_header(self):
        return ["Country" ,"Airport", "Abreviation", "Time", "Distance", "Contact Name", "Contact Num"]


    def get_keys(self):
        return ["country" ,"airport", "abrev", "flight_time", "flight_dist", "contact_name", "contact_num"]


    def get_summary(self):
        return "{} ({})".format(self.info_dict["country"], self.info_dict["airport"])
