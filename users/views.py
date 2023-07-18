"""
Views of Users App
"""
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponse
from django.views.generic.base import View


# Create your views here.

class LoginView(View):
    """
    Login
    """
    def get (self,request):
        """
        GET METHOD
        """
        return render(request,'login.html')
    def post(self,request):
        """
        POST METHOD
        """
        user = authenticate(request, username=request.POST['username'],
                            password=request.POST['password'])
        if user is not None:
            login(request, user)
            return HttpResponse(content=b'Success')
        return self.get(request)
class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return redirect('login')
        
            