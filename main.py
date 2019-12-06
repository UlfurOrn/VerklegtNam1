from Data import DataInterface
from Employees import *
from Destinations import *
from Routes import *
from UserInterface import *
from datetime import datetime, timedelta


class Airline:
	def __init__(self):
		self.data = DataInterface()
		self.employees = EmployeeContainer()
		#self.data_collection = DataLayer()
		self.UI = UserInterface(self)
		self.id_counter = 1

	def entity_occupied_day(self,entity,day):
		return self.data_occupied_time_period(current_id,[day,day])

	def entity_occupied_time_period(self,entity,time):
		cschedule = self.data_collection.get_schedule(entity)
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

	def get_occupied_employees_by_day(self,day):
		employees = self.employees.get_all()
		return_array = []
		for employee in employees:
			if(self.entity_occupied_day(day)):
				return_array.append(employee)
		return return_array

	def get_all(self):
		return self.employees.get_all()

	def get_pilots(self):
		return self.employees.get_pilots()

   	def get_attendants(self):
   		return self.employees.get_attendants()

	def get_employee_by_id(self,current_id):
		return self.employees.get_by_id(current_id)

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

cair.UI.main_menu()

