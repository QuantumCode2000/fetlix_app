from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from series.models import Serie
from series.api.serializers import SerieSerializer
from rest_framework.viewsets import ViewSet, ModelViewSet

# class SerieApiView(APIView):
#     def get(self, request):
#         series = SerieSerializer(Serie.objects.all(),many=True)
#         # series.is_valid(raise_exception=True)
        
#         return Response(data=series.data, status=status.HTTP_200_OK)
    
#     def post(self, request):
#         serie =  SerieSerializer(data=request.POST)
#         serie.is_valid(raise_exception=True)
#         Serie.objects.create(title=serie.validated_data['title'],description = serie.validated_data['description'])
#         return self.get(request)
    
    
# utilizaremos el viewset
# los viewset son metodos que se adantan mejor a las apirest
# con metodos como list,retrieve,create
# class SerieApiView(ViewSet):
#     def list(self, request):
#         series = SerieSerializer(Serie.objects.all(),many=True)
#         return Response(data=series.data, status=status.HTTP_200_OK)
#     def retrieve(self,request, pk:int):
#         series = SerieSerializer(Serie.objects.get(pk=pk))
#         return Response(data=series.data, status=status.HTTP_200_OK)    
#     def create(self, request):
#         serie_serializer = SerieSerializer(data=request.POST)
#         serie_serializer.is_valid(raise_exception=True)
#         Serie.objects.create(title=serie_serializer.validated_data['title'], description=request.POST['description'])
#         return self.list(request)
#! este viewset debe anadirse a un router 
#! un router es un componente que es capaz de entender las peticiones al metodo que nos conviene

# ? UTILIZANDO LOS MODELVIEWSET
class SerieApiView(ModelViewSet):
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer
    
    
