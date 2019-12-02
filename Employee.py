class Employee:
    def __init__(self, name,mobile,home_phone, address, email,job_type, cid):
        self.name = name
        self.mobile = mobile
        self.home_phone = home_phone
        self.address = address
        self.email = email
        self.id = cid
        self.is_pilot = job_type


    def __str__(self):
        return "id: "+str(self.id)+"\nname: "+self.name+"\nmobile phone: "+str(self.mobile)+"\nhome phone: "+str(self.home_phone)+"\nadress: "+self.address+"\nemail: "+self.email
