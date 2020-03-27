from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import UserChart, BarChart
from subscription.models import UserSubscription

@login_required
def save_chart(request):
    """
    View that saves the chart.
    If method is POST, save the chart in the database.
    If method is GET, render a page showing all saved charts.
    """
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
            title = request.session.get('chart_title',''),
            subtitle = request.session.get('chart_subtitle','')
        )
        user_chart.save()

        chart_data = request.session.get('chart_data', [])

        # check if empty list?
        
        # should we only save user_chart when we know everything is ok with data?
        if chart_type == 'bar':
            for row in chart_data:
                bar_chart = BarChart(
                    chart_id = user_chart,
                    x_data = row['x_data'],
                    y_data = row['y_data']
                )
                bar_chart.save()
        else:
            print('Missing bar chart')

        # clear session variable?

        return redirect(reverse('search:all_charts'))
        
    return redirect(reverse('search:all_charts'))

@login_required
def all_charts(request):
    """
    View that displays all the users saved charts.
    """
    charts = UserChart.objects.filter(user_id=request.user.id).order_by('-date_created')
    return render(request, 'search/savedcharts.html', {'charts': charts})

@login_required
def do_search(request):
    """
    View that searches the saved charts by their titles.
    """
    if 'q' in request.GET:
        charts = UserChart.objects.filter(user_id=request.user.id,
                                          title__icontains=request.GET['q']).order_by('-date_created')
    else:
        return redirect(reverse('search:all_charts'))

    return render(request, 'search/savedcharts.html', {'charts': charts})

@login_required
def delete_chart(request, pk=None):
    """
    View that deletes a chart.
    """
    chart = get_object_or_404(UserChart, user_id=request.user.id, pk=pk) if pk else None
    if request.method == "POST":
        chart.delete()
        return redirect(reverse('search:all_charts'))
    
    return render(request, 'search/confirmdelete.html', {'chart': chart})