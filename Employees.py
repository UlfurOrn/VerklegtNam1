from datetime import datetime



class Employee:
    def __init__(self, name, social, mobile, home_phone, address, email, plane_type, job_type, cid):
        self.name = name
        self.social = social
        self.mobile = mobile
        self.home_phone = home_phone
        self.address = address
        self.email = email
        self.id = cid
        self.plane_type = plane_type
        self.is_pilot = job_type
        self.schedule = [[datetime(2019,10,23,10,30),datetime(2019,10,30,10,30)],[datetime(2019,12,1,10,30),datetime(2019,12,1,2,30)],[datetime(2019,12,3,10,30),datetime(2019,12,3,12,30)]]

    def update_variable(self, value, variable):
        if variable is not "":
            if(variable == "mobile"):
                self.mobile = value
            if(variable == "home phone"):
                self.home_phone = value
            if(variable == "address"):
                self.address = value
            if(variable == "email"):
                self.email = value
            if(variable == "plane"):
                self.plane_type = value

    def employee_info(self):
        return [self.id,self.name,self.social,self.mobile,self.home_phone,self.address,self.email,self.plane_type]

    def __str__(self):
        return "id: "+str(self.id)+"\nname: "+self.name+"\nmobile phone: "+str(self.mobile)+"\nhome phone: "+str(self.home_phone)+"\naddress: "+self.address+"\nemail: "+self.email




class EmployeeContainer:
    def __init__(self, airline):
        self.all = []
        self.attendants = []
        self.pilots = []
        self.airline = airline


    def hire_employee(self, name, social, mobile, home_phone, address, email,plane_type, job_type):
        cemployee = Employee(name, social, mobile, home_phone, address, email, plane_type, job_type, self.airline.id_counter)

        self.airline.assets[self.airline.id_counter] = cemployee
        self.all.append(self.airline.id_counter)
        if job_type:
            self.pilots.append(self.airline.id_counter)
        else:
            self.attendants.append(self.airline.id_counter)
        self.airline.id_counter+=1


    def update_employee(self, cid, updates):
        cemployee = self.airline.assets[cid]
        cemployee.update_variable(updates[0],"mobile")
        cemployee.update_variable(updates[1],"home_phone")
        cemployee.update_variable(updates[2],"address")
        cemployee.update_variable(updates[3],"email")
        cemployee.update_variable(updates[4],"plane")
