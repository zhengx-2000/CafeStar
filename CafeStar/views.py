from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from CafeStar.models import User, Order, Drink, ShopStatus
from django.views import View
from django.utils.decorators import method_decorator


def drinkDetail(request, drink_name):
    context_dict = {}
    try:
        drink = Drink.objects.get(Name=drink_name)
    except:
        drink = None

    context_dict['drink'] = drink

    return render(request, 'CafeStar/drinkDetail.html', context=context_dict)


def drinks(request):
    context_dict = {}

    drink_list = Drink.objects.all()
    context_dict['drinks'] = drink_list

    return render(request, 'CafeStar/drinks.html', context=context_dict)


def drinksModify(request):
    pass


def homePage(request):
    drink_list = Drink.objects.order_by('-Rating')[:5]

    context_dict = {}
    context_dict['drinks'] = drink_list

    return render(request, 'CafeStar/homePage.html', context=context_dict)


def newLogin(request):
    pass


def order(request, order_ID, user_ID):
    # TODO: need to get user ID and order ID here
    context_dict = {}
    if request.method == 'POST':
        drink_name = request.POST.get('drinks')
        sweetness = request.POST.get('sweetness')
        milks = request.POST.get('milks')
        pickup = request.POST.get('pickup')
        drink = Drink.objects.filter(Name=drink_name)
        drink_ID = drink.first().DrinkID
        price = drink.first().Price
        point = drink.first().Point
        order_model = Order(OrderID=order_ID,
                            UserID=user_ID,
                            DrinkID=drink_ID,
                            Status=False,
                            Drink=drink_name,
                            Sweetness=sweetness,
                            Milk=milks,
                            PickupTime=pickup,
                            Price=price,
                            Point=point)
        order_model.save()
    return render(request, 'CafeStar/order.html', context=context_dict)


def orderList(request):
    pass


def register(request):
    pass


def status(request):
    pass


def userProfile(request):
    pass


class OrderInformationView(View):
    # TODO: AJAX and JS functions not implemented
    @method_decorator(login_required)
    def get(self, request):
        if 'drinks' in request.GET:
            drink_name = request.GET['drinks']
        else:
            drink_name = ''

        drink = Drink.objects.filter(Name=drink_name)
        price = drink.first().Price
        point = drink.first().Point

        context_dict = {}
        context_dict['price'] = price
        context_dict['point'] = point

        return render(request, 'CafeStar/order.html', context=context_dict)