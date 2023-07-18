from rest_framework import serializers
from series.models import Serie
from rest_framework.exceptions import ValidationError
from typing import Dict
# class SerieSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField()
#     description = serializers.CharField()


# Model serializers
class SerieSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    def validate(self, serie:Dict[str,str]):
        if not serie.get('title'):
            raise ValidationError('title is madatory')
        return serie

    class Meta :
        model = Serie
        fields = ('__all__')
# #normal serializers
# class SerieSerializer(serializers.Serializer):
#     title = serializers.CharField(required=True)
#     description = serializers.CharField(required=True)
#     id = serializers.IntegerField(read_only=True)

#     def validate_title(self, title: str):
#         series = Serie.objects.filter(title=title)
#         if series.exists():
#             raise ValidationError('The title already exists')
#         return title

#     def validate_description(self, description: str):
#         if not description:
#             raise ValidationError('The description cannot be blank')
#         return description