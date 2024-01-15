from django.contrib import admin
from .models import blog
# Register your models here.
@admin.register(blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=['id','title','dis']
