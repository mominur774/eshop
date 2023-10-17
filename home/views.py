from django.shortcuts import render
from django.views.generic import ListView, DetailView
from product.models import Product, Category

# Create your views here.


def home(request):
    return render(request, 'pages/index.html')


class CategoryProductView(DetailView):
    model = Product
    template_name = 'pages/category-product.html'
    slug_field = 'slug'
    context_object_name = 'products'

    def get_object(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['category'] = Category.objects.get(slug=self.kwargs['slug'])
        return context