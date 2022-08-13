from urllib import request
from django.shortcuts import render,HttpResponse
from flask import render_template
from .models import Employee,Role,Department


# Create your views here.
def home(request):
    return render(request,'index.html')

def view_emp(request):
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    
    return render(request,'vemp.html',context)

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
       
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        new_emp = Employee(first_name= first_name, last_name=last_name, salary=salary, bonus=bonus, dept_id = dept, role_id = role)
        new_emp.save()
        return HttpResponse('Employee added Successfully')
    
    return render(request, 'aemp.html')
    
    
     
        
            

def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_removed=Employee.objects.get(id=emp_id)
            emp_removed.delete()
            return HttpResponse("Employee removed succesfully")

        except:
            return HttpResponse("Envalid Entry")
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request,'remp.html',context)

def filt_emp(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        dept=request.POST['dept']
        role=request.POST['role']
        salary=request.POST['salary']
        emps=Employee.objects.all()
        if first_name:
            emps=emps.filter(first_name__icontains=first_name)
        if last_name:
            emps=emps.filter(last_name__icontains=last_name)
        if dept:
            emps=emps.filter(dept__name__icontains=dept)
        if role:
            emps=emps.filter(role__name__icontains=role)
        if salary:
            emps=emps.filter(salary__gte=salary)

        context={
            "emps":emps
        }
        return render(request,'vemp.html',context)
    elif request.method=="GET":
        return render(request,'femp.html')

    