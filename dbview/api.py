from tastypie.api import Api
from tastypie.resources import ModelResource, ALL
from models import *

class Test1Resource(ModelResource):
    class Meta:
        queryset = Test1View.objects.using('catalog').all()
        resource_name = 'test1'
#        fields = ['id', 'name']

class Test2Resource(ModelResource):
    class Meta:
        queryset = Test3.objects.using('catalog').all()
        resource_name = 'test2'
#        fields = ['id', 'name']
