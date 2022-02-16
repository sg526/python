salaries=[300,678,897,675,7865,8976,88976,78,900,45,8777,88899,334,321,435,9000000,756,10,12,24352,666,333,22]

i=1
big=salaries[0]
while i<len(salaries):
	if salaries[i]>big:
		big=salaries[i]
	i=i+1
print("Highest number is:",big)