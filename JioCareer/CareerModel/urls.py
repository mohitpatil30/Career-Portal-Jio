from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^explore$',views.explore,name = 'explore'),
	url(r'^compare$',views.compare_roles,name = 'compare_roles'),
]