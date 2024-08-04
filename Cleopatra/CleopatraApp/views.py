from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Course, Dancer
from CleopatraApp.qr_gen import qr_gen, get_dancer_courses

# Create your views here.
def go_home(request):
        return render(request, 'CleopatraApp/index.html')

def about_us(request):
        return render(request, 'CleopatraApp/about.html')

def saludo_User(request,user_Name):
    return HttpResponse( f"hola generico {user_Name.capitalize()}")

def show_template(request):
    return render(request, "CleopatraApp/index.html")

def show_dancers(request):
    dancers = Dancer.objects.all()
    context = {"dancers": dancers, }
    return render(request, 'CleopatraApp/dancers.html',context)

def show_dancer_profile(request, dancer_name):
    dancer = get_object_or_404(Dancer, name = dancer_name) #accedo al nombre de la planta
    id = dancer
    qr_path = qr_gen(id)
    courses_string = get_dancer_courses(dancer)
    context = {"dancer": dancer, "codigoqr": qr_path,"courses_string": courses_string}
    return render(request, 'CleopatraApp/profile.html',context)


def show_courses(request):
    courses = Course.objects.all()
    context = {"courses": courses}
    return render(request, 'CleopatraApp/courses.html',context)




