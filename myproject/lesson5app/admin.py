from django.contrib import admin
from .models import Good, Client, Order


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class GoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity']
    ordering = ['name']
    list_filter = ['date_add', 'price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание товара (description)'
    actions = [reset_quantity]

    """Отдельный товар."""

    readonly_fields = ['date_add', 'image']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Подробное описание товара',
                'fields': ['description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'quantity'],
            }
        ),
        (
            'Прочее',
            {
                'fields': ['date_add'],
            }
        ),
    ]


class CleintAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'address']
    ordering = ['name']
    list_filter = ['reg_date']
    search_fields = ['address']
    search_help_text = 'Поиск по адресу'

    """Отдельный клиент."""

    readonly_fields = ['reg_date']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),

        (
            'Контактная информация',
            {
                'fields': ['email', 'phone', 'address'],
            }
        ),
    ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'total', 'date_ordered']
    ordering = ['-date_ordered']
    list_filter = ['date_ordered', 'client']

    """Отдельный Заказ."""

    readonly_fields = ['date_ordered']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['client'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['total'],
            }
        ),
        (
            'Товары',
            {
                'fields': ['goods'],
            }
        ),
    ]


admin.site.register(Good, GoodAdmin)
admin.site.register(Client, CleintAdmin)
admin.site.register(Order, OrderAdmin)
