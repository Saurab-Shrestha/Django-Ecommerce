from django.db import models
from django.contrib.auth.models import User
from product.models import Product
#tuple
STATUS_CHOICES = (
    ('ORDERED', 'ordered'),
    ('SHIPPED', 'shipped'),
)


class Order(models.Model):

    user = models.ForeignKey(User,related_name='orders',on_delete=models.CASCADE,blank=True,null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    paid_amount = models.FloatField(blank=True, null=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="ORDERED")
    class Meta:
        ordering = ('-created_at',)

    def get_total_price(self):
        if self.paid_amount:
            return self.paid_amount
        return 0

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items",on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name="items",on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField(default=1)

    def get_total_price(self):
        return (self.quantity * self.price)