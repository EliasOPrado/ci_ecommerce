from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.

class OrderLineAdminInline(admin.TabularInline):
    model = OrderLineItem


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, )

"""Order and OrderAdmin are models of this app """
admin.site.register(Order, OrderAdmin)
