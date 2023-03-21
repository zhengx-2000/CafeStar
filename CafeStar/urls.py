from django.urls import path
from CafeStar import views

app_name = 'CafeStar'

urlpatterns = [
    path('', views.homePage, name='home_page'),
    path('drinkDetail', views.drinkDetail, name='drink_detail'),
    path('drinks', views.drinks, name='drinks'),
    path('order', views.order, name='order'),
    path('orderPricePoint', views.OrderInformationView.as_view(), name='order_price_point'),
]