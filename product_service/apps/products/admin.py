from django.contrib import admin

from apps.products.models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    fields = (
        "name",
        "description",
        "price",
        "stock",
    )

    list_display = (
        "name",
    )


admin.site.register(Product, ProductAdmin)
