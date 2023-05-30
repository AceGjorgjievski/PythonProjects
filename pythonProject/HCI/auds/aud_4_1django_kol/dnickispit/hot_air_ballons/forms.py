from django import forms
from .models import Flight


class FlightForm(forms.ModelForm):

    def __init__(self):
        #od gitlab da prevzememe
        pass

    class Meta:
        model = Flight
        exclude = ("user",)
