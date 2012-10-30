from tastypie.api import Api
from tastypie.resources import ModelResource, ALL
from tastypie.authorization import Authorization
from tastypie import fields
from models import *
from master.models import *
from catalog.models import *
from django.contrib.auth.models import User
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource
class Test1Resource(ModelResource):
    class Meta:
        queryset = Test1View.objects.using('catalog').all()
        resource_name = 'test1'
        authorization = Authorization()        
#        fields = ['id', 'name']

class Test2Resource(ModelResource):
    fk = fields.ForeignKey(Test1Resource,'fk', null=True)
    class Meta:
        queryset = Test3.objects.using('catalog').all()
        resource_name = 'test2'
        authorization = Authorization()        
#        fields = ['id', 'name']

class Test4Resource(ModelResource):
    test2 = fields.ForeignKey(Test2Resource,'fk', null=False,full=True)
    class Meta:
        queryset = Test4.objects.using('catalog').all()
        allowed_methods = ['get', 'post', 'put','delete']
        resource_name = 'test4'
        authorization = Authorization()        
#        fields = ['idnum', 'fk']
    def dehydrate(self, bundle):
        print bundle
#        bundle.data['fk_id'] = bundle.data['fk'].id 
        return bundle        
