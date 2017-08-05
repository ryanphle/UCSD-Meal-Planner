from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response

#Home page for the landing page
def home(request):
	return render_to_response('homepage.html')
