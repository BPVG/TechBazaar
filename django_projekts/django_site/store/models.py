from django.db import models
from django.core.exceptions import ValidationError
from PIL import Image
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import Group, Permission

def validate_image(image):
    try:
        img = Image.open(image)
    except Exception as e:
        raise ValidationError("Invalid image, please upload a different image")
    return None

class Listing(models.Model):
  listingname = models.CharField(max_length=255)
  description = models.TextField(max_length=2000, default="Nav apraksta")
  listingimage = models.ImageField(upload_to='images/', validators=[validate_image], default='images/default.png')
  price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
  currency = models.CharField(max_length=255, default="EUR")
  statuscompleted = models.BooleanField(default=False)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, related_name='users', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='users', blank=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'

    
    groups = models.ManyToManyField(Group, related_name='store_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='store_user_set', blank=True)

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admin')

class Guest(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='guest')
