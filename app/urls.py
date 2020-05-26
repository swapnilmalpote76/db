from django.contrib import admin
from django.urls import path
from . import views
from .views import AboutView

from django.views.generic import TemplateView

# from .views import submit,home
app_name = 'app'
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('cbview/',AboutView.as_view()),
    # path('listview/',views.EmployeeList.as_view()),
    # path('submit/', views.submit, name='sub')
]
