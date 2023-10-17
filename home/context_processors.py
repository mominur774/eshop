from product.models import Category



def shop_context(request):
    return {
        'categories': Category.objects.all()
    }