def textfile_to_list(filename,delimiter="\n"):
	with open(filename,'r') as textfile:
		newlist=textfile.read().split(delimiter)
 	return newlist

def deduplicate(my_list):
	my_list=list(set(my_list))
	return my_list

def find_duplicates(list_1, list_2):
	duplicates=[]
	master_list=list(set(list_1+list_2))
	for item in master_list:
		if item in(list_1) and item in(list_2):
			duplicates.append(item)
 	return duplicates


screening=textfile_to_list('screening_attendees.txt')
happy_hour=textfile_to_list('HH_attendees.txt')

all_attendees=screening+happy_hour

all_attendees=deduplicate(all_attendees)
super_attendees=find_duplicates(screening, happy_hour)

print "{0} total attendees: ".format(len(all_attendees)), all_attendees

print "{0} people attended both events: ".format(len(super_attendees)), super_attendees
