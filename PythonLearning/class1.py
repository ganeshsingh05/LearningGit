class Employee:
	def __init__(self, fname, lname, pay):
		self.fname = fname
		self.lname = lname
		self.pay = pay

<<<<<<< HEAD
=======
	def fullname(self):
		return '{}  {}'.format(self.fname, self.lname)
	
	def email(self):
		return '{}.{}@company.com'.format(self.fname,self.lname)
>>>>>>> fc9ba61... email funtion added


