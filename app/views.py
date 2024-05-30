from django.shortcuts import render,redirect
from .models import Register,task
from .forms import UserRegisterForm



# Create your views here.
def ragister(request):
    obj=UserRegisterForm(request.POST) 
    if obj.is_valid():
        data=Register.objects.all().filter(email=request.POST['email'])
        if len(data)<=0:
            obj.save()
            return redirect('tableview')
        else:
            return render(request,'ragister.html')
    return render(request,'ragister.html')


import dateutil.parser as parser
def tableview(request):
    data=task.objects.all()
    
    return render(request,'table.html',{'data':data})

def deletetable(request,id):
    a=task.objects.get(id=id)
    a.delete()
    return redirect('tableview')
def addtable(request):
    print("hii")
    a=Register.objects.all()
    if request.method=="POST":
        user_id=request.POST['user']
        name=request.POST['name']
        decription=request.POST['decription']
        category=request.POST['category']
        Create_date=request.POST['Create_date']
        user=Register.objects.get(id=user_id)
        task.objects.create(user=user,name=name,decription=decription,category=category,Create_date=Create_date)
        return redirect('tableview')
    return render(request,'adddta.html',{'a':a})

def updatetable(request,id):
    print("hii")
    a=task.objects.get(id=id)
    if request.method=="POST":
        model=task.objects.get(id=id)
        model.name=request.POST['name']
        model.decription=request.POST['decription']   
        model.save()
        return redirect('tableview')
    return render(request,'update.html',{'a':a})

def filterdata(request):
    Category = request.GET.get('Category')
    date=request.GET.get('Create_date')
    date_time = parser.parse(date)
    # print(str(date_time))
    categoryfilter = task.objects.filter(category=Category) & task.objects.filter(Create_date=date_time)
    return render(request,'filter.html',{'data':categoryfilter})