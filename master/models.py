from django.db import models

class Test1(models.Model):
    idnum = models.AutoField(primary_key=True)
    fk_id = models.IntegerField()
    fk_id2 = models.IntegerField()
    class Meta:
        db_table = 'test1'    
    

