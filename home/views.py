from django.shortcuts import render, get_object_or_404, redirect, reverse

def index(request):
    """
    A view that displays the index page.
    """
    return render(request, 'home/index.html')

def create_chart(request):
    """
    A view that lists the available chart types.
    """
    return render(request, 'home/createchart.html')