from django.shortcuts import render,HttpResponseRedirect
from .models import User,Project,Task
from .forms import ProjectForm, TaskForm
# Create your views here.


def Project_show(request):
    if request.method == 'POST':
        fm = ProjectForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            ds = fm.cleaned_data['description']
            sd = fm.cleaned_data['start_date']
            ed = fm.cleaned_data['end_date']
            reg = Project(name=nm,description=ds,start_date=sd,end_date=ed)
            reg.save()
            fm = ProjectForm()
    else:
        fm = ProjectForm()
    stud = Project.objects.all()
    return render(request,'app/addandshow.html',{'form':fm,'stu':stud})


def update_data(request,id):
    if request.method == 'POST':
        pi = Project.objects.get(pk=id)
        fm = ProjectForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Project.objects.get(pk=id)
        fm = ProjectForm(instance=pi)
    return render(request,'app/updateproject.html',{'form':fm})


def delete_data(request,id):
    if request.method =='POST':
        pi = Project.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    


#Task Crud Operation



def Task_show(request):
    if request.method == 'POST':
        fm = TaskForm(request.POST)
        if fm.is_valid():
            p = fm.cleaned_data['project']
            t = fm.cleaned_data['title']
            d = fm.cleaned_data['description']
            dl = fm.cleaned_data['deadline']
            s = fm.cleaned_data['status']
            reg = Task(project=p,title=t,description=d,deadline=dl,status=s)
            reg.save()
            fm = TaskForm()
    else:
        fm = TaskForm()
    stud = Task.objects.all()
    return render(request,'app/addandshowtask.html',{'form':fm,'stu':stud})


def update_task(request,id):
    if request.method == 'POST':
        pi = Task.objects.get(pk=id)
        fm = TaskForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Task.objects.get(pk=id)
        fm = TaskForm(instance=pi)
    return render(request,'app/updatetask.html',{'form':fm})


def delete_task(request,id):
    if request.method =='POST':
        pi = Task.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    