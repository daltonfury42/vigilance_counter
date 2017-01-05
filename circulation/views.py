from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import CheckOuts
from django.utils import timezone
from datetime import date
from .desktopReader import getPatronIDAndBooksList

desktopReaderIP = '192.168.240.149'
desktopReaderPort = 100

# Create your views here.
def HomeView(request):
        today = date.today()
        todays_entries = CheckOuts.objects.filter(time_stamp__year = today.year, time_stamp__month = today.month, time_stamp__day = today.day)
        books_count = len({entry.accn_no for entry in todays_entries})
        patrons_count = len({entry.roll for entry in todays_entries})
        request.session['roll'] = '' 
        request.session['books'] = ''
        return render(request, 'circulation/index.html', { 'books_count':books_count, 'patrons_count':patrons_count })

def IssueView(request):
	if 'accn_no' in request.POST.keys():
		request.session['books'].append(request.POST['accn_no'])
	if 'roll' in request.POST.keys():
		request.session['roll'] = request.POST['roll']
                
	request.session.modified = True
	return render(request, 'circulation/issue.html', { 'roll': request.session['roll'], 'books':request.session['books']})
	
	
def StartView(request):
        RFID_Data = getPatronIDAndBooksList(desktopReaderIP, desktopReaderPort)
        request.session['roll'] = RFID_Data['patron']
        request.session['books'] = RFID_Data['books']
        request.session.modified = True

        return HttpResponseRedirect(reverse('circulation:issue'))

def CancelBookView(request):
	request.session['books'].remove(request.POST['cancel'])
	request.session.modified = True

	return HttpResponseRedirect(reverse('circulation:issue'))

def WriteDBView(request):
	for book in request.session['books']:
		CheckOuts(roll=request.POST['roll'], accn_no=book, time_stamp=timezone.now()).save()

	return HttpResponseRedirect(reverse('circulation:home'))
	#return render(request, 'circulation/index.html', { 'prev_transaction':'success' })

