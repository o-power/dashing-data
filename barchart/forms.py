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

    def clean_y_data(self):
        """
        y_data should be numeric
        """
        y_data = self.cleaned_data['y_data']

        parsed_y_data = y_data.splitlines()
        print(parsed_y_data)
        
        try:
            parsed_y_data = list(map(float, parsed_y_data))
        except ValueError:
            raise forms.ValidationError("y data must be numeric")

        return y_data