from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
def IssueView(request):
	if 'books' not in request.session.keys():
		request.session['books'] = []
	if 'accn_no' in request.POST.keys():
		request.session['books'].append(request.POST['accn_no'])

	return render(request, 'circulation/issue.html', { 'roll': request.session['roll'], 'books':request.session['books']})
	
	
def AcceptRollView(request):
	request.session['roll'] = request.POST['roll']

	return HttpResponseRedirect(reverse('circulation:issue'))
