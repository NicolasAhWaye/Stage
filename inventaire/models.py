from django.db import models


# Create your models here.
class Expiration(models.Model):
    date = models.DateField()

    def __str__(self):
        return self.date.isoformat()


class GTIN(models.Model):
    numero = models.CharField(max_length=14)
    date_expiration = models.OneToOneField(Expiration, on_delete=models.CASCADE)

    def __str__(self):
        return self.date_expiration
