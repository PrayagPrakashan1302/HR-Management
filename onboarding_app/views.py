from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Employee
from .forms import EmployeeForm
from django.contrib.auth import authenticate, login 
from django.http import JsonResponse  

def login_page(request):
    if request.user.is_authenticated:
        return redirect("/appemployee-list/")
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('employee_list')
            else:
                # Add error message for invalid credentials
                return render(request, 'login.html')
        return render(request, 'login.html')

@login_required(login_url='my_login_url')
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

@login_required(login_url='my_login_url')
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employee_detail.html', {'employee': employee})

@login_required(login_url='my_login_url')
def employee_add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee_add.html', {'form': form})

@login_required(login_url='my_login_url')
def onboard_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.is_onboarded = True
    employee.save()
    return redirect('employee_list')


def onboard_check(request):
    is_checked = request.GET.get("is_checked")
    emp_id = request.GET.get("emp_id")
    
    onboard= False
    
    if is_checked == 'true':
        onboard = True 
    
    emp = Employee.objects.get(id=emp_id)
    emp.is_onboarded = onboard
    emp.save()

    return JsonResponse({"message":"Onboarded successfully"})


from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    # Redirect to a different page or URL after logging out
    return redirect('/')

