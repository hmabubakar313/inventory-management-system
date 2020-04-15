from django.contrib import admin
from . models import *
# Register your models here.


@admin.register(Desktops, Mobiles, Laptops) 
class ViewAdmin(admin.ModelAdmin):
    pass

