class Employee:
    def __init__(self,
                 name="",
                 ssn="",
                 address="",
                 hphone="",
                 wphone="",
                 email="",
                 plane_type="",
                 job_type="",
                 time_table=[]):
        self.name = name
        self.ssn = ssn
        self.ID = ssn
        self.address = address
        self.hphone = hphone
        self.wphone = wphone
        self.email = email
        self.plane_type = plane_type
        self.job_type = job_type
        self.time_table = time_table

    def get_header(self):
        return [
            "Name", "Social Num", "Address", "Home Phone", "Work Phone",
            "Email", "Plane Auth", "Job Title"
        ]

    def get_print_info(self):
        return [
            self.name, self.ssn, self.address, self.hphone, self.wphone,
            self.email, self.plane_type, self.job_type
        ]

    def get_save_info(self):
        return [
            self.name, self.ssn, self.address, self.hphone, self.wphone,
            self.email, self.plane_type, self.job_type, self.time_table
        ]

    def is_pilot(self):
        return self.job_type == "Captain" or self.job_type == "Co Pilot"

    def is_superior(self):
        return self.job_type == "Captain" or self.job_type == "Super Attendant"

    def get_creation_fields(self):
        return [0, 1, 2, 3, 4, 5, 6, 7]

    def get_updatable_fields(self):
        return [2, 3, 4, 5, 6]

    def get_id(self):
        return self.ssn

    def update_info(self, new_info_list):
        name, ssn, address, hphone, wphone, email, plane_type, job_type = new_info_list
        self.name = name
        self.ssn = ssn
        self.address = address
        self.hphone = hphone
        self.wphone = wphone
        self.email = email
        self.plane_type = plane_type
        self.job_type = job_type

    def __str__(self):
        return "{} ({})".format(self.name, self.job_type)
