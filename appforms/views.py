from django.shortcuts import render,redirect
from .forms import ReviewForm,MeetingOfferForm,AccommodationOfferForm,ContactForm,WorkspaceForm

# Create your views here.
def formpost(request):
    if request.method=="POST" and request.POST["id"]:
        if request.POST["id"]=="review":
            form=ReviewForm(request.POST,request.FILES)
            
            s=form.save()
            return redirect("/")
        if request.POST["id"]=="meeting":
            form=MeetingOfferForm(request.POST)
            s=form.save()
            return redirect("/")
        if request.POST["id"]=="accommodation":
            form=AccommodationOfferForm(request.POST)
            s=form.save()
            return redirect("/")
        if request.POST["id"]=="contact":
            form=ContactForm(request.POST)
            s=form.save()
            return redirect("/")
        if request.POST["id"]=="workspace":
            form=WorkspaceForm(request.POST)
            s=form.save()
            return render(request,"appForms/checkout.html",{"form":s})