from django import forms  
from .models import Student
class StudentForm(forms.ModelForm):  
    firstname = forms.CharField(label="Enter first name",max_length=50)  
    lastname  = forms.CharField(label="Enter last name", max_length = 10)  
    email     = forms.EmailField(label="Enter Email")  
    file      = forms.FileField() # for creating file input  
        
    class Meta:
        model = Student
        fields = ('firstname','lastname','email','file')
    