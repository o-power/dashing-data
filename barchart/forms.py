from django import forms

class UploadDataForm(forms.Form):
    """
    Form for uploading data.
    """
    chart_title = forms.CharField(
        label='Chart Title',
        max_length=254,
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