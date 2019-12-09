"""class Employee:

    def __init__(self, info_dict={"name": "", "ssn": "", "address": "", "home_phone": "", "work_phone": "", "email": "", "plane_type": "", "job_type": "", "time_table": ""}):
        self.info_dict = info_dict


    def get_header(self):
        return ["Name", "Social Num", "Address", "Home Phone", "Work Phone", "Email", "Plane Auth", "Job Title"]


    def get_keys(self):
        return ["name" ,"ssn", "address", "home_phone", "work_phone", "email", "plane_type", "job_type"]


    def get_summary(self):
        return "{} ({})".format(self.info_dict["name"], self.get_job())

    def get_job(self):
        return self.info_dict["job_type"]
"""

class Employee(dict):
    def is_pilot(self):
        return self["job_type"] == "Co Pilot" or self["job_type"] == "Captain"

    def get_summary(self):
        return self["name"]+" ("+self["job_type"]+")"

    def get_header(self):
        return ["Name", "Social Num", "Address", "Home Phone", "Work Phone", "Email", "Plane Auth", "Job Title"]


    def get_keys(self):
        return ["name" ,"ssn", "address", "home_phone", "work_phone", "email", "plane_type", "job_type"]