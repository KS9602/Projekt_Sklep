from django.contrib import admin
from .models import ShopUser,Product,Order,Advertisement

admin.site.register(ShopUser)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Advertisement)
