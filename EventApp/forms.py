from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class DateForm(forms.Form):
    date = forms.DateTimeField(widget=DateInput)