
from django import forms

class TextInputForm(forms.Form):
    text = forms.CharField(
        label="Enter Text",
        widget=forms.Textarea(attrs={"rows": 5, "cols": 60}),
        required=True
    )