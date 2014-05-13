#imports the requests package
import requests

#ask the user what movie title they're looking for
title=raw_input("What movie title or IMDb id do you want to search for? ")

#checks to see if the input is all numbers, and thus the imdb id
if title.isdigit():
	urlb="http://bechdeltest.com/api/v1/getMovieByImdbId?imdbid="+title
	urlomd="http://www.omdbapi.com/?i=tt"+title
	#looks up the api and returns the json for that movie title
	responseb=[requests.get(urlb).json()]
	responseomd=[requests.get(urlomd).json()]

#appends the title to the api request
else:
	if "the" in title[0:4].lower():
		title=title[4:]
		#looks up the api and returns the json for that movie title
		urlb="http://bechdeltest.com/api/v1/getMoviesByTitle?title="+title
		responseb=requests.get(urlb).json()
	else:
		#looks up the api and returns the json for that movie title
		urlb="http://bechdeltest.com/api/v1/getMoviesByTitle?title="+title
		responseb=requests.get(urlb).json()
	#searches the open movie database for matching titles, returns a dict. of search results
	urlomd="http://www.omdbapi.com/?s="+title
	responseomd=[requests.get(urlomd).json()]


#checks to see if the response is empty ie. the movie is not found in the api
bmissing=0
omissing=0
if not responseb:
	print "Movie not found in Bechdel Test!"
	bmissing=1
#then checks to see if status is 404 (not found)	
elif '404' in responseb[0].get('status', 'x'):
	print "Movie not found in Bechdel Test!"
	bmissing=1
#then checks to see if status is 403 (not yet approved)
elif '403' in responseb[0].get('status','x'):
	print "Movie not yet approved"
	bmissing=1
#checks to see if the movie is found in the open movie database 	
if responseomd[0].get('Response')=='False':
	print "Movie not found in Open Movie Database!"
	omissing=1
#as long as there are results from both databases
if bmissing==0 and omissing==0:
#checks to see if any of the search results from open movie database match those from the Bechdel database
#if so, prints out the information about that movie.
	for movie1 in responseb:
		for movie2 in responseomd[0].get('Search',[]):
			if "tt"+movie1['imdbid']==movie2['imdbID']:
				imdbid=movie2['imdbID']
				urlomd2="http://www.omdbapi.com/?i="+imdbid
				responseomd2=[requests.get(urlomd2).json()]
				#print responseomd2
				#compile the info from the bechdel database
				bechdel_data={}
				for key in movie1:
					bechdel_data.update({key : movie1[key]})

				#print bechdel_data

				#reformat movies that have 'the' in the title in the Bechdel database
				if "the" in bechdel_data['title'].lower():
					new_title=bechdel_data['title'].split(",")
					bechdel_data['title']="The "+new_title[0]
				#print the info from the bechdel database
				for key in bechdel_data:
					print key,": ",bechdel_data[key]
				print "\n"
				#print the info from the open movie database
				for movie in responseomd2:
					for key in movie:
						print key,": ",movie[key]
		print "\n"

elif bmissing==0 and omissing==1:
	for movie in responseb:
		bechdel_data={}
		for key in movie1:
			bechdel_data.update({key : movie1[key]})
		#print bechdel_data
		#reformat movies that have 'the' in the title in the Bechdel database
		if "the" in bechdel_data['title'].lower():
			new_title=bechdel_data['title'].split(",")
			bechdel_data['title']="The "+new_title[0]
		#print the info from the bechdel database
		for key in bechdel_data:
			print key,": ",bechdel_data[key]

elif bmissing==1 and omissing==0:
	urlomd="http://www.omdbapi.com/?t="+title
	responseomd=[requests.get(urlomd).json()]
	for movie in responseomd:
		for key in movie:
			print key,": ",movie[key]
