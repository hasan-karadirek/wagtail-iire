from django.db import models
from wagtail.core.models import Page,ParentalKey,Orderable
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import FieldPanel,InlinePanel,MultiFieldPanel,PageChooserPanel
from django_extensions.db.fields import AutoSlugField

# Create your models here.

class Menu_items(Orderable):
    
    link_title=models.CharField(max_length=50,blank=True,null=True)
    link_url=models.CharField(max_length=500,blank=True)
    link_page=models.ForeignKey("wagtailcore.Page",blank=True,null=True, related_name="+",on_delete=models.SET_NULL)

    submenu=models.ForeignKey("menus.Menu", on_delete=models.SET_NULL,blank=True,null=True)

    page=ParentalKey("menus.Menu",related_name="menu_itemss")
    panels=[
        FieldPanel("link_title"),
        FieldPanel("link_url"),
        PageChooserPanel("link_page"),
        FieldPanel("submenu")

    ]
    @property
    def title(self):
        if self.link_page and not self.link_title:
            return self.link_page.title
        elif self.link_title:
            return self.link_title
        return "Missing Title"
    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_url:
            return self.link_url
        return "#"

class Menu(ClusterableModel):
    title=models.CharField(max_length=50)
    slug=AutoSlugField(populate_from="title",editable=True)

    panels=[
        MultiFieldPanel([
            FieldPanel("title"),
            FieldPanel("slug"),
        ],heading="Menu"),
        InlinePanel("menu_itemss", label="Menu Item")
    ]
    def __str__(self):
        return self.title
