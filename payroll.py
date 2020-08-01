'''
 File Name: payroll.py
 Author's Name: Tamanna Yasmin Jitu
 Student Number: 300924009
 Date: July 31, 2020
 Description: Showing Data into tabular format
'''

from tabulate import tabulate
print (tabulate([],headers=['Employee Number','Employee Name','Hours Worked']))
with open('data.txt') as filestream:
    for line in filestream:
        currentline = line.split(",")
        print(currentline[0]+'\t\t   '+currentline[2] + ' ' + currentline[1] + '\t\t' + currentline[3] )