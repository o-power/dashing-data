from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def save_chart(request):
    uploaded_data = request.session.get('uploaded_data', {})
    # need to save chart and data
    return render(request, "savedcharts.html")