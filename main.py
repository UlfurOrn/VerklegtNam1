from Employees import *
from Destinations import *
from Routes import *
from datetime import datetime


class Airline:
	def __init__(self):
		self.employees = EmployeeContainer(self)
		self.assets = {}
		self.id_counter = 1

	def asset_occupied_day(self,cid,day):
		return self.asset_occupied_time_period(cid,[day,day])


	def asset_occupied_time_period(self,cid,time):
		cschedule = self.assets[cid].schedule
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



cair = Airline()

cair.employees.hire_employee("siggi","251135","652584","22325","spain-drive 21","siggi@sigg.is","boeing 747",False)


print(cair.asset_occupied_day(1,datetime(2019,10,23,10,30)))


for i in cair.employees.all:
    print(cair.assets[i])
print()
cair.employees.update_employee(1,["","","spain-drive 23","",""])

for i in cair.employees.all:
    print(cair.assets[i])
