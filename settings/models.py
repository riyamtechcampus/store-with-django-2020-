from django.db import models
from django.utils.translation import gettext as _

# Create your models here.


class Brand(models.Model):
    """Model definition for Brand."""
    BRDname = models.CharField(
        max_length=50, verbose_name=_('brand name'))
    BRDdesc = models.TextField(
        max_length=200, verbose_name=_('brand description '))

    # TODO: Define fields here

    class Meta:
        """Meta definition for Brand."""

        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        """Unicode representation of Brand."""
        return str(self.BRDname)


class Varient(models.Model):
    """Model definition for Varient."""
    VARname = models.CharField(
        max_length=50, verbose_name=_('varient name'))
    VARdesc = models.TextField(
        max_length=200, verbose_name=_('varient description'))

    # TODO: Define fields here

    class Meta:
        """Meta definition for Varient."""

        verbose_name = 'Varient'
        verbose_name_plural = 'Varients'

    def __str__(self):
        """Unicode representation of Varient."""
        return str(self.VARname)
