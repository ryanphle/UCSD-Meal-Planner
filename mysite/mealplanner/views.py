from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from .calorie_parser import *

fullMenu = {}
foodList = {}

diningHallList = ['64 Degrees', 'Canyon Vista', 'OceanView Terrace', 
'Cafe Ventanas', 'Foodworx', 'Pines']

# Message Strings
reqDiningHallMsg = "*** A Dining Hall is required ***"
reqCaloriesMsg = "*** Calories are required ***"
noResultsMsg = "Sorry, there are no items at %s that are under %d calories."
resultsMsg = "Here are the menu items at %s that are under %d calories."

@csrf_exempt
def home(request):
	"""
	Returns homepage as the landing page
	"""
	return render_to_response('homepage.html', {'tableVisiblity':"display: none;"})

@csrf_exempt
def submit(request):
	"""
	Actions when user enters data
	"""
	if request.method == 'POST':
		dininghall = request.POST.get('dininghall')
		calories = request.POST['calories'].encode('utf-8')

		# Checking if dining hall and calories is entered, return required message if not
		if dininghall not in diningHallList and calories == "":
			return render_to_response('homepage.html', {'reqDiningHall':reqDiningHallMsg, 
				'reqCalories':reqCaloriesMsg, 'tableVisiblity':"display: none;"})
		elif dininghall not in diningHallList:
			return render_to_response('homepage.html', {'reqDiningHall':reqDiningHallMsg, 
				'tableVisiblity':"display: none;"})
		elif calories == "":
			return render_to_response('homepage.html', {'reqCalories':reqCaloriesMsg, 
				'tableVisiblity':"display: none;"})

		calories = int(calories)
		fullMenu = populateList(dininghall)
		foodList = findFoods(fullMenu, calories)

		# Checking if there were foods under the calorie limit
		if (len(foodList) > 0):
			return render_to_response('homepage.html', 
				{'d':foodList, 'resultsMsg':resultsMsg%(dininghall, calories), 
				'tableVisiblity':"display: visible;"})
		else:
			return render_to_response('homepage.html', 
				{'noresults':noResultsMsg%(dininghall, calories), 
				'tableVisiblity':"display: none;"})

	# Redirecting user to home page if went to link directly
	else:
		return HttpResponseRedirect(reverse('home'))