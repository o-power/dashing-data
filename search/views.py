from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
#from .models import UserChart, BarChart

@login_required
def save_chart(request):
    #user = request.user

    print(request.session.get('chart_type',''))
    #user_chart = UserChart(
    #                user_id = ,
    #                chart_type = ,
    #                title = 
    #            )
    #user_chart.save()

    uploaded_data = request.session.get('uploaded_data', {})

    #if bar chart
    for row in uploaded_data['bar_data']:
        print(row)
        print(row['x_data'])
        print(row['y_data'])
        #bar_chart = BarChart(
        #            chart_id = user_chart,
        #            x_data = row['x_data']
        #            y_data = row['y_data']
        #        )
        #bar_chart.save()

    #print(uploaded_data)
    #{'x_data': ['A', 'B', 'C'], 
    # 'y_data': [7, 6, 7],
    # 'bar_data': [{'x_data': 'A', 'y_data': 7},
    # {'x_data': 'B', 'y_data': 6}, 
    # {'x_data': 'C', 'y_data': 7}]}
    # need to save chart and data
    return render(request, "savedcharts.html")