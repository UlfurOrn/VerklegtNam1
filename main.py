from Employees import *
from Destinations import *
from Routes import *
from DataLayer import *
from datetime import datetime, timedelta


class Airline:
	def __init__(self):
		self.employees = EmployeeContainer(self)
		self.data_collection = DataLayer()
		self.id_counter = 1

	def data_occupied_day(self,entity,day):
		return self.data_occupied_time_period(current_id,[day,day])


	def data_occupied_time_period(self,entity,time):
		cschedule = self.data_collection.get_schedule()
		if cschedule[0][0] > time[1]:
			return False
		if(cschedule[-1][1] < time[0]):
			return False
		for i in range(len(cschedule)):
			if cschedule[i+1][0] > time[1]:
				if cschedule[i][1] < time[0]:
					return False
				else:
   					return True

   	def get_pilots(self):
   		return self.employees.get_pilots()

   	def get_data_by_Week(self,data):
   		return self.data_collection[data]

   	def get_week_schedule(self,entity,current_week):
   		weekwork = []
   		voyage = self.routes.get_voyages(entity)
   		for i in employee.schedule():
   			if(current_week > voyage[i].outboundDeparture and current_week+timedelta(week=1) < voyage[i].outboundDeparture):
   				weekwork.append(voyage)

   		return weekwork



cair = Airline()

cair.employees.hire_employee("siggi","251135","652584","22325","spain-drive 21","siggi@sigg.is","boeing 747",False)


print(cair.data_occupied_day(1,datetime(2019,10,23,10,30)))


for i in cair.employees.all:
    print(cair.data_collection[i])
print()
cair.employees.update_employee(1,["","","spain-drive 23","",""])

for i in cair.employees.all:
    print(cair.data_collection[i])
