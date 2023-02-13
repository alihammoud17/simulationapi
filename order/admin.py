from django.contrib import admin
from .models import Order, OrderLine, Status

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    # def has_add_permission(self, request, obj=None) -> bool:
    #     return False

    # def has_change_permission(self, request, obj = None) -> bool:
    #     return True
    def get_user_email(self, obj):
        return obj.user.email

    
    list_display=('get_user_email', 'orderDate', 'shippingDate')

class OrderLineAdmin(admin.ModelAdmin):

    def getTotalPrice(self, obj):
        return obj.unitPrice * obj.quantity
    getTotalPrice.short_description = 'Total Price'


    def get_order_username(self, obj):
        return obj.orderID.user.username

    get_order_username.short_description = 'Client Username'

    def get_order_date(self, obj):
        return obj.orderID.orderDate

    def get_shippingdate(self, obj):
        return obj.orderID.shippingDate


    list_display = (
        'orderID',
        'quantity',
        'unitPrice',
        'getTotalPrice',
        'get_order_username',
        'get_order_date',
        'get_shippingdate'
    )

    # list_editable = ('get_shippingdate', )



admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine, OrderLineAdmin)
admin.site.register(Status)