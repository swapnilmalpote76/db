from .models import *
from django import forms
from .models import employee


class EmployeeForm(forms.ModelForm):
    # name = forms.CharField(max_length=30)
    # address = forms.CharField(max_length=100)
    # #status = forms.BooleanField(default=False)
    # salary = forms.IntegerField()
    # age = forms.IntegerField()

    class Meta:
        model = employee
        fields = ['name', 'address','salary', 'age']
