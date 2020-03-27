def uploaded_data_function(request):
    """
    Function to add chart_data to the template context.
    """
    chart_title = request.session.get('chart_title', '')
    chart_subtitle = request.session.get('chart_subtitle', '')
    chart_data = request.session.get('chart_data', [])

    return {'chart_title': chart_title,
            'chart_subtitle': chart_subtitle,
            'chart_data': chart_data}