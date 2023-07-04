from django.db import models

class Transaction(models.Model):
    timestamp = models.DateTimeField()
    product_name = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    seller = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.timestamp} - {self.product_name} - {self.value} - {self.seller}'
