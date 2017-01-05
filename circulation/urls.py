from django.conf.urls import url
from django.views import generic
from . import views

app_name = 'circulation'
urlpatterns = [
	url(r'^$', views.HomeView, name='home'),
	url(r'^start', views.StartView, name='start'),
	url(r'^cancelBook', views.CancelBookView, name='cancelBook'),
	url(r'^issue', views.IssueView, name='issue'),
	url(r'^about', generic.TemplateView.as_view(template_name='circulation/about.html'), name='about'),
	url(r'^writeDB', views.WriteDBView, name='writeDB'),
		]
