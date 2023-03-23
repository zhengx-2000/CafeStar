from django.contrib import admin

from CafeStar.models import User, Drink, Order, ShopStatus


admin.site.register(User)
admin.site.register(Drink)
admin.site.register(Order)
admin.site.register(ShopStatus)
