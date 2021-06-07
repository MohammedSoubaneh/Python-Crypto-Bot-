from django.db import models


class BinanceKey(models.Model):

    api = models.CharField(max_length=65)
    secret = models.CharField(max_length=65)

    def __str__(self):
        return self
    

class Orders(models.Model):

    symbol = models.CharField(max_length=65)
    side = models.CharField(max_length=5)
    quantity = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.symbol

class Currency(models.Model):
    name = models.CharField(max_length=65)
    symbol = models.CharField(max_length=10)
    position = models.IntegerField(db_index=True, default=0)

    def __str__(self):
        return self.name


