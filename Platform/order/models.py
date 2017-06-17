from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
from cart.models import Cart

STATUS_CHOICES = (
		("Started", "Started"),
		("Finished", "Finished"),
	)
User=get_user_model()

class Order(models.Model):
    user=models.ForeignKey(User,null=True,blank=True)
    order_id = models.CharField(max_length=120, default='XYZ', unique=True)
    cart = models.ForeignKey(Cart)
    status = models.CharField(max_length=120, choices=STATUS_CHOICES, default="Started")
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    sub_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
    tax_total = models.DecimalField(default=0.00, max_digits=1000, decimal_places=2)
    final_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        app_label = 'order'
