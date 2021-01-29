from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

# Create your models here.
class Reviews(models.Model):
    name=models.CharField( max_length=70)
    company=models.CharField(max_length=50)
    comment=models.TextField(null=False,blank=False,max_length=250)
    image=models.ImageField()
    approved=models.BooleanField(default=False)
    panels = [
        FieldPanel('name'),
        FieldPanel('company'),
        FieldPanel('comment'),
        FieldPanel('approved'),
    ]
class OfferRequests(models.Model):
    services=models.CharField(max_length=50)
    name=models.CharField( max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    message=models.CharField(max_length=1000)
class ContactRequest(models.Model):
    name=models.CharField(max_length=50, null=False)
    phone=models.IntegerField(null=True)
    email=models.EmailField(null=False) 
    message=models.CharField(max_length=250,null=False)
class WorkspaceRequest(models.Model):
    name=models.CharField(max_length=50, null=False)
    email=models.EmailField(null=False) 
    phone=models.IntegerField(null=True)    
    date=models.DateField(auto_now=False, auto_now_add=False)
    price=models.IntegerField(null=True)
    createdDate=models.DateField( auto_now=True, auto_now_add=False)
    ticketImage=models.ImageField(null=True,blank=True)
    paymentId=models.CharField(max_length=1000,null=True)
    paymentStatus=models.IntegerField(default=0)
    
