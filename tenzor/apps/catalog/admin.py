# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Category, Goods
from django.contrib import admin

# Register your models here.


class GoodsInline(admin.ModelAdmin):
    model = Goods
    list_display = ('name', 'qty', 'price', 'production_date', 'category')


class CategoryInline(admin.StackedInline):
    inlines = [
        GoodsInline
    ]

admin.site.register(Category)
admin.site.register(Goods, GoodsInline)
