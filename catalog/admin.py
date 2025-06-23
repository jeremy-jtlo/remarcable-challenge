from django.contrib import admin
from .models import Category, Tag, Item

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category', 'tags')
    search_fields = ('name', 'description')