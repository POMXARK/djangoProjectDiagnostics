from django.db import models


class BaseModelCmn(models.Model):  # base class should subclass 'django.db.models.Model'
    id = models.IntegerField(primary_key=True)
    idobj = models.IntegerField()
    amount = models.IntegerField()
    date = models.CharField(blank=True, max_length=19)
    mode = models.FloatField()
    ai1 = models.FloatField()
    ai2 = models.FloatField()
    ai3 = models.FloatField()
    ai4 = models.FloatField()
    ai5 = models.FloatField()
    ai6 = models.FloatField()
    ai7 = models.FloatField()
    ai8 = models.FloatField()
    ai9 = models.FloatField()
    ai10 = models.FloatField()  # real_x000D_ ?

    class Meta:
        abstract = True  # Set this model as Abstract


class BaseModelAi(models.Model):
    id = models.IntegerField(primary_key=True)
    idobj = models.IntegerField()
    idai = models.IntegerField()
    datein = models.CharField(blank=True, max_length=19)
    mode = models.FloatField()
    aimax = models.FloatField()
    aimean = models.FloatField()
    aimin = models.FloatField()
    statmin = models.FloatField()
    statmax = models.FloatField()
    mlmin = models.FloatField()
    mlmax = models.FloatField()
    err = models.IntegerField()
    sts = models.IntegerField()
    dateout = models.CharField(max_length=19)
    datecheck = models.CharField(max_length=19)
    cmnt = models.CharField(max_length=50)  # cmnt / character varying (50)_x000D__x000D_ ?

    class Meta:
        abstract = True


class Obj1Cmn(BaseModelCmn):
    pass


class Obj2Cmn(BaseModelCmn):
    pass


class Obj1Ai(BaseModelAi):
    pass


class Obj2Ai(BaseModelAi):
    pass
