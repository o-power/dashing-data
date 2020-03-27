from django.shortcuts import render, redirect, reverse
from .forms import UploadDataForm
from django.conf import settings
from subscription.models import UserSubscription

def upload_chart(request):
    """
    A form through which the user uploads data.
    If method is POST, save data in a session object.
    If method is GET, render an empty upload data form.
    """
    
    # if the user is not logged in, redirect to login page
    if not request.user.is_authenticated:
        return redirect('{0}?next={1}'.format(settings.LOGIN_URL, request.path))
    # else if user is logged in, check subscription
    else:
        try:
            user_subscription = UserSubscription.objects.get(user_id=request.user.id)
        except UserSubscription.DoesNotExist:
            user_subscription = None
    
        # a subscription is required to create this chart type
        if user_subscription is None:
            return redirect(reverse('subscription:choose_subscription'))
        # an expired subscription
        elif user_subscription.status == 'Expired':
            return redirect(reverse('subscription:choose_subscription'))

    if request.method == 'POST':
        upload_data_form = UploadDataForm(request.POST)

        if upload_data_form.is_valid():        
            chart_title = upload_data_form.cleaned_data['chart_title']
            chart_subtitle = upload_data_form.cleaned_data['chart_subtitle']
            x_data = upload_data_form.cleaned_data['x_data'].splitlines()
            y_data = upload_data_form.cleaned_data['y_data'].splitlines()
            
            y_data = list(map(float, y_data))

            line_data = []
            for i in range(0,len(x_data),1):
                line_data.append({'x_data': x_data[i], 'y_data': y_data[i]})
            
            request.session['chart_type'] = 'line'
            request.session['chart_title'] = chart_title
            request.session['chart_subtitle'] = chart_subtitle
            request.session['chart_data'] = line_data

            return redirect(reverse('linechart:create_chart'))
    else:
        upload_data_form = UploadDataForm()

    context = {'upload_data_form': upload_data_form}
    return render(request, 'linechart/upload.html', context)

def create_chart(request):
    """
    Render page with line chart.
    """
    return render(request, 'linechart/chart.html')