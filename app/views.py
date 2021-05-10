from django.shortcuts import render, redirect  
from app.forms import appForm  
from app.models import App  
# Create your views here.  
def emp(request):  
    if request.method == "POST":  
        form = appForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = appForm()  
    return render(request,'index.html',{'form':form})  

def show(request):  
    apps = App.objects.all()  
    return render(request,"show.html",{'apps':apps})  


def edit(request, id):  
    app = App.objects.get(id=id)  
    return render(request,'edit.html', {'app':app})  
    
def update(request, id):  
    app = App.objects.get(id=id)  
    form = appForm(request.POST, instance = app)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'app': app})  
def destroy(request, id):  
    app = App.objects.get(id=id)  
    app.delete()  
    return redirect("/show")  