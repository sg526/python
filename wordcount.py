def wordcount(msg):
	space=0
	i=0
	while i<len(msg):
		if msg[i] == " ":
			space=space+1
		i=i+1
	print("In the message we found: ",space+1)

wordcount("I need to call the hairdresser later as I have a clash")
