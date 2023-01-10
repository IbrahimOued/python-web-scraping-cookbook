""" Defines the interface for writing a blob of data to storage """


class IBlobWriter():
	def write(self, filename, contents):
		pass 