class Employee:
    def __init__(self, name, social, mobile, home_phone, address, email, job_type, cid):
        self.name = name
        self.social = social
        self.mobile = mobile
        self.home_phone = home_phone
        self.address = address
        self.email = email
        self.id = cid
        self.is_pilot = job_type

    def update_variable(self,value,variable):
        if variable is not "":
            if(variable == "mobile"):
                self.mobile = value
            if(variable == "home phone"):
                self.home_phone = value
            if(variable == "address"):
                self.address = value
            if(variable == "email"):
                self.email = value
        

    def __str__(self):
        return "id: "+str(self.id)+"\nname: "+self.name+"\nmobile phone: "+str(self.mobile)+"\nhome phone: "+str(self.home_phone)+"\naddress: "+self.address+"\nemail: "+self.email




class EmployeeContainer:
    def __init__(self, airway):
        self.all = []
        self.attendants = []
        self.pilots = []
        self.airway = airway
    def hire_employee(self,name,social,mobile,home_phone, address, email,job_type):
        cemployee = Employee(name,social,mobile,home_phone,address,email,job_type,self.airway.id_counter)

        self.airway.assets[self.airway.id_counter] = cemployee
        self.all.append(self.airway.id_counter)
        if job_type:
            self.pilots.append(self.airway.id_counter)
        else:
            self.attendants.append(self.airway.id_counter)
        self.airway.id_counter+=1


    def update_employee(self,cid,updates):
        cemployee = self.airway.assets[cid]
        cemployee.update_variable(updates[0],"mobile")
        cemployee.update_variable(updates[1],"home_phone")
        cemployee.update_variable(updates[2],"address")
        cemployee.update_variable(updates[3],"email")

