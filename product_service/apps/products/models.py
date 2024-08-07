from django.db import models
from django.utils.translation import (
    gettext_lazy as _,
)

# Create your models here.


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name=_("Name"),
    )
    description = models.TextField(
        verbose_name=_("Description")
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Price"),
    )
    stock = models.IntegerField(
        verbose_name=_("Stock"),
    )

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name
