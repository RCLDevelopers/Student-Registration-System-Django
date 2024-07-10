"""
URL configuration for studentregistration project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from authentication import views


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',views.show),
    path('reg/',views.register,name='reg'),
    path('all_stu/', views.all_stu, name = 'all_stu'),
    path('search_stu', views.search_stu, name = 'search_stu'),
    path('delete_stud', views.delete_stud, name = 'delete_stud'),
    path('delete_stud/<int:stud_id>', views.delete_stud, name = 'delete_stud'),
    path('update_student', views.update_student, name='update_student'),
    path('update_student/<int:id>', views.update_student, name='update_student'),
    path('Student/Update', views.STUDENT_UPDATE, name='student_update'),
    
    
]
