"""
Descripción del módulo.

Proporciona funciones y clases relacionadas con [especifica el propósito del módulo].
"""

from django.shortcuts import render, redirect
# from django.http.response import Http404
from django.views.generic.base import View
# from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from series.models import Serie, Episode


# # Create your views here.
# class HelloWorld(View):
#     """
#     Buscamos renderizar la vista 
#     """

#     def get(self, request):
#         """
#         busca el template de index.html y lo renderiza , debemos pasarle
#         el request
        
#         context : es la informacion que le pasamos a django
#         """
#         context = {
#             'items':list(range(10))
#         }
#         return render(request, 'index.html',context=context)
#         # También puedes utilizar:
#         # return HttpResponse(content=b'Hola Mundo')

class SerieView(View):
    """
    Vista de Serie
    """
    def get(self, request):
        """
        get 
        """
        if request.user.is_authenticated:
            context = {
                'series':list(Serie.objects.all())
            }
            return render(request,'series.html',context=context)
        return redirect('login')
    
# documentacion de los mixin
"""
! La siguiente clase EpisodeView(View) es igual a la 
! clase EpisodeView(LoginRequiredMixin,View)
"""

# class EpisodeView(View):
#     """
#     Vista de Serie
#     """
#     def get(self, request, serie_id : int ):
#         """
#         get 
#         """
#         if request.user.is_authenticated:    
#             context = {
#                 'episodes':list(Episode.objects.filter(serie_id=serie_id))
#             }
#             return render(request,'episodes.html',context=context)
#         return redirect('login')
"""
la siguiente clase es la clase que nos hara lo mismo que si
agregamos una condicianal dentro de la clase para ejecutar la misma
"""
class EpisodeView(LoginRequiredMixin,View):
    """
    Esta clase con el parametro LoginRequiredMixin es igual al poner
    la condicional if request.user.isatuthenticated dentro de la funcion
    """
    def get(self, request, serie_id : int ):
        """
        get 
        """          
        context = {
            'episodes':list(Episode.objects.filter(serie_id=serie_id))
        }
        return render(request,'episodes.html',context=context)
        # return redirect('login')