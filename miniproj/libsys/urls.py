from django.conf.urls import patterns, url
from libsys import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^signup/', views.signup, name='signup'),
	url(r'^success/', views.signupsuccess, name='signupsuccess'),
	url(r'^userhome/', views.dashboard, name='dashboard'),
	url(r'^bookborrow/', views.bookborrow, name='bookborrow'),
	url(r'^viewbooks/', views.viewbooks, name='viewbooks'),
	url(r'^viewstatus/', views.viewstatus, name='viewstatus'),

)

