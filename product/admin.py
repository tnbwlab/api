from django.contrib import admin
from .models import Product, Owner

# Register your models here.
admin.site.register(Owner)
admin.site.register(Product)