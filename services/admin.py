from wagtail.contrib.modeladmin.options import(

    ModelAdmin,
    modeladmin_register,
    ModelAdminGroup,
)
from .models import Services,Tabs
from django.contrib import admin


class ServicesAdmin(ModelAdmin):
    model=Services
    menu_label='Services'
    menu_icon="placeholder"
    menu_order=1
    add_to_settings_menu=False
    exclude_from_explorer=False
    list_display=("title","text")
    search_fields=("title","text")

modeladmin_register(ServicesAdmin)
