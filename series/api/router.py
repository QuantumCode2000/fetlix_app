from rest_framework.routers import DefaultRouter
from series.api.views import SerieApiView
router  = DefaultRouter()
#basename = es un parametro de django 
router.register(prefix='series',basename='series',viewset=SerieApiView) 