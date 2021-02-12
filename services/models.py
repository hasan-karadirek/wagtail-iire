from django.db import models
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import FieldPanel,InlinePanel,MultiFieldPanel,StreamFieldPanel
from wagtail.core.models import Page,ParentalKey,Orderable
from modelcluster.models import ClusterableModel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtailmodelchooser import register_model_chooser
from wagtailmodelchooser.edit_handlers import ModelChooserPanel
from django.utils.text import slugify
from streams.blocks import RichTextBlock
from wagtail.core.fields import StreamField
from appforms.models import Reviews
from appforms.forms import MeetingOfferForm,AccommodationOfferForm,WorkspaceForm 
from wagtail.core.fields import RichTextField


def get_unique_slug(self):
    slug = slugify(self.title)
    unique_slug = slug
    num = 1
    while Services.objects.filter(slug=unique_slug).exists() and Services.objects.get(slug=unique_slug) != self:
        unique_slug = '{}-{}'.format(slug, num)
        num += 1
    return unique_slug
# Create your models here.

@register_model_chooser
class Services(ClusterableModel):
    
    title=models.CharField(max_length=100,null=False,blank=False)
    text=RichTextField()
    slug=models.CharField(max_length=250)
    panels = [
        FieldPanel('title'),
        FieldPanel('text'),
        MultiFieldPanel([InlinePanel('service_tabs') 
    ], heading="Service Tabs"),
    ]
    def getTabs(self):
        tabs=Tabs.objects.filter(page_id=self.id)
        return tabs
    
    def save(self):
        self.slug=get_unique_slug(self)
        super().save()
    def __str__(self):
        return str(self.title)
        

class Tabs(Orderable):
    page = ParentalKey("services.Services", related_name="service_tabs")
    title=models.CharField(max_length=50,null=True,blank=True)
    text=RichTextField()
    detailText=RichTextField()
    image=models.ForeignKey(
        "wagtailimages.Image", 
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
    )

    panels=[
        FieldPanel("title"),
        FieldPanel("text"),
        FieldPanel("detailText"),
        ImageChooserPanel("image"),
    ]
class ServiceDetail(Page):
    templates="services/service_detail.html"

    meetingForm=MeetingOfferForm()
    accommodationForm=AccommodationOfferForm()
    reviews=Reviews.objects.filter(approved=True)
    workspaceForm=WorkspaceForm()

    pageImage=models.ForeignKey(
        "wagtailimages.Image", 
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
    )
    pageText=RichTextField()
    service=models.ForeignKey("services.Services", verbose_name=("verb"), on_delete=models.PROTECT)
    content=StreamField([
        ("content", RichTextBlock()),
    ],
    null=True,
    blank=True)
    content_panels=Page.content_panels+[
        ImageChooserPanel("pageImage"),
        FieldPanel('pageText'),
        ModelChooserPanel("service"),
        StreamFieldPanel("content")

    ]
    def clean(self):
        super().clean()
        self.slug=self.service.slug
    
        

    