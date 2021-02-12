from django import forms
from .models import Reviews,OfferRequests,ContactRequest,WorkspaceRequest
from .widgets import BootstrapDateTimePickerInput
from wagtail.images.models import Image

class ReviewForm(forms.ModelForm):
    name=forms.CharField(max_length=70, required=True,label="Your Name",widget=forms.TextInput(attrs={"cols":4,"class":"form-control-input"}))
    company=forms.CharField(max_length=50, required=True,label="Company",widget=forms.TextInput(attrs={"cols":4,"class":"form-control-input"}))
    comment=forms.CharField(required=True,label="Your Review",widget=forms.Textarea(attrs={"cols":7, "rows":5,"class":"form-control-input"}))
    image=forms.ImageField(required=False,widget=forms.FileInput(attrs={"class":"form-control-file"}))
    class Meta:
        model = Reviews
        fields = ['name', 'company','comment']
    def save(self, commit=False):
        instance = super(ReviewForm, self).save(commit=False)
        avatar_image = Image.objects.create(
            file=self.cleaned_data['image'],
            title=self.cleaned_data['image'],   
        )
        instance.avatar_image = avatar_image
        instance.save()
        return instance

class MeetingOfferForm(forms.ModelForm):
    services=forms.CharField( max_length=50, required=True,label="Your Name", widget=forms.TextInput(attrs={'type':'hidden','value':'Meeting Room'}))
    name=forms.CharField( max_length=50, required=True,label="Your Name", widget=forms.TextInput(attrs={}))
    email=forms.EmailField(required=True,label="Email",widget=forms.TextInput(attrs={}))
    phone=forms.CharField(max_length=15,  required=True,label="Phone Number",widget=forms.TextInput(attrs={}))
    message=forms.CharField(required=True,label="Anything you would like to add or ask?", widget=forms.Textarea(attrs={'cols':40, 'rows': 4, }))
    class Meta:
        model = OfferRequests
        fields = [ 'services','name','email', 'phone', 'message']
class AccommodationOfferForm(forms.ModelForm):
    services=forms.CharField( max_length=50, required=True,label="Your Name", widget=forms.TextInput(attrs={'type':'hidden','value':'Accommodation'}))
    name=forms.CharField( max_length=50, required=True,label="Your Name", widget=forms.TextInput(attrs={}))
    email=forms.EmailField(required=True,label="Email",widget=forms.TextInput(attrs={}))
    phone=forms.CharField(max_length=15,  required=True,label="Phone Number",widget=forms.TextInput(attrs={}))
    message=forms.CharField(required=True,label="Anything you would like to add or ask?", widget=forms.Textarea(attrs={'cols':40, 'rows': 4, }))
    class Meta:
        model = OfferRequests
        fields = [ 'services','name','email', 'phone', 'message']
class ContactForm(forms.ModelForm):
    name=forms.CharField(max_length=50, required=True, label="Name",widget=forms.TextInput(attrs={"class":"form-control-input"}))
    phone=forms.IntegerField(required=False, label="Phone",widget=forms.TextInput(attrs={"class":"form-control-input"}))
    email=forms.EmailField(required=True, label="Email",widget=forms.EmailInput(attrs={"class":"form-control-input"}))
    message=forms.CharField(required=True, widget=forms.Textarea(attrs={"class":"form-control-input"}))
    class Meta:
        model = ContactRequest 
        fields = ['name', 'phone','email', 'message']
class WorkspaceForm(forms.ModelForm):
    name=forms.CharField( max_length=50, required=True,label="Your Name", widget=forms.TextInput(attrs={"class":"workspace-form-input"}))
    email=forms.EmailField(required=True,label="Email",widget=forms.TextInput(attrs={"class":"workspace-form-input"}))
    phone=forms.CharField(max_length=15,  required=True,label="Phone Number",widget=forms.TextInput(attrs={"class":"workspace-form-input"}))
    date=forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"workspace-form-input","id":"flatpickr"}))
    class Meta:
        model = WorkspaceRequest
        fields = [ 'name','email', 'phone', 'date']
    def clean(self):
        name=self.cleaned_data.get("name")
        email=self.cleaned_data.get("email")
        phone=self.cleaned_data.get("phone")
        date=self.cleaned_data.get("date")
        values={
            'name':name,
            'phone':phone,
            'email':email,
            'date':date,
        }
        return values