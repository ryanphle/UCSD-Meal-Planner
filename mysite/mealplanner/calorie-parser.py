from urllib import urlopen
from bs4 import BeautifulSoup
import re

# Base of url to find different dining halls
baseURL = "https://hdh.ucsd.edu/DiningMenus/default.aspx?i="

# Dictionary of all dining hall codes
diningHallCodes = {'64':"64", 'cafev':'18', 'cv':'24', 'foodworx':'11', 'ovt':'05', 'pines':'01' }

def populateList(diningHall):
	
	foodList = {}

	# Finding the correct url of the passed in dining hall
	url = baseURL + diningHallCodes[diningHall]

	try:
		namePage = urlopen(url) 
		soup = BeautifulSoup(namePage, 'html.parser')
	except Exception as e: 
		# Printing the error if thrown
		print(e)
		return

	foodNames = soup.find_all('li')

	# Parses through all of the name links and populates dictionary
	for listItem in foodNames:
		if listItem.find('a', {"target" : "_blank"}):
			name = listItem.find('a', {"target" : "_blank"})
			foodList[str(name.contents[0])] = None


# Main Method
if __name__ == "__main__":
	populateList('64');