from django.shortcuts import render,redirect,render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.db.models import Q
from .models import Role,Family
# Create your views here.
# Remove all cxempts
@login_required(login_url = "/user/login")
def family_details(request):
	family_list,role_list = list(Family.objects.all()),[]
	if (request.method == 'POST'):
		try:
			family_pk = request.POST['family_pk']
			family = Family.objects.get(pk = family_pk)
			role_list = list(Role.objects.filter(family = family))
		except:
			print ("Error")
			# Show Error Page
	return render(request,'CareerModel/explore.html',{'family_list':family_list,'role_list':role_list})


@login_required(login_url = "/user/login")
def role_details(request):
	if (request.method == 'POST'):
		try:
			role_pk = request.POST['role_pk']
			role = Role.objects.get(pk = role_pk)
		except:
			return redirect('/career/explore')
			print("Error")
			# Show Error Page
	else:
		return redirect('/career/explore')
		#redirect
	return render(request,'CareerModel/role.html',{'role':role})

@login_required(login_url = "/user/login")
def search_roles(request):
	family_list,role_list = list(Family.objects.all()),[]
	if (request.method == 'POST'):
		try:
			# search query
			name_query = request.POST['name_query']
			family_pk = request.POST['family_pk']
			family = Family.objects.get(pk = family_pk)
			print (family)
			role_list = list(Role.objects.filter(Q(family = family) & Q(name__icontains = name_query)))
			print (role_list)
		except:
			return redirect('/career/explore')
		#redirect
	return render(request,'CareerModel/explore.html',{'family_list':family_list,'role_list':role_list})


@login_required(login_url = "/user/login")
def compare_roles(request):
	if (request.method == 'POST'):
		try:
			pk_list = request.POST.getlist('role_list')
			print (pk_list)
			role_pk1,role_pk2 = pk_list[0],pk_list[1]
			role1 = Role.objects.get(pk = role_pk1)
			role2 = Role.objects.get(pk = role_pk2)
		except:
			return redirect('/career/explore')
			print("Error")
			# Show Error Page
	else:
		return redirect('/career/explore')
		#redirect
	return render(request,'CareerModel/compare.html',{'role1':role1,'role2':role2})

@login_required(login_url = '/user/login')
def explore(request):
	family_list,role_list = list(Family.objects.all()),[]
	if (request.method == 'POST'):
		try:
			name_query = request.POST['name_query']
			family_pk = request.POST['family_pk']
			family = Family.objects.get(pk = family_pk)
			print (family)
			role_list = list(Role.objects.filter(Q(family = family) & Q(name__icontains = name_query)))
			print (role_list)
		except:
			do_nothing = True
	else:
		do_nothing = True
	return render(request,"CareerModel/explore.html",{'family_list':family_list,'role_list':role_list})