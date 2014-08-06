def csv_to_dict(filename,delimiter=","):
	'''
	A function that opens a csv file and turns it into a nested list 
	with items in each row as a list within the list of rows.
	'''
	with open(filename,'r') as csvfile:
		rows=csvfile.read().splitlines()

		for index, row in enumerate(rows):
			rows[index]=row.split("delimiter")

		#remove the header so we can iterate over it
		header=rows.pop(0)
		
		#create the nested dictionary that uses row numbers as keys to fake 'order'
		nestdict={}
		#loop over each row in the csv
		for index, row in enumerate(rows):
			#this dict comprehension loops over the pairs created when we zip the header and row lists together
			#and creates a dictionary for that line with the header as the key and row as the value 
			line={key:value for key,value in zip(header,row)}
			#then we add that line to our nested dictionary as a value, with the key being the index (row number)
			nestdict[index]=line

	return nestdict
