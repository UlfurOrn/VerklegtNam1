class LogicLayer:

	def get_page(self,asset_list,current_page,page_delimiter = 9):
		return_value = asset_list[(current_page -1)*page_delimiter:current_page*page_delimiter]
		return_value+= [""]*(page_delimiter-len(return_value))
		return return_value

	def total_pages(self, asset_list, page_delimiter = 9):
		num_pages = len(asset_list) // page_delimiter
		if num_pages % page_delimiter != 0:
			num_pages += 1
		if num_pages == 0:
			num_pages += 1
		return num_pages


	def get_all(self):
		return self.IO.get_all()

	def add(self, asset):
		self.IO.add(asset)
		self.save()

	def save(self):
		self.IO.save()

	def load(self):
		self.IO.load()
