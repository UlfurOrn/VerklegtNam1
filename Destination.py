class Destination(dict):
	def get_summary(self):
		return str(self["country"])+" ("+str(self["airport"])+")"

	def get_header(self):
		return ["Country" ,"Airport", "Abreviation", "Time", "Distance", "Contact Name", "Contact Num"]

	def get_keys(self):
		return ["country" ,"airport", "abrev", "flight_time", "flight_dist", "contact_name", "contact_num"]