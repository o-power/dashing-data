from django import forms

class UploadDataForm(forms.Form):
    chart_title = forms.CharField(
        label='Chart Title',
        max_length=100,
        required=True,
    )

    x_data = forms.CharField(
        label='X Data',
        widget=forms.Textarea,
        required=True,
    )

    y_data = forms.CharField(
        label='Y Data',
        widget=forms.Textarea,
        required=True,
    )
    
# https://docs.djangoproject.com/en/3.0/ref/forms/api/#binding-uploaded-files
# https://docs.djangoproject.com/en/3.0/ref/forms/fields/