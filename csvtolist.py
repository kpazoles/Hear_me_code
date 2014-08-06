def csv_to_list(filename,delimiter=","):

"""
A function that opens a csv file and turns it into a nested list 
with items in each row as a list within the list of rows.
"""
	with open(filename,'r') as csvfile:
		newlist=csvfile.read().splitlines()

		for index,line in enumerate(newlist):
			newlist[index]=line.split("delimiter")

 	return newlist
