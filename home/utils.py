def product_filter(request):
    filter_string = {}
    filter_mappings = {
        'search': 'name__icontains',
        'category': 'category__slug'
    }
    for key in request.GET:
        if request.GET.get(key):
            filter_string[filter_mappings[key]] = request.GET.get(key)

    return filter_string