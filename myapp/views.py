from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import User, auth 
from .models import Contact, Order, Payment, Testimonial, Portfolio, Team
from datetime import datetime
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid 
from django.urls import reverse 
from django.contrib import messages
from . import forms 
from django.views.decorators.csrf import csrf_protect,  csrf_exempt, requires_csrf_token




@requires_csrf_token
def index(request):

    n=''
    if  request.method == "POST":
        full_name= request.POST.get('full_name')
        email= request.POST.get('email')
        subject= request.POST.get('subject')
        message= request.POST.get('message')   
        contact = Contact(full_name=full_name, email=email, subject=subject, message=message)
        contact.save()
        n='Data Sent Successfully'
        redirect(index)
    testimonials=Testimonial.objects.all()
    portfolios=Portfolio.objects.all()
    teams=Team.objects.all()

    return render(request, 'index.html' , {'testimonials': testimonials, "portfolios":portfolios, "teams": teams})


@requires_csrf_token
def home(request):
    host = request.get_host()
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL, 
        'amount': '30.00', 
        'currency_code': 'USD', 
        'item_name': 'Product 1', 
        'invoice': str(uuid.uuid4()), 
        'notify_url': f'http://{host}{reverse("paypal-ipn")}',
        'return_url': f'http://{host}{reverse("paypal-return")}',
        'cancel_return': f'http://{host}{reverse("paypal-cancel")}',

    }    
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {'form':form}
    return render(request, 'home.html', context)


@requires_csrf_token
def paypal_return(request):
    messages.success(request, 'You have successfully made a donation payment!')
    return redirect('index')   


@requires_csrf_token
def paypal_cancel(request):
    messages.error(request, 'Your donation payment was cancelled.')
    return redirect('index')


@requires_csrf_token
def confirm_payment(request, pk):
    order = Order.objects.get(id=pk)
    order.completed = True 
    order.save()
    messages.success(request, "Payment made successfully")


@requires_csrf_token
def initiate_payment(request: HttpRequest) -> HttpResponse:
    if request.method == "POST": 
        payment_form = forms.PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save()
            return render(request, "make_payment.html", {'payment': payment, 'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY})
    else: 
        payment_form = forms.PaymentForm()
    return render(request, 'initiate_payment.html', {'payment_form': payment_form})            


@requires_csrf_token
def verify_payment(request: HttpRequest, ref:str) -> HttpResponse:
    payment = get_object_or_404(Payment, ref=ref)
    verified = payment.verify_payment()
    if verified:
        messages.success(request, 'Verification Successful')
    else:
        messages.error(request, 'verification Failed') 

    return redirect('/')

    




