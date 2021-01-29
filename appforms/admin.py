from django.contrib import admin
from wagtail.contrib.modeladmin.options import(

    ModelAdmin,
    modeladmin_register,
    ModelAdminGroup,
)
from .models import Reviews,OfferRequests,ContactRequest,WorkspaceRequest

class ReviewsAdmin(ModelAdmin):
    model=Reviews
    menu_label='Review'
    menu_icon="placeholder"
    menu_order=1
    add_to_settings_menu=False
    exclude_from_explorer=False
    list_display=("name","company","comment")
    search_fields=("name","company","comment")
class OfferRequestsAdmin(ModelAdmin):
    model=OfferRequests
    menu_label='Offer Requests'
    menu_icon="placeholder"
    menu_order=1
    add_to_settings_menu=False
    exclude_from_explorer=False
    list_display=("services","name","message")
    search_fields=("services","name")
class ContactRequestsAdmin(ModelAdmin):
    model=ContactRequest
    menu_label='Contact Requests'
    menu_icon="placeholder"
    menu_order=1
    add_to_settings_menu=False
    exclude_from_explorer=False
    list_display=("name","message")
    search_fields=("name")
class WorkspaceRequestsAdmin(ModelAdmin):
    model=WorkspaceRequest
    menu_label='Workspace Requests'
    menu_icon="placeholder"
    menu_order=1
    add_to_settings_menu=False
    exclude_from_explorer=False
    list_display=("name","date","paymentStatus")
    search_fields=("name","date")

modeladmin_register(ReviewsAdmin)
modeladmin_register(WorkspaceRequestsAdmin)
modeladmin_register(OfferRequestsAdmin)
modeladmin_register(ContactRequestsAdmin)