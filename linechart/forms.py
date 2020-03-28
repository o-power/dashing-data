from django import forms
from datetime import datetime
from django.utils import timezone

class UploadDataForm(forms.Form):
    """
    Form for uploading data.
    """
    DATE_FORMAT_CHOICES = [
		('%m-%d-%Y', timezone.now().strftime('%m-%d-%Y')),
        ('%m/%d/%Y', timezone.now().strftime('%m/%d/%Y')),
		('%d-%m-%Y', timezone.now().strftime('%d-%m-%Y')),
		('%d/%m/%Y', timezone.now().strftime('%d/%m/%Y')),
    ]
    
    chart_title = forms.CharField(
        label='Chart Title',
        max_length=254,
        required=True,
    )

    chart_subtitle = forms.CharField(
        label='Chart Subtitle',
        max_length=254,
        required=False,
    )

    date_format = forms.ChoiceField(
        label='Date Format',
		choices=DATE_FORMAT_CHOICES,
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
            raise forms.ValidationError('y data must be numeric.')

        return y_data
    
    def clean(self):
        """
        Number of entries in x and y data should be the same.
        """
        cleaned_data = super().clean()
        date_format = cleaned_data.get('date_format')
        x_data = cleaned_data.get('x_data')
        y_data = cleaned_data.get('y_data')

        # Only do something if fields are valid so far
        if x_data and date_format:
            parsed_x_data = x_data.splitlines()
            try:
                parsed_x_data = [datetime.strptime(x, date_format) for x in parsed_x_data]
            except ValueError:
                raise forms.ValidationError('x data must be in chosen date format.')

        # Only do something if fields are valid so far.
        if x_data and y_data:
            parsed_x_data = x_data.splitlines()
            parsed_y_data = y_data.splitlines()
            
            if len(parsed_x_data) != len(parsed_y_data):
                raise forms.ValidationError(
                    'Number of y values must match number of x values.'
                )