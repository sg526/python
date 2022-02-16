bill=int(input("Enter your bill:"))
paid=int(input("Enter Amount Paid:"))
balance=paid-bill
print("Your balance is:",balance)
if balance>=50:
	fifty=int(balance/50)
	print("Fifty Pounds:",fifty)
	balance=balance-(fifty*50)
if balance>=20:
	twenty=int(balance/20)
	print("Twenty Pounds:",twenty)
	balance=balance-(twenty*20)
if balance>=10:
	print("Ten Pounds:1")
	balance=balance-10
if balance>=5:
	print("Five Pounds:1")
	balance=balance-5
if balance>=1:
	one=int(balance/1)
	print("One Pound:",one)
	balance=balance-(one*1)