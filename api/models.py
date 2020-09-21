from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Destination(models.Model):
    name = models.CharField(max_length=18)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Offer(models.Model):
    offer_id = models.CharField(primary_key=True, unique=True, max_length=50)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='destination')
    old_price = models.IntegerField(validators=[MinValueValidator(0)])
    current_price = models.IntegerField(validators=[MaxValueValidator(old_price)])
    rank = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(6.0)])
    link = models.URLField(max_length=200)
    # photo = models.URLField(max_length=200)
    # date = models.DateTimeField()

    def __str__(self):
        return '{} {}'.format(self.offer_id, self.destination)
