from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import UserChart, BarChart, LineChart
from subscription.models import UserSubscription
from django.contrib import messages

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

        if chart_type == 'bar':
            for row in chart_data:
                bar_chart = BarChart(
                    chart_id = user_chart,
                    x_data = row['x_data'],
                    y_data = row['y_data']
                )
                bar_chart.save()
        elif chart_type == 'line':
            for row in chart_data:
                line_chart = LineChart(
                    chart_id = user_chart,
                    date_format = request.session.get('date_format',''),
                    x_data = row['x_data'],
                    y_data = row['y_data']
                )
                line_chart.save()
        else:
            messages.error(request, 'Unable to save chart.')

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

@login_required
def load_chart(request, pk=None):
    """
    Render page with saved bar chart
    """
    chart = get_object_or_404(UserChart, user_id=request.user.id, pk=pk) if pk else None
        
    if chart.chart_type == 'bar':
        bar_chart = BarChart.objects.filter(chart_id=pk) if pk else None
        if bar_chart:
            bar_data = []
            for row in bar_chart:
                bar_data.append({'x_data': row.x_data, 'y_data': float(row.y_data)})

            request.session['chart_type'] = chart.chart_type
            request.session['chart_title'] = chart.title
            request.session['chart_subtitle'] = chart.subtitle
            request.session['chart_data'] = bar_data

            return redirect(reverse('barchart:view_chart', kwargs={'pk': pk}))
    elif chart.chart_type == 'line':
        line_chart = LineChart.objects.filter(chart_id=pk) if pk else None
        if line_chart:
            line_data = []
            for row in line_chart:
                line_data.append({'x_data': row.x_data, 'y_data': float(row.y_data)})
            
            request.session['chart_type'] = chart.chart_type
            request.session['chart_title'] = chart.title
            request.session['chart_subtitle'] = chart.subtitle
            request.session['date_format'] = line_chart[0].date_format
            request.session['chart_data'] = line_data

            return redirect(reverse('linechart:view_chart', kwargs={'pk': pk}))

    messages.error(request, 'Unable to load chart.')
    return redirect(reverse('search:all_charts'))