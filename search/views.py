from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def save_chart(request):
    uploaded_data = request.session.get('uploaded_data', {})
    #print(uploaded_data)
    #{'x_data': ['A', 'B', 'C'], 
    # 'y_data': [7, 6, 7],
    # 'bar_data': [{'x_data': 'A', 'y_data': 7},
    # {'x_data': 'B', 'y_data': 6}, 
    # {'x_data': 'C', 'y_data': 7}]}
    # need to save chart and data
    return render(request, "savedcharts.html")