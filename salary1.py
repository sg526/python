salary=input("Enter Your Salary:")
if int(salary)>=2000:
	tax=int(salary)*20/100
	net=int(salary)-tax
if int(salary)<2000:
	tax=int(salary)*10/100
	net=int(salary)-tax
print("Tax:",tax)
print("Net Salary:",net)