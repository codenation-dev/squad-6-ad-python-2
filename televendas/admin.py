from django.contrib import admin
from televendas.models.comission_plan import ComissionPlan
from televendas.models.seller import Seller
from televendas.models.sale import Sale

admin.site.register([Seller, ComissionPlan, Sale])
