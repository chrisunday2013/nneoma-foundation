from django.db import models 
from django.contrib.auth.models import User
import secrets
from .paystack import PayStack



class Contact(models.Model):
    full_name=models.CharField(max_length=100, null=True)
    email=models.EmailField(max_length=100, null=True)
    subject=models.CharField(max_length=100, null=True)
    message=models.TextField(null=True)

    def __str__(self):
        return self.full_name



class Portfolio(models.Model):
    image = models.ImageField(default="default.jpg", upload_to='portfolio_pics' )
    title = models.CharField(max_length=50, null=False)

    
    def __str__(self):
        return self.title



class Team(models.Model):
    image = models.ImageField(default="default.jpg", upload_to='portfolio_pics' )
    full_name = models.CharField(max_length=100, null=False)
    position = models.CharField(max_length=50, null=False)

    
    def __str__(self):
        return self.full_name       



class Testimonial(models.Model):
    image = models.ImageField(default="default.jpg", upload_to='portfolio_pics' )
    full_name = models.CharField(max_length=100, null=False)
    heading = models.CharField(max_length=100, null=False)
    statement= models.TextField(max_length=500, null=False)

    
    def __str__(self):
        return self.full_name


class Order(models.Model):
    pass  

class DonationFlutter(models.Model):
    pass


class Payment(models.Model):
    amount = models.PositiveIntegerField()
    ref = models.CharField(max_length=200)
    email = models.EmailField()
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta: 
        ordering =('-date_created',)

    def __str__(self):
        return f"Payment: {self.amount}"    

    def save(self, *args, **kwargs):
        while not self.ref: 
            ref = secrets.token_urlsafe(50)   
            object_with_similar_ref = Payment.objects.filter(ref=ref) 
            if not object_with_similar_ref:
                self.ref = ref 
        super().save(*args, **kwargs)   

    def amount_value(self):
        return self.amount *100 

    def verify_payment(self):
        paystack = PayStack()
        status, result = paystack.verify_payment(self.ref, self.amount)
        if status:
            if result['amount'] / 100 == self.amount:
                self.verified = True
            self.save()
        if self.verified:
            return True 
        return False             



