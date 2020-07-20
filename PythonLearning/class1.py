class Employee:
	def __init__(self, fname, lname, pay):
		self.fname = fname
		self.lname = lname
		self.pay = pay

	def fullname(self):
		return '{}  {}'.format(self.fname, self.lname)



