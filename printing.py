def printing(msg):
	word=""
	i=0
	while i<len(msg):
		if msg[i]==" ":
			print(word)
			word=""
		else:
			word=word+msg[i]
		i=i+1
	print(word)

printing("it is a wonderful life")
print("-------------------------")
printing("Willy Wonka and the Chocolate Factory")
print("-------------------------")
printing("Puppy Power")