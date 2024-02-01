from django.contrib import admin
from app2_hw.models import *

# Register your models here.


@admin.action(description="Обнулить количества")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    """Список продуктов."""

    list_display = ["name", "quantity"]
    list_filter = ["add_date", "price"]
    search_fields = ["description"]
    search_help_text = "Поиск по полю Описание продукта (description)"
    actions = [reset_quantity]


admin.site.register(User)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
