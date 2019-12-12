from DataLayer.IO import IO
from LogicLayer import LogicLayer

class VoyageLL(LogicLayer):

    def __init__(self):
        self.IO = IO()

    def get_voyage_info(self, voyage):
        return_value = str(voyage)
        destination = IO.get_destination_by_id(voyage.destination)
        airplane = IO.get_airplane_by_id(voyage.airplane)
        return_value+= "destination: "+destination.country+"\n"
        return return_value

    def get_employees_in_voyage(self, voyage):
        return_array = []
        for i in voyage.pilots:
            return_array.append(self.IO.get_employee_by_id(i))
        for i in voyage.attendants:
    	    return_array.append(self.IO.get_employee_by_id(i))
        return return_array

    def add_employee_to_voyage(self, voyage, employee):
    	employee.time_table.append(voyage.id)
    	if employee.job_type == "Captain":
    		voyage.pilots[0] = employee
    	elif employee.job_type == "Co Pilots":
    		voyage.pilots[1] = employee
    	elif employee.job_type == "Super Attendant":
    		voyage.attendants[0] = employee
    	elif employee.job_type == "attendant":
    		voyage.attendants.append(employee)

    def add_airplane_to_voyage(self, voyage, airplane):
    	airplane.time_table.append(voyage.id)
    	voyage.airplane = airplane.id

    def get_all(self):
    	return self.IO.get_voyages()	
