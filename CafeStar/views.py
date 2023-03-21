from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from CafeStar.models import User, Order, Drink, ShopStatus
from django.views import View
from django.utils.decorators import method_decorator

from django import forms
from CafeStar import models
import random
from django.shortcuts import redirect


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


def status(request):
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


# log in function
def newLogin(request):
    print('in newLogin:  method ', request.method)
    if request.method == "GET":
        return render(request, "CafeStar/newLogin.html")

    userName = request.POST.get("userName")
    passWord = request.POST.get("pwd")
    userForm = models.User.objects.filter(Email=userName, Password=passWord)

    if userForm.count() > 0:

        # The website generates a random key, writes it to the user's browser cookie
        # Write user information to session for permission verification etc.
        request.session["userInfo"] = {
            'userName': userForm.first().Fullname,
            'userId': userForm.first().UserID,
            'email': userForm.first().Email,
        }

        return render(request, 'CafeStar/homePage.html')

    else:

        errMsg = "Incorrect username or password"
        return render(request, "CafeStar/newLogin.html", {"errMsg": errMsg})


# log out function
def logout(request):
    request.session.clear()
    return render(request, 'CafeStar/homePage.html')


# Generate UserModelForm from User table
class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.User

        exclude = ['Point', 'Manager', 'UserID']
        # Set the CSS style
        widgets = {
            'Fullname': forms.TextInput(attrs={'class': 'sign-txt'}),
            'Username': forms.TextInput(attrs={'class': 'sign-txt'}),
            'Email': forms.TextInput(attrs={'class': 'sign-txt'}),
            'Password': forms.TextInput(attrs={'class': 'sign-txt'}),
            'PhoneNumber': forms.TextInput(attrs={'class': 'sign-txt'}),
        }

        # Setting up error messages
        error_messages = {
            'Fullname': {'required': 'This field is required'},
            'Username': {'required': 'This field is required'},
            'Email': {'required': 'This field is required'},
            'Password': {'required': 'This field is required'},
            'PhoneNumber': {'required': 'This field is required'},
        }


# User registration function
def register(request):
    # When accessed via get method
    if request.method == "GET":
        form = UserModelForm()
        # registration jumps to register.html
        return render(request, "CafeStar/register.html", {"userModelform": form})

    # When accessed via ppst method
    # Collecting form information
    form = UserModelForm(data=request.POST)

    # Determining whether user information is legitimate
    if form.is_valid():
        # Form data is legal
        email = form.cleaned_data.get('Email')

        # select user information via email
        user = models.User.objects.filter(Email=email)

        # Determining whether an email has been registered
        if user.count() > 0:
            error = "This email address has been registered"
            return render(request, "CafeStar/register.html", {"userModelform": form, "error_msg": error})

        # Randomly generated userID
        # random_number = ''.join([str(random.randint(0, 9)) for _ in range(10)])
        # userID = int(random_number)
        # form.instance.UserId = userID

        # Save registration information
        form.save()
        user = models.User.objects.filter(Email=email).first()

        # Write to session after successful registration
        request.session["userInfo"] = {
            'userName': form.cleaned_data.get('Fullname'),
            'userId': user.UserID,
            'email': form.cleaned_data.get('Email'),
        }

        return render(request, 'CafeStar/homePage.html')

    else:

        # Illegal user information, re-collection
        return render(request, "CafeStar/register.html", {"userModelform": form})


# Edit user method
def userProfile(request):
    userId = request.session.get("userInfo")['userId']
    userForm = models.User.objects.filter(UserID=userId).first()

    if request.method == "GET":
        # When accessed via get method

        form = UserModelForm(instance=userForm)

        return render(request, "CafeStar/userProfile.html", {"userModelform": form})

    # When accessed via post method
    form = UserModelForm(data=request.POST, instance=userForm)
    # Determining whether user information is legitimate
    if form.is_valid():
        # Form data is legal
        email = form.cleaned_data.get('Email')
        oriEmail = request.session.get("userInfo").get("email")
        print("email : ", email)
        print("oriEmail : ", oriEmail)
        if not email == oriEmail:
            # select user information via email
            user = models.User.objects.filter(Email=email)

            # Determining whether an email has been registered
            if user.count() > 0:
                error = "This email address has been registered"
                return render(request, "CafeStar/userProfile.html", {"userModelform": form, "error_msg": error})

        # Save registration information
        form.save()
        # Write to session after successful registration
        request.session["userInfo"] = {
            'userName': form.cleaned_data.get('Fullname'),
            'email': form.cleaned_data.get('Email'),
        }
        error = "Saved successfully"
        return render(request, 'CafeStar/userProfile.html', {"userModelform": form, "error_msg": error})

    else:
        # Illegal user information, re-collection
        return render(request, "CafeStar/userProfile.html", {"userModelform": form})
