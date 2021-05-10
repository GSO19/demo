from django import forms  
from app.models import App  
class appForm(forms.ModelForm):  
    class Meta:  
        model = App  
        fields = "__all__"  