with open("file.txt", "a+") as file:
	content = file.write("Even more sample text")
	file.seek(0)
	file.read()