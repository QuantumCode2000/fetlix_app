"""
URL configuration for fetlix_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
# from series.views import HelloWorld
from series.views import SerieView,EpisodeView
from users.views import LoginView, LogoutView
from series.api.views import SerieApiView
from series.api.router import router

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',HelloWorld.as_view())
    path('series/',SerieView.as_view()),
    path('episodes/<int:serie_id>',EpisodeView.as_view(),name='episodes'),
    path('login/' ,LoginView.as_view(),name='login'),
    path('logout/' ,LogoutView.as_view(),name='logout'),
    # include inclue las vistas del router de router.py
    path('docs/',include_docs_urls(title="Mi titulo!!",public=False)),
    path('api/',include(router.urls))

]
