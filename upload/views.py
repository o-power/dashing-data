from django.shortcuts import render
from .forms import UploadDataForm

def upload(request):
    """A form through which the user uploads data"""

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        upload_data_form = UploadDataForm(request.POST)
        # check whether it's valid:
        if upload_data_form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            
            #subject = form.cleaned_data['chart_title']
            return render(request, 'upload_test.html', {'form_data_dict': upload_data_form.cleaned_data})

    # if a GET (or any other method) we'll create a blank form
    else:
        upload_data_form = UploadDataForm()

    return render(request, 'upload.html', {'upload_data_form': upload_data_form})
