nums=[]
print("Enter 0 to Terminate")
while True:
	no=int(input("Enter any number: "))
	if no==0:
		break
	nums.append(no)
print("You have Entered",len(nums),"Values")