from django.shortcuts import render

def upload(request):
    """A form through which the user uploads data"""
    return render(request, "upload.html")
