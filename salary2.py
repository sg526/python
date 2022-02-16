def salaryslip(name, salary):
	if salary>=2000:
		tax=salary*20/100
	else:
		tax=salary*15/100
	net=salary-tax
	print("Name of Employee: ",name)
	print("Salary: ", salary)
	print("Tax: ", tax)
	print("Net Salary: ", net)

salaryslip("Sophie", 2000)
salaryslip("Simon",1500)
salaryslip("Natalie",2450)