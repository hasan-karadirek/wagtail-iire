from wagtail.contrib.modeladmin.options import(

    ModelAdmin,
    modeladmin_register,
    ModelAdminGroup,
)
from .models import Menu
from django.contrib import admin





class MenusAdmin(ModelAdmin):
    model=Menu
    menu_label='Menus'
    menu_icon="placeholder"
    menu_order=1
    add_to_settings_menu=False
    exclude_from_explorer=False
    list_display=("title","slug")
    search_fields=("title","slug")

modeladmin_register(MenusAdmin)

