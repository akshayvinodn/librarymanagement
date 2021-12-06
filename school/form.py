from django import forms  
from .models import Students1,Book  
class EmpForm(forms.ModelForm):  
    class Meta:  
        model = Students1  
        fields = "__all__"  
class BkForm(forms.ModelForm):  
    class Meta:  
        model = Book 
        fields = "__all__"  