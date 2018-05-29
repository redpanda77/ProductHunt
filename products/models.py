from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):

    name        = models.CharField(max_length=255)
    product_id  = models.CharField(max_length=255)
    pub_date    = models.DateTimeField()
    body        = models.TextField()
    address     = models.TextField()
    rating      = models.CharField(max_length=255)
    categories  = models.TextField()
    coordinates = models.TextField()
    url         = models.TextField()
    image       = models.ImageField(upload_to='images/', blank=True, null=True)
    icon        = models.ImageField(upload_to='images/', blank=True, null=True)

    votes_total = models.IntegerField(default=1)
    hunter      = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')