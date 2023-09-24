from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)


class ExportData(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    year = models.IntegerField()
    export_value = models.IntegerField()
