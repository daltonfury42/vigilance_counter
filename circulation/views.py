from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import CheckOuts
from django.utils import timezone

# Create your views here.
def IssueView(request):
	if 'accn_no' in request.POST.keys():
		request.session['books'].append(request.POST['accn_no'])
	request.session.modified = True
	return render(request, 'circulation/issue.html', { 'roll': request.session['roll'], 'books':request.session['books']})
	
	
def AcceptRollView(request):
	request.session['roll'] = request.POST['roll']
	request.session['books'] = []

	return HttpResponseRedirect(reverse('circulation:issue'))

def CancelBookView(request):
	request.session['books'].remove(request.POST['cancel'])
	request.session.modified = True

	return HttpResponseRedirect(reverse('circulation:issue'))

def WriteDBView(request):
	for book in request.session['books']:
		CheckOuts(roll=request.session['roll'], accn_no=book, time_stamp=timezone.now()).save()

	return render(request, 'circulation/index.html', { 'prev_transaction':'success' })

