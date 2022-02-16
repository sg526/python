nums=[]
choice ="Y"
while choice =="Y" or choice=="y":
	no=int(input("Enter any number: "))
	nums.append(no)
	choice=input("....Do you want to add another number? (y/n): ")
print("You have Entered",len(nums),"Values")