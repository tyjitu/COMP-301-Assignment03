'''
 File Name: copyfile.py
 Author's Name: Tamanna Yasmin Jitu
 Student Number: 300924009
 Date: July 31, 2020
 Description: Copy one file content to another file
'''

Source = input(" Source : ")
Destination = input(" Destination : ")
with open(Source) as file1:
	with open(Destination, "w") as file2:
		for line in file1:
			file2.write(line)
