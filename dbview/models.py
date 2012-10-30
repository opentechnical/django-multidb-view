from django.db import models

class Test1View(models.Model):
    idnum = models.AutoField(primary_key=True)
    fk_id = models.IntegerField()
    class Meta:
        db_table = 'test1_view'   
        
class Test3(models.Model):
    idnum = models.AutoField(primary_key=True)
    fk = models.ForeignKey(Test1View)
    class Meta:
        db_table = 'test2'
            
class Test4(models.Model):
    idnum = models.AutoField(primary_key=True)
    fk = models.ForeignKey(Test3)
    class Meta:
        db_table = 'test4'            
         
    

