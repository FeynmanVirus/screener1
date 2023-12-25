from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager
from django.conf import settings
from datetime import date, timedelta

# Create your models here.
class User(AbstractUser):
    email = models.EmailField("email address", unique=True)
    subscription_valid = models.DateField(default=(date.today() - timedelta(1))) 
    USERNAME_FIELD = "email" # make the user log in with the email
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    @property
    def subscribed(self):
        if (date.today() - self.subscription_valid) < timedelta(0):
            return True
        return False


class Transactions(models.Model):
    made_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='transactions')
    made_on = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    checksum = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.order_id is None and self.made_on and self.id:
            self.order_id = self.made_on.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)        

class Screener(models.Model):
    title = models.CharField(max_length=100)
    nifty_clause = models.CharField(max_length=1000, default='')
    future_clause = models.CharField(max_length=1000, default='')
    cash_clause = models.CharField(max_length=1000, default='')