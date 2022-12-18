from django.shortcuts import render, HttpResponseRedirect
from . models import user
from . forms import studentform
from django.contrib import messages

# Create your views here.

def add_show(request):
    if request.method == "POST":
        fm = studentform(request.POST)
        if fm.is_valid():
# entered data in forms will be cleaned
            nm = fm.cleaned_data["name"]
            em = fm.cleaned_data["email"]
            pw = fm.cleaned_data["password"]
# cleaned form data will go in model web data (ie model class)
            reg = user(name=nm, email=em, password= pw)
            reg.save()
# after save() .. show empty form()
            fm = studentform()
    else:
        fm = studentform()
    studread = user.objects.all()
    return render (request, "enroll/addandshow.html", {"form":fm, "read": studread})

# to DELETE
def delete_data(request, id):
    if request.method == "POST":
        deldata = user.objects.get(pk = id)
        deldata.delete()
        return HttpResponseRedirect("/")

# to UPDATE
def update_data(request, id):
    if request.method == "POST":
        upd = user.objects.get(pk=id)
        fm = studentform(request.POST, instance=upd)
        if fm.is_valid():
            fm.save()
            fm = studentform()
    else:
        upd = user.objects.get(pk=id)
        fm = studentform(instance=upd)
    return render(request, "enroll/updatestudent.html", {"form":fm})
