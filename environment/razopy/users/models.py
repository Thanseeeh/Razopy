from django.apps import apps
from django.db import models

def get_account_model():
    return apps.get_model('accounts', 'Account')

class Token(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.TextField()
    price = models.FloatField()
    brand = models.CharField(max_length=100, null=True)
    image = models.ImageField(null=True, blank=True)
    owner = models.ForeignKey('accounts.Account', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name