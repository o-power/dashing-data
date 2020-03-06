from django.shortcuts import render

#from django.shortcuts import render, redirect, reverse
#from .forms import UploadDataForm

def upload_line_chart(request):
    return render(request, 'linechart/linechart.html')

#def create_bar_chart(request):
#    """Creates bar chart"""
#    return render(request, 'barchart/barchart.html')