Source = input(" Source : ")
Destination = input(" Destination : ")
with open(Source) as file1:
	with open(Destination, "w") as file2:
		for line in file1:
			file2.write(line)