from django.shortcuts import render,redirect
from django.http import HttpResponse
from .form import BkForm, EmpForm  
from .models import Students1,Book
# Create your views here. 
def home(request):
    books=Book.objects.all()
    return render(request,"home.html",{'books':books})   
def emp(request):  
    if request.method == "POST":  
        form = EmpForm(request.POST or None)  
        if form.is_valid():
            form.save()  
            return redirect('show')  
        
    else:  
        form = EmpForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    students = Students1.objects.all()  
    return render(request,'show.html',{'students':students})

def edit(request, id):  
    student = Students1.objects.get(id=id)  
    return render(request,'edit.html', {'student':student})  

def update(request,id):
    student=Students1.objects.get(id=id)
    form=EmpForm(request.POST,instance=student)
    if form.is_valid():
        form.save()
        return redirect("show")
    return render(request,'edit.html',{'student':student})  
def destroy(request,id):
    student=Students1.objects.get(id=id)
    student.delete()
    return redirect("/show")

def empbook(request):  
    if request.method == "POST":  
        form = BkForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()  
            return redirect('bookshow')  
    else:
        form = BkForm()
    return render(request, 'bookindex.html', {'form' : form})
  
  
def success(request):
    return HttpResponse('successfully uploaded')

        
    # else:  
    #     form = BkForm()  

    return render(request,'bookindex.html',{'form':form})  
def bookshow(request):  
    students = Book.objects.all()  
    return render(request,'bookshow.html',{'students':students})

def bookedit(request, id):  
    student = Book.objects.get(id=id)  
    return render(request,'bookedit.html', {'student':student})  

def bookupdate(request,id):
    student=Book.objects.get(id=id)
    form=BkForm(request.POST,request.FILES,instance=student,)
    if form.is_valid():
        form.save()
        return redirect("bookshow")
    else:
        form = BkForm()
    return render(request, 'bookedit.html', {'form' : form})
  
  
def success(request):
    return HttpResponse('successfully uploaded')
    # return render(request,'bookedit.html',{'student':student})  
def bookdestroy(request,id):
    student=Book.objects.get(id=id)
    student.delete()
    return redirect("/bookshow")