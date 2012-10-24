from django.db import models
from master.models import Test1

class Test2(models.Model):
    idnum = models.AutoField(primary_key=True)
    fk = models.ForeignKey(Test1)
    class Meta:
        db_table = 'test2'    

