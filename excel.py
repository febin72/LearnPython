import csv
with open('Febin.csv') as csv_file:
	read_csv = csv.reader(csv_file, delimiter=',')
	for row in read_csv:
		print (row[1],row[2])
		
		