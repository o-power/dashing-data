from django.shortcuts import render

def index(request):
    """A view that displays the index page"""
    return render(request, "index.html")

def create_chart(request):
    """Lists available chart types"""
    return render(request, 'createchart.html')