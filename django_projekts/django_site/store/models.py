from django.db import models
from django.core.exceptions import ValidationError
from PIL import Image

def validate_image(image):
    try:
        img = Image.open(image)
    except Exception as e:
        raise ValidationError("Invalid image, please upload a different image")
    return None

class User(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

class Listing(models.Model):
  listingname = models.CharField(max_length=255)
  description = models.TextField(max_length=2000, default="Nav apraksta")
  listingimage = models.ImageField(upload_to='images/', validators=[validate_image], default='images/default.png')
  price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
  currency = models.CharField(max_length=255, default="EUR")
  statuscompleted = models.BooleanField(default=False)