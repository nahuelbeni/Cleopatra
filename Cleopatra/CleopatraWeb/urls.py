"""CleopatraWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from CleopatraApp.views import go_home, show_courses, show_dancer_profile, show_dancers
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('CleopatraApp/index',go_home),
#     path('CleopatraApp/profile',show_dancer_profile),
#     path('CleopatraApp/courses',show_courses),
#     path('CleopatraApp/dancers',show_dancers),
# ]


from django.contrib import admin    
from django.urls import path
from CleopatraApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('CleopatraApp/index',views.go_home, name="Index"),
    path('CleopatraApp/about_us',views.about_us, name="About"),
    # path('CleopatraApp/profile',views.show_dancer_profile, name="Profile"),
    path('CleopatraApp/courses',views.show_courses, name="Courses"),
    path('CleopatraApp/dancers',views.show_dancers, name="Dancers"),
    path('CleopatraApp/profile/<str:dancer_name>/', views.show_dancer_profile, name='profile'), 
]
