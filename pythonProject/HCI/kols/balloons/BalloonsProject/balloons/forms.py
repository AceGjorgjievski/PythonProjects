from django import forms
from .models import *


class FlightForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for f in self.visible_fields():
            f.field.widgets.attrs["class"] = "form-control"

    class Meta:
        model = Flight
        exclude = ["user",]
