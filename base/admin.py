from django.contrib import admin
from . models import Category, Photo

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']
admin.site.register(Category, CategoryAdmin)

class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'image', 'description']
admin.site.register(Photo, PhotoAdmin)
