from django.conf.urls import url
from django.views import generic
from . import views

app_name = 'circulation'
urlpatterns = [
	url(r'^$', generic.TemplateView.as_view(template_name='circulation/index.html')),
	url(r'^acceptRoll', views.AcceptRollView, name='acceptRoll'),
	url(r'^cancelBook', views.CancelBookView, name='cancelBook'),
	url(r'^issue', views.IssueView, name='issue'),
	url(r'^writeDB', views.WriteDBView, name='writeDB'),
		]
