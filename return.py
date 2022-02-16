def tax(salary):
	T=salary*20/100
	return T

salary=int(input("Please enter your salary: "))
net = salary-tax(salary)

print("Tax:",tax(salary))
print("Net:",net)