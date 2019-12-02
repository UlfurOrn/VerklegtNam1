class airway:
    def __init__(self):
        self.employees = []
        self.attendants = []
        self.pilots = [] 
        self.assets = {}
        self.id_counter = 1

    def hire_employee(self,name,mobile,home_phone, address, email,job_type):
        cemployee = employee(name,mobile,home_phone,address,email,job_type,self.id_counter)
        
        self.assets[self.id_counter] = cemployee
        self.employees.append(self.id_counter)
        if job_type:
            self.pilots.append(self.id_counter)
        else:
            self.attendants.append(self.id_counter)
        self.id_counter+=1

        
            
        
        
class employee:
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



cair = airway()

cair.hire_employee("siggi",52584,22325,"spain-drive 21","siggi@sigg.is",False)



for i in cair.employees:
    print(cair.assets[i])
