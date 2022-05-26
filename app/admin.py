from django.contrib import admin

# Register your models here.
from app.models import Obj1Cmn, Obj2Cmn, Obj1Ai, Obj2Ai

admin.site.register(Obj1Cmn)
admin.site.register(Obj2Cmn)

admin.site.register(Obj1Ai)
admin.site.register(Obj2Ai)