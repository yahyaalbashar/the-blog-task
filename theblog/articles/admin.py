from django.contrib import admin
from .models import (Article, Category)
# Register your models here.

@admin.register(Article)
class AdminArticle(admin.ModelAdmin):
    class Meta:
        model=Article
    list_display=['title','publish_date','author']
    list_filter=['publish_date','title']
    ordering=['publish_date','title']

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    class Meta:
        model=Category
    list_display=['title']
