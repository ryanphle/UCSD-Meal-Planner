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

#Home page for the landing page
@csrf_exempt
def home(request):
	return render_to_response('homepage.html')

@csrf_exempt
def submit(request):
	if request.method == 'POST':
		fullMenu = populateList('64')
		foodList = findFoods(fullMenu, 200)
		return render_to_response('test.html')
	else:
		return HttpResponseRedirect(reverse('home'))