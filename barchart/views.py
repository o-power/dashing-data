from django.shortcuts import render

from django.shortcuts import render, redirect, reverse
from .forms import UploadDataForm

def upload_chart(request):
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
            
            chart_title = upload_data_form.cleaned_data['chart_title']
            x_data = upload_data_form.cleaned_data['x_data'].splitlines()
            y_data = upload_data_form.cleaned_data['y_data'].splitlines()

            y_data = list(map(int, y_data))

            request.session['chart_type'] = 'bar'

            #return redirect(create_bar_chart, chart_title)
            #uploaded_data = request.session.get('uploaded_data', {})
            uploaded_data = {}

            uploaded_data['chart_title'] = chart_title
            uploaded_data['x_data'] = x_data
            uploaded_data['y_data'] = y_data
            
            bar_data = []
            for i in range(0,len(x_data),1):
                bar_data.append({'x_data': x_data[i], 'y_data': y_data[i]})
            
            uploaded_data['bar_data'] = bar_data

            request.session['uploaded_data'] = uploaded_data

            #print(request.session['uploaded_data'])

            return redirect(reverse('barchart:create_chart'))
            #return render(request, 'upload_test.html', {'form_data_dict': upload_data_form.cleaned_data,
            #'x_data': x_data,
            #                                            'y_data': y_data,})


            # Don't forget to empty session dict when finished
            #request.session['cart'] = {}

    # if a GET (or any other method) we'll create a blank form
    else:
        upload_data_form = UploadDataForm()

    return render(request, 'barchart/upload.html', {'upload_data_form': upload_data_form})

def create_chart(request):
    """Creates bar chart"""
    return render(request, 'barchart/chart.html')