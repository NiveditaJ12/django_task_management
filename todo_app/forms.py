from django import forms # type: ignore
from .models import ToDoModel,StartTime

STATUS_CHOICES = [
        ('DONE','Done'),
        ('UNFINISHED','Unfinished'),
        ('POSTPONED', 'Postponed'),
        ('CANCELLED', 'Cancelled'),
    ]
    

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDoModel
        fields = ('sr_no','task','status')

        widgets = {
            "sr_no" : forms.NumberInput(attrs={'class':'form-control', 'placeholder':""}),
            "task" : forms.TextInput(attrs={'class':'form-control', 'placeholder':""}),
            
        }
class StartTimeForm(forms.ModelForm):
    class Meta:
        model = StartTime
        fields = ('start_time',)
        widgets = {
            "start_time" : forms.TimeInput(attrs={'class':'form-control', 'placeholder':""})
        }