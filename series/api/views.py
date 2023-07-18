from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from series.models import Serie
from series.api.serializers import SerieSerializer

class SerieApiView(APIView):
    def get(self, request):
        series = SerieSerializer(Serie.objects.all(),many=True)
        # series.is_valid(raise_exception=True)
        
        return Response(data=series.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        Serie.objects.create(title=request.POST['title'],description=request.POST['description'])
        return self.get(request)
    