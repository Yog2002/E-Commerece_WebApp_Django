from django.contrib import admin

# Register your models here.

from .models import Product  # Added Manually
admin.site.register(Product)  #Added Manually
