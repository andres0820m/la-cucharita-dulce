from django.db import models


# Create your models here.

class Material(models.Model):
    name = models.TextField(null=False, blank=False)
    price_per_unit = models.FloatField(null=False, blank=False)
    paid = models.FloatField(null=False, blank=False)
    quantity = models.FloatField(null=False, blank=False)

    def __str__(self):
        return str(self.name)


class Cake(models.Model):
    name = models.TextField(null=False, blank=False)
    gain_margin = models.FloatField(null=False, blank=False)
    material = models.ManyToManyField(Material)
    price_per_unit = models.FloatField(null=True, blank=False)
    services = models.FloatField(null=True, blank=False)


class Client(models.Model):
    name = models.TextField(null=False, blank=False)
    address = models.TextField(null=False, blank=False)
    email = models.TextField(null=False, blank=True)
    phone = models.TextField(null=False, blank=True)

    def __str__(self):
        return str(self.name)


class PaidOption(models.Model):
    option = models.TextField(blank=False, null=False)

    def __str__(self):
        return str(self.option)


class Order(models.Model):
    delivery_date = models.DateField(null=False, blank=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=False, blank=False)
    delivery_address = models.TextField(blank=False, null=False)
    paid = models.ForeignKey(PaidOption, blank=False, null=False, on_delete=models.CASCADE)
