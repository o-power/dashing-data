from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import UserChart, BarChart

@login_required
def save_chart(request):

    chart_type = request.session.get('chart_type','')
    user_chart = UserChart(
        user_id = request.user,
        chart_type = request.session.get('chart_type',''),
        title = request.session.get('chart_title','')
    )
    user_chart.save()

    uploaded_data = request.session.get('uploaded_data', {})

    # check if empty dictionary?
    
    # should we only save user_chart when we know everything is ok with data?
    if chart_type == 'bar':
        for row in uploaded_data['chart_data']:
            bar_chart = BarChart(
                chart_id = user_chart,
                x_data = row['x_data'],
                y_data = row['y_data']
            )
            bar_chart.save()
    else:
        print('Missing bar chart')

    # clear session variable?

    #print(uploaded_data)
    #{'x_data': ['A', 'B', 'C'], 
    # 'y_data': [7, 6, 7],
    # 'bar_data': [{'x_data': 'A', 'y_data': 7},
    # {'x_data': 'B', 'y_data': 6}, 
    # {'x_data': 'C', 'y_data': 7}]}
    # need to save chart and data
    return redirect(reverse('all_charts'))
    #return render(request, 'search/savedcharts.html')

@login_required
def all_charts(request):
    charts = UserChart.objects.all().order_by('-date_created')
    return render(request, 'search/savedcharts.html', {'charts': charts})

@login_required
def do_search(request):
    charts = UserChart.objects.filter(title__icontains=request.GET['q']).order_by('-date_created')
    return render(request, 'search/savedcharts.html', {'charts': charts})