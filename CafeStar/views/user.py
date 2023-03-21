from django.shortcuts import render
from django import forms
from CafeStar import models
from django.shortcuts import redirect
import random


class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.User
        # fields = '__all__'
        exclude = ['Point', 'Manager', 'UserID']


# path("user/login/", user.login),
def login(request):
    if request.method == "GET":
        return render(request, "newLogin.html")

    userName = request.POST.get("userName")
    passWord = request.POST.get("pwd")
    # inputCode = request.POST.get("inputCode")
    # sessionCode = request.session.get("image_code", "")
    # print(inputCode, " ", sessionCode)
    # if inputCode != sessionCode:
    #    return render(request, "login.html", {"errMsg": "Captcha error"})

    userForm = models.User.objects.filter(Username=userName, Password=passWord)
    print(userForm)
    if userForm.count() > 0:
        # 网站随机生成key，写到用户浏览器的cookie中，在写入到session中 {'key1':value1,'key2':value2} 也可以存json
        request.session["userInfo"] = {'userName': userForm.first().Fullname, 'userId': userForm.first().UserID}
        return redirect('/user/homePage')

    else:
        errMsg = "Incorrect username or password"
        return render(request, "newLogin.html", {"errMsg": errMsg})


# path("user/logout/", views.logout),
def logout(request):
    request.session.clear()
    return redirect('/user/login/')


# path("user/register/", user.register),
def register(request):

    if request.method == "GET":
        form = UserModelForm()
        # 注册成功跳转到DrinkList.html
        return render(request, "register.html", {"userModelform": form})

    print("request.POST : ", request.POST)

    form = UserModelForm(data=request.POST)

    if form.is_valid():
        random_number = ''.join([str(random.randint(0, 9)) for _ in range(10)])
        userID = int(random_number)
        form.instance.UserId = userID
        form.save()

        # 跳转到哪里
        return redirect('')
    else:
        print(form.errors)
        return render(request, "UserRegister.html", {"userModelform": form})


# path("user/<int:uid>/edit/", views.userEdit),
def userEdit(request, uid):
    """ toEdit """
    userForm = models.User.objects.filter(UserID=uid).first()
    if request.method == "GET":
        userForm = UserModelForm(instance=userForm)
        return render(request, "UserEdit.html", {"userModelform": userForm})

    userForm = UserModelForm(data=request.POST, instance=userForm)
    """edit"""
    if userForm.is_valid():

        userForm.save()
        return render(request, "UserEdit.html", {"userModelform": userForm})
    else:
        return render(request, "UserEdit.html", {"userModelform": userForm})
