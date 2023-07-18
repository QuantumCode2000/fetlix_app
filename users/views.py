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
        # del form del html le pasamos los datos usando una funcion de django users
        user = authenticate(request, username=request.POST['username'],
                            password=request.POST['password'])
        if user is not None:
            login(request, user)
            return HttpResponse(content=b'Success')
        return self.get(request)
class LogoutView(View):
    """
    Clase logout para deslogear un usuario en django user
    """
    def get(self, request):
        """
        Pasamos el request que tiene el usuario y si esta autenticado lo saca 
        y si no ,redirecciona a login
        """
        if request.user.is_authenticated:
            logout(request)
            return redirect('login')
