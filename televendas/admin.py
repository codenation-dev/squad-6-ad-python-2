from django.contrib import admin

# Register your models here.
from .models import Seller, ComissionPlan, Sale
admin.site.register([Seller, ComissionPlan, Sale])