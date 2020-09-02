from .models import Leave_data
from django import forms


class LeaveForm(forms.ModelForm):
    start_date = forms.DateField(label= "Leave Start Date :" , widget = forms.SelectDateWidget())
    end_date = forms.DateField(label= "Leave End Date :" , widget = forms.SelectDateWidget())

    class Meta:
        model = Leave_data
        fields = ['start_date', 'end_date' , 'disc' ]
        #  , 'mob_no'
