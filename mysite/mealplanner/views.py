from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

#Home page for the landing page
@csrf_exempt
def home(request):
	return render_to_response('homepage.html')

@csrf_exempt
def submit(request):
	return render_to_response('test.html')