def uploaded_data_function(request):
    """
    Function to add chart_data to the template context.
    """
    chart_data = request.session.get('chart_data', [])

    return {'chart_data': chart_data}