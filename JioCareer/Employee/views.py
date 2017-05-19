from django.shortcuts import render,redirect,render_to_response
from django.contrib.auth import authenticate,login,logout
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Employee
from CareerModel.models import Role,Family

# Create your views here.

def employee_login(request):
	if (request.user.is_authenticated()):
		return redirect('/user/profile')
	elif (request.method == 'POST'):
		try:
			username = request.POST['username']
			password = request.POST['password']
			print (username)
			user = authenticate(username = username,password = password)
			print (username,password)
			if (user is not None):
				print ("correct combination")
				login(request,user)
				print ("login success")
				return redirect('/user/profile')
			else:
				return redirect('/user/login')
		except Exception as error:
			print (error)
			# Handle This Case
	return render(request,'Employee/login.html')


def employee_logout(request):
	if (request.user.is_authenticated()):
		logout(request)
	return redirect('/user/login')

@login_required(login_url = '/user/login')
def profile(request):
	employee = Employee.objects.get(user = request.user)
	rprev = rnext = employee.role
	lprev,lnext,role_list,rlist = list(rprev.role_set.all()),list(rnext.next_roles.all()),[],[employee.role]
	prole = 0
	while (lprev):
		print (lprev)
		rprev = lprev[0]
		if (employee.role != rprev):
			rlist.insert(0,rprev)
		lprev = list(rprev.role_set.all())
		prole += 1
	while (lnext):
		print (lnext)
		rnext = lnext[0]
		if (employee.role != rnext):
			rlist.append(rnext)
		lnext = list(rnext.next_roles.all())
	if (len(rlist) > 7):
		clen,p_idx,n_idx = 1,prole - 1,prole + 1
		role_list.insert(employee.role)
		while (clen != 7):
			if (p_idx >= 0):
				role_list.insert(0,rlist[p_idx])
				p_idx -= 1
				clen += 1
			if (n_idx < len(rlist)):
				role_list.append(rlist[n_idx])
				n_idx += 1
				clen += 1
	else:
		role_list = rlist
	print (role_list)
	return render(request,'Employee/profile.html',{'employee':employee,'role_list':role_list})
