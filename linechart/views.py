from django.shortcuts import render

#from django.shortcuts import render, redirect, reverse
#from .forms import UploadDataForm

def upload_chart(request):
    return render(request, 'linechart/chart.html')

#def create_chart(request):
#    """Creates line chart"""
#    return render(request, 'linechart/chart.html')