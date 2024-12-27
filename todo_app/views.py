from django.shortcuts import render, redirect # type: ignore
from datetime import datetime
from .forms import ToDoForm,StartTimeForm
from .models import ToDoModel, StartTime

def index(request):
    now = datetime.now()
    form1 = ToDoForm(request.POST or None)
    form2 = StartTimeForm(request.POST or None)
    if request.method == 'POST':
            if 'form1_submit' in request.POST:
                if form1.is_valid():
                    sr_no = form1.cleaned_data['sr_no']
                    task = form1.cleaned_data['task']
                    status = form1.cleaned_data['status']
                    form1.save()
            elif 'form2_submit' in request.POST:
                form2 = StartTimeForm(request.POST)
                if form2.is_valid():
                    start_time = form2.cleaned_data['start_time']
                    form2.save()
      
    todo = ToDoModel.objects.all()
    prev_time = StartTime.objects.all().order_by('-id')[1:]
    for i in prev_time:
        i.delete()
    time_start = StartTime.objects.last()
    return render(request, 'index.html', {'form':form1, 
                                          'time_form':form2,'task':todo, 
                                          'current_time':now.strftime('%Y-%m-%d %H:%M:%S'),
                                           'time_start':time_start})

def change_task(request, id):
    now = datetime.now()
    todo = ToDoModel.objects.get(id=id)
    form = ToDoForm(instance=todo)
    if request.method =='POST':
        form = ToDoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
        return redirect('index')
    return render(request, 'edit.html', {'form':form, 'current_time':now.strftime('%Y-%m-%d %H:%M:%S')})

def remove_task(request,id):
    todo = ToDoModel.objects.get(id=id)
    todo.delete()

    all_todos = ToDoModel.objects.all()
    for i,todo1 in enumerate(all_todos):
        todo1.sr_no = i+1
        todo1.save()
    return redirect('index')