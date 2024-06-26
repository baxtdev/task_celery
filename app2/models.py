from django.db import models

# Create your models here.


class Bid(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField( max_length=254)
    review = models.TextField()

    def __str__(self) -> str:
        return self.name