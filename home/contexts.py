def uploaded_data_function(request):
    """
    Function to add chart_data to the template context.
    """
    uploaded_data = request.session.get('uploaded_data', {})

    if bool(uploaded_data):
        chart_data = uploaded_data['chart_data']
    else:
        chart_data = []

    return {'chart_data': chart_data}