from django.shortcuts import render
from mollie.api.client import Client
from appforms.models import WorkspaceRequest
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def mollie(request,id): 
    mollie_client = Client()
    mollie_client.set_api_key('test_TQW97evcmbKSDRKhKCG4GVnJfHCkRK')
    payment = mollie_client.payments.create({
    'amount': {
        'currency': 'EUR',
        'value': '10.00'
    },
    'description': 'My first API payment',
    'redirectUrl': 'http://hasankaradirek.pythonanywhere.com/workspacepayment/mollie/thanks/{}'.format(id),
    'webhookUrl': 'http://hasankaradirek.pythonanywhere.com/workspacepayment/mollie/status/{}'.format(id),
})
    paymentId=payment.id
    ticket=WorkspaceRequest.objects.get(id=id)
    ticket.paymentId=paymentId
    ticket.save()
    return redirect(payment.checkout_url)
@csrf_exempt
def mollieResponse(request,id):
    ticket=WorkspaceRequest.objects.get(id=id)
    if request.method=="POST":

        mollie_client=Client()
        mollie_client.set_api_key('test_TQW97evcmbKSDRKhKCG4GVnJfHCkRK')

        payment = mollie_client.payments.get(ticket.paymentId)
        print(ticket.paymentStatus)
        if payment.is_paid():
            ticket.paymentStatus=1
            ticket.save()

            return 'Paid'
        elif payment.is_pending():

            return 'Pending'
        elif payment.is_open():

            return 'Open'
        else:

            return 'Cancelled'
    else:
        return render(request,'access-denied.html')
def thanks(request,id):
    ticket=WorkspaceRequest.objects.get(id=id)
    if ticket.paymentStatus==1:
        sendMail(id)

        context={'ticket':ticket}
        return render(request,'success.html',context)
    else:
        return render(request,'pendingPage.html')