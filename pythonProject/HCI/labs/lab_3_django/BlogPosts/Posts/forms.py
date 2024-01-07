from django import forms
from .models import *



class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for f in self.visible_fields():
            f.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Post
        # fields = ['title', 'author', 'content', 'files',]
        exclude = ['user',]

class BlockForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for f in self.visible_fields():
            f.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Block
        fields = ['user_blocked',]
