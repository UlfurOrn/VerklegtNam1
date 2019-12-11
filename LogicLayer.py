class LogicLayer:

	def get_all(self):
		return self.IO.get_all()

	def add(self, asset):
		self.IO.add(asset)

	def save(self):
		self.IO.save()

	def load(self):
		self.IO.load()