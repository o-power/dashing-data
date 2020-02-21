from django.shortcuts import render

def create_bar_chart(request):
    """Creates bar chart"""
    return render(request, 'barchart.html')
