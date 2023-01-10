from django.db import models

# Create your models here.

class Listing(models.Model):
  listingname = models.CharField(max_length=255)