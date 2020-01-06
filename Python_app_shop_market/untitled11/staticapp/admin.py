from django.contrib import admin
from staticapp.models import Category, Brand, Products
from .models import *
from cart.models import Cart

from cart.models import Item
# Register your models here.
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Products)
admin.site.register(Status)
admin.site.register(Cart)
admin.site.register(Item)
