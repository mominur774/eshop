from django.urls import path
from home import views


urlpatterns = [
    path('', views.home, name='index'),
    path('<str:slug>/', views.CategoryProductView.as_view(), name="category_product")
]
