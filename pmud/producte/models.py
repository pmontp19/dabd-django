from django.db import models

# Create your models here.

class ProductTemplate(models.Model):
    name = models.CharField(max_length=200)
    list_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    cost_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    salable = models.BooleanField()

    def __str__(self):
        return self.name


class ProductProduct(models.Model):
    template = models.ForeignKey(ProductTemplate, on_delete=models.CASCADE)
    code = models.CharField(max_length=200)

    def __str__(self):
        return '[' + self.code + '] ' + self.template.name
