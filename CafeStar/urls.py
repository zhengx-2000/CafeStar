from django.urls import path
from CafeStar import views

app_name = 'CafeStar'

urlpatterns = [
    path('', views.homePage, name='home_page'),
    path('homePage', views.homePage, name='home_page'),
    path('drinkDetail', views.drinkDetail, name='drink_detail'),
    path('drinks', views.drinks, name='drinks'),
    path('order', views.order, name='order'),
    path('orderPricePoint', views.OrderInformationView.as_view(), name='order_price_point'),
    path('login', views.newLogin, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('edit', views.userProfile, name='edit'),
    path('orderList', views.orderList, name='order_list'),
    path('shopStatus', views.status, name='shop_status'),
    path('drinksModify', views.drinksModify, name='drinks_modify'),
]
