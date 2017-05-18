from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^login$',views.employee_login,name = 'login'),
	url(r'^logout$',views.employee_logout,name = 'logout'), 	
	url(r'^profile$',views.profile,name = 'profile'),
]