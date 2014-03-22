with open("states.txt", "r") as states_file:
	states=states_file.read().split("\n")

	print "<select name='States'>"

	for index,state in enumerate(states):
		states[index]=state.split("\t")

	for state in states:
		print "\t <option value='{0}'>{1}</option>".format(state[0], state[1])

print "</select>"
