from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from circulation.models import CheckOuts
import csv
import datetime

# Create your views here.
def getQueryView(request):
	query_set = CheckOuts.objects.all()
	if request.POST['rollno']:
		query_set = query_set.filter(roll = request.POST['rollno'])

	if request.POST['bookno']:
		query_set = query_set.filter(accn_no = request.POST['bookno'])

	if request.POST['from_dd'] and request.POST['from_mm'] and request.POST['from_yy']:
		query_set = query_set.filter(time_stamp__gte = datetime.date(int(request.POST['from_yy']), int(request.POST['from_mm']), int(request.POST["from_dd"])))

	if request.POST['to_dd'] and request.POST['to_mm'] and request.POST['to_yy']:
		query_set = query_set.filter(time_stamp__lte = datetime.date(int(request.POST['to_yy']), int(request.POST['to_mm']), int(request.POST["to_dd"])))
	
	request.session['query'] = str(query_set.query)
	request.session.modified = True

	return render(request, 'search/results.html', { 
		'results':query_set, 
		'rollno':request.POST['rollno'], 
		'bookno':request.POST['bookno'], 
		'from_dd':request.POST['from_dd'], 
		'from_mm':request.POST['from_mm'], 
		'from_yy':request.POST['from_yy'],
		'to_dd':request.POST['to_dd'], 
		'to_mm':request.POST['to_mm'], 
		'to_yy':request.POST['to_yy'],
		
		})
		
def downloadCsvView(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="results.csv"'

	writer = csv.writer(response)
	writer.writerow(['Entry ID','Patron ID', 'Accession Number', 'Time Stamp'])

	query_set = CheckOuts.objects.all()
	if 'rollno' in request.POST.keys():
		query_set = query_set.filter(roll = request.POST['rollno'])

	if 'bookno' in request.POST.keys():
		query_set = query_set.filter(accn_no = request.POST['bookno'])

	if request.POST['from_dd'] and request.POST['from_mm'] and request.POST['from_yy']:
		query_set = query_set.filter(time_stamp__gte = datetime.date(int(request.POST['from_yy']), int(request.POST['from_mm']), int(request.POST["from_dd"])))

	if request.POST['to_dd'] and request.POST['to_mm'] and request.POST['to_yy']:
		query_set = query_set.filter(time_stamp__lte = datetime.date(int(request.POST['to_yy']), int(request.POST['to_mm']), int(request.POST["to_dd"])))
	
	for row in query_set:
		writer.writerow([row.pk ,row.roll, row.accn_no, row.time_stamp])

	return response
