from adminsortable.admin import SortableAdmin
from django.contrib import admin

from .models import Banner


@admin.register(Banner)
class FoodCategoryAdmin(SortableAdmin):
    list_display = ['heading', ]
    fields = ['image', 'heading', 'subheading', ]
