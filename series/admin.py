from django.contrib import admin
# from django.contrib.admin import ModelAdmin
from series.models import Serie,Episode
# from django.contrib.admin.decorators import register
# Register your models here.
# class SeriesAdmin(ModelAdmin):
#     pass

admin.site.register(Serie)
admin.site.register(Episode)


# @register(Episode)
# class EpidoseAdmin(ModelAdmin):
#     pass