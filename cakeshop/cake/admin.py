from django.contrib import admin
from .models import *

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display=['id','name','phone','email','desc']

admin.site.register(Contact,ContactAdmin)
admin.site.register(order)

class CakesAdmin(admin.ModelAdmin):
    list_display2=['id','name','price','stock' 'image_url   ']
admin.site.register(Cakes,CakesAdmin)