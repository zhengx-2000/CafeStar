from django.shortcuts import redirect, render
from django.utils.deprecation import MiddlewareMixin


# MIDDLEWARE = [''CafeStar.utils.auth.Authentication','] 在settings内加入
class Authentication(MiddlewareMixin):
    """ Middleware """

    def process_request(self, request):

        if request.path_info in ['/CafeStar/login', '/CafeStar/register','/CafeStar/homePage','/CafeStar/drinks.html','/CafeStar/homePage.html']:
            return
        # Permission verification
        userInfo = request.session.get("userInfo")
        print('userInfo',userInfo)
        if not userInfo:
            print('Intercept page : ', request.path_info)
            return render(request, "CafeStar/homePage.html")
        return

    def process_response(self, request, response):

        return response
