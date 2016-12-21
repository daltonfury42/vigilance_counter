from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def getQueryView(request):
	return HttpResponse("Works!")

