from urllib import urlopen
from bs4 import BeautifulSoup
from multiprocessing import Pool
from functools import partial
import re

# Base of url to find different dining halls
baseURL = "https://hdh.ucsd.edu/DiningMenus/default.aspx?i="
foodURL = "https://hdh.ucsd.edu/DiningMenus/"

# Dictionary of all dining hall codes
diningHallCodes = {'64':"64", 'cafev':"18", 'cv':"24", 'foodworx':"11", 'ovt':"05", 'pines':"01" }

def populateList(diningHall):
	""" 
	Populates and returns a dictionary of food with the link to their nutrition facts 
	of the dining hall given 
	"""

	foodDict = {}

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
			name = listItem.find('a', {"target" : "_blank"}).string.encode('utf-8')

			# Removing the prices if needed
			priceMarker = name.find("(")
			if priceMarker != -1:
				name = name[:priceMarker]

			# Adding the food name to the dictionary
			foodDict[name] = foodURL + listItem.find('a')['href'].encode('utf-8')

	return foodDict
'''
def findFoodCals(foodDict, calorieLimit):
	"""
	Returns a sublist of food within the given calorie limit
	"""

	newFoodList = {}

	# Parsing through list of food
	for key, value in foodDict.items():
		try:
			nutritionPage = urlopen(value) 
			soup = BeautifulSoup(nutritionPage, 'html.parser')
		except Exception as e: 
			# Printing the error if thrown
			print(e)
			return
			
		# Finding the calories in the list
		calories = soup.find('span', {"style" : "font-weight:bold;"}).string

		# Removing the Calories label and converting to int
		numMarker = calories.find(' ')
		calories = int(calories[numMarker+1:])

		# Comparing the calories of each food to the limit
		if calories <= calorieLimit:
			newFoodList[key] = calories
		

	return newFoodList
'''

def findCalories(url, calorieLimit):
	try:
		nutritionPage = urlopen(url) 
		soup = BeautifulSoup(nutritionPage, 'html.parser')
	except Exception as e: 
		# Printing the error if thrown
		print(e)
		return

	# Finding the calories in the list
	calories = soup.find('span', {"style" : "font-weight:bold;"}).string

	# Removing the Calories label and converting to int
	numMarker = calories.find(' ')
	calories = int(calories[numMarker+1:])

	# Comparing the number of calories
	if calories <= calorieLimit:
		return calories

	return -1

def findFoods(foodDict, calorieLimit):
	newFoodList = {}

	p = Pool(30)
	calories = p.map(partial(findCalories, calorieLimit=calorieLimit), foodDict.values())

	p.terminate()
	p.join()

	newFoodList = dict(zip(foodDict.keys(), calories))
	newFoodList = {key : value for key, value in newFoodList.items() if value != -1}

	return newFoodList

# Main Method
if __name__ == "__main__":
	list = populateList('64')
	print(findFoods(list, 400))