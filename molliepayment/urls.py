from django.urls import path
from . import views

urlpatterns = [
    
    path('<int:id>',views.mollie,name='mollie'),
    path('status/<int:id>',views.mollieResponse,name='mollieResponse'),
    path('thanks/<int:id>',views.thanks,name='thanks'),
]