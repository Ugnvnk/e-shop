from django.contrib import admin
from django.contrib.admin import ModelAdmin
from mptt.admin import MPTTModelAdmin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import *

class CategoryAdmin(ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    fields = ('name', 'parent', 'slug')
class ProductAdmin(ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

    list_display = ('name', 'category', 'photo', 'slug', 'brand', 'description', 'price', 'created_at')
    list_display_links = ('name',)
    search_fields = ('name', 'category__name', 'brand')


admin.site.register(User)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Order)
admin.site.register(OrderItems)
admin.site.register(Customer)
admin.site.register(Product, ProductAdmin)


