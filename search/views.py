from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import UserChart, BarChart
from subscription.models import UserSubscription

@login_required
def save_chart(request):

    try:
        user_subscription = UserSubscription.objects.get(user_id=request.user.id)
    except UserSubscription.DoesNotExist:
        user_subscription = None
    
    # a subscription is required to save charts
    if user_subscription is None:
        return redirect(reverse('subscription:choose_subscription'))
    # an expired subscription
    elif user_subscription.status == 'Expired':
        return redirect(reverse('subscription:choose_subscription'))

    if request.method == "POST":

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

        # clear session variable? otherwise will save again if we go to search/save/

        #print(uploaded_data)
        #{'x_data': ['A', 'B', 'C'], 
        # 'y_data': [7, 6, 7],
        # 'bar_data': [{'x_data': 'A', 'y_data': 7},
        # {'x_data': 'B', 'y_data': 6}, 
        # {'x_data': 'C', 'y_data': 7}]}
        # need to save chart and data

        return redirect(reverse('search:all_charts'))
        
    # GET go to here
    return redirect(reverse('search:all_charts'))
    


@login_required
def all_charts(request):
    charts = UserChart.objects.filter(user_id=request.user.id).order_by('-date_created')
    return render(request, 'search/savedcharts.html', {'charts': charts})

@login_required
def do_search(request):

    if 'q' in request.GET:
        charts = UserChart.objects.filter(user_id=request.user.id,
                                          title__icontains=request.GET['q']).order_by('-date_created')
    else:
        return redirect(reverse('search:all_charts'))

    return render(request, 'search/savedcharts.html', {'charts': charts})

@login_required
def delete_chart(request, pk=None):
    chart = get_object_or_404(UserChart, user_id=request.user.id, pk=pk) if pk else None
    if request.method == "POST":
        chart.delete()
        return redirect(reverse('search:all_charts'))
    
    return render(request, 'search/confirmdelete.html', {'chart': chart})
