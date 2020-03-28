from django.shortcuts import render, redirect, reverse
from .forms import UploadDataForm

def upload_chart(request):
    """
    A form through which the user uploads data.
    If method is POST, save data in a session object.
    If method is GET, render an empty upload data form.
    """
    if request.method == 'POST':
        upload_data_form = UploadDataForm(request.POST)

        if upload_data_form.is_valid():        
            chart_title = upload_data_form.cleaned_data['chart_title']
            chart_subtitle = upload_data_form.cleaned_data['chart_subtitle']
            x_data = upload_data_form.cleaned_data['x_data'].splitlines()
            y_data = upload_data_form.cleaned_data['y_data'].splitlines()
            
            y_data = list(map(float, y_data))
            print(y_data)

            bar_data = []
            for i in range(0,len(x_data),1):
                bar_data.append({'x_data': x_data[i], 'y_data': y_data[i]})
            
            request.session['chart_type'] = 'bar'
            request.session['chart_title'] = chart_title
            request.session['chart_subtitle'] = chart_subtitle
            request.session['chart_data'] = bar_data

            return redirect(reverse('barchart:create_chart'))
    else:
        upload_data_form = UploadDataForm()

    context = {'upload_data_form': upload_data_form}
    return render(request, 'barchart/upload.html', context)

def create_chart(request):
    """
    Render page with bar chart.
    """
    return render(request, 'barchart/chart.html')