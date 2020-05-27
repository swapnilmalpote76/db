from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpRequest, HttpResponseRedirect
from .models import employee
from .forms import EmployeeForm
from django.views.generic import *
from django.views.generic import TemplateView,ListView
from .forms import *



# Create your views here.
def home(request):
    print("a")
    Employee = employee.objects.all()
    # Employee = employee.objects.filter(age=21)
    # print(Employee)
    return render(request, 'a.html', {'employee': Employee})


class AboutView(ListView):
    model = employee
    template_name = "class_view.html"
    queryset = employee.objects.all()
    context_object_name = "a"
    paginate_by = 5






    # def get_queryset(self):
    #     return employee.objects.filter(age=21)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['a'] = employee.objects.all()
    #     return context






# def home(request):
#    return render(request, 'register.html', {'titles': 'django'})

def register(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            # print("employee is created")
            return HttpResponseRedirect('/')
    else:
        form = EmployeeForm()
    return render(request, "register.html", {'form': form})

    # return render(request, 'register.html')

# def submit(request):
#     if request.method == 'POST':
#         form=EmployeeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             print("employee is created")
#             return redirect('/')
#     else:
#         form=EmployeeForm()
#     return render(request,'register.html',{'form':form})
#
#
#
