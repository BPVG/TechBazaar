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
  description = models.CharField(max_length=1020)
  location = models.CharField(max_length=255)
  listingimage = models.ImageField(upload_to'images/', validators=[validate_image])
  price = models.MoneyField(max_digits=10, decimal_places=2, default_currency='EUR')
  listingowner = models.ForeignKey(User, on_delete=models.CASCADE)
  statuscompleted = models.BooleanField(default=False)