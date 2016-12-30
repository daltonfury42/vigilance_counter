from django.conf.urls import url
from django.views import generic
from . import views

app_name = 'search'
urlpatterns = [
	url(r'^$', generic.TemplateView.as_view(template_name='search/index.html'), name='home'),
	url(r'^getQuery', views.getQueryView, name='getQuery'),
	url(r'^downloadCSV', views.downloadCsvView, name='downloadCSV'),
		]
