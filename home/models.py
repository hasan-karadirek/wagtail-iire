from django.db import models
from wagtail.admin.edit_handlers import FieldPanel,InlinePanel,MultiFieldPanel,StreamFieldPanel,PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.models import Page,Orderable,ParentalKey
from wagtail.core.fields import StreamField
from streams import blocks
from appforms.models import Reviews
from appforms.forms import ReviewForm,MeetingOfferForm,AccommodationOfferForm,ContactForm,WorkspaceForm
from wagtail.contrib.settings.models import BaseSetting,register_setting
from wagtail.core.fields import RichTextField


class Slider(Orderable):
    page = ParentalKey("home.homePage", related_name="slider_images")
    title=models.CharField(max_length=150,null=True,blank=True)
    text=RichTextField()
    image=models.ForeignKey(
        "wagtailimages.Image", 
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
    )
    panels=[
        FieldPanel("title"),
        FieldPanel("text"),
        ImageChooserPanel("image"),
    ]
class OurTeam(models.Model):
    name=models.CharField(max_length=150)
    position=models.CharField(max_length=150)
    image=models.ForeignKey(
        "wagtailimages.Image", 
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    panels = [
        FieldPanel('name'),
        FieldPanel('position'),
        ImageChooserPanel("image"),
    ]

class HomePage(Page):
    templates="home/homepage.html"

    introTitle=models.CharField(max_length=100,null=True,blank=True)
    introText=RichTextField()
    reviews=Reviews.objects.filter(approved=True)
    reviewForm=ReviewForm()
    workspaceForm=WorkspaceForm()
    contactForm=ContactForm()
    meetingForm=MeetingOfferForm()
    accommodationForm=AccommodationOfferForm()
    content=StreamField([
       ("servicesR", blocks.ServiceFeaturesImgRBlock()),
       ("servicesL", blocks.ServiceFeaturesImgLBlock()),
    ],
    null=True,
    blank=True)

    content_panels=Page.content_panels+[
        MultiFieldPanel(
            [InlinePanel("slider_images",max_num=5)], heading="Slider Images"),
        MultiFieldPanel([FieldPanel("introTitle"),
        FieldPanel("introText"),], heading="Intro"),
        StreamFieldPanel("content"),
        
    
    ]
class RoutePage(Page):
    templates="home/route_page.html"

    meetingForm=MeetingOfferForm()
    accommodationForm=AccommodationOfferForm()
    contactForm=ContactForm()
    workspaceForm=WorkspaceForm()

    pageImage=models.ForeignKey(
        "wagtailimages.Image", 
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    contentTitle=models.CharField(max_length=100)
    contentText=RichTextField()
    mapEmbed=models.TextField()
    

    content_panels=Page.content_panels+[
    ImageChooserPanel("pageImage"),
    FieldPanel("contentTitle"),
    FieldPanel("contentText"),
    FieldPanel("mapEmbed"),
    ]
class AboutUsPage(Page):
    template="home/about_us.html"

    meetingForm=MeetingOfferForm()
    accommodationForm=AccommodationOfferForm()
    workspaceForm=WorkspaceForm()
    
    pageImage=models.ForeignKey(
        "wagtailimages.Image", 
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    contentTitle=models.CharField(max_length=100)
    contentText=RichTextField()
    ourTeamTitle=models.CharField(max_length=100)
    ourTeamText=RichTextField()
    ourTeam=OurTeam.objects.all()
    
    content_panels=Page.content_panels+[
    ImageChooserPanel("pageImage"),
    FieldPanel("contentTitle"),
    FieldPanel("contentText"),
    FieldPanel("ourTeamTitle"),
    FieldPanel("ourTeamText"),
    ]
@register_setting
class GeneralSettings(BaseSetting):
    site_logo=models.ForeignKey(
        "wagtailimages.Image", 
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    address=models.CharField(max_length=500)
    phone=models.CharField(max_length=20)
    email=models.CharField(max_length=100)
    wsFormHeader=models.CharField(max_length=100)
    wsFormText=models.TextField(max_length=400)
    mrFormHeader=models.CharField(max_length=100)
    mrFormText=models.TextField(max_length=400)
    acFormHeader=models.CharField(max_length=100)
    acFormText=models.TextField(max_length=400)

    panels=[
        ImageChooserPanel("site_logo"),
        FieldPanel("address"),
        FieldPanel("phone"),
        FieldPanel("email"),
        MultiFieldPanel(
            [
        FieldPanel("wsFormHeader"),
        FieldPanel("wsFormText"),
        FieldPanel("mrFormHeader"),
        FieldPanel("mrFormText"),
        FieldPanel("acFormHeader"),
        FieldPanel("acFormText"),
        ],
         heading="Form Texts"),
    ]