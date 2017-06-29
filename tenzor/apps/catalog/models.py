from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Goods(models.Model):
    name = models.CharField(max_length=150)
    qty = models.PositiveIntegerField()
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    production_date = models.DateField()
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name
