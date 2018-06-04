from django.db import models
from django.contrib.auth.models import User
from products.models import Product
# Create your models here.

class Post(models.Model):

    pub_date    = models.DateTimeField()
    type        = models.CharField(max_length=255, default='vote')
    product     = models.ForeignKey(Product, on_delete=models.CASCADE)
    hunter      = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
# Create your models here.
