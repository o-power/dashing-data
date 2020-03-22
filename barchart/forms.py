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
        
        try:
            parsed_y_data = list(map(float, parsed_y_data))
        except ValueError:
            raise forms.ValidationError('y data must be numeric')

        return y_data
    
    def clean(self):
        """
        Number of entries in x and y data should be the same.
        """
        cleaned_data = super().clean()
        x_data = cleaned_data.get('x_data')
        y_data = cleaned_data.get('y_data')

        if x_data and y_data:
            # Only do something if both fields are valid so far.
            parsed_x_data = x_data.splitlines()
            parsed_y_data = y_data.splitlines()
            
            if len(parsed_x_data) != len(parsed_y_data):
                raise forms.ValidationError(
                    'Number of y values must match number of x values'
                )