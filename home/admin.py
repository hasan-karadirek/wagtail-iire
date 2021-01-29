from wagtail.contrib.modeladmin.options import(

    ModelAdmin,
    modeladmin_register,
    ModelAdminGroup,
)
from .models import OurTeam
from django.contrib import admin


class OurTeamAdmin(ModelAdmin):
    model=OurTeam
    menu_label='Our Team'
    menu_icon="placeholder"
    menu_order=1
    add_to_settings_menu=False
    exclude_from_explorer=False
    list_display=("name","position")
    search_fields=("name","position")

modeladmin_register(OurTeamAdmin)