from django.shortcuts import render
from django.http import HttpResponse
from circulation.models import CheckOuts

# Create your views here.
def getQueryView(request):
	if request.POST['rollno']:
		roll = "'" + request.POST['rollno'] + "'"
	else:
		roll = 'roll'

	if request.POST['bookno']:
		accn_no = "'" + request.POST['bookno'] + "'"
	else:
		accn_no = 'accn_no'

	if request.POST['from_dd'] and request.POST['from_mm'] and request.POST['from_yy']:
		from_date = request.POST['from_yy'] + '-' + request.POST['from_mm'] + '-' + request.POST["from_dd"]
	else:
		from_date = '2016-01-01'

	if request.POST['to_dd'] and request.POST['to_mm'] and request.POST['to_yy']:
		to_date = request.POST['to_yy'] + '-' + request.POST['to_mm'] + '-' + request.POST["to_dd"]
	else:
		to_date = '2032-01-01'

	query = "SELECT * FROM circulation_checkouts WHERE roll = " + roll + " and accn_no = " + accn_no + " and time_stamp > Datetime('" + from_date + " 00:00:00') and time_stamp < Datetime('" + to_date + " 23:59:59')"
	print("Query: " + query)
	for p in CheckOuts.objects.raw(query):
		print(p.roll)

	return HttpResponse("Works!")
		
