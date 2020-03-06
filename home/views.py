from django.shortcuts import render

def index(request):
    """A view that displays the index page"""
    return render(request, 'home/index.html')

def create_chart(request):
    """Lists available chart types"""
    return render(request, 'home/createchart.html')