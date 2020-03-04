from django.db import models
from django.utils.translation import gettext as _
from django.utils.text import slugify
from django.urls import reverse
# from django.core.urlresolvers import reverse

# Create your models here.


class Product(models.Model):
    PRDname = models.CharField(
        max_length=50, unique=True, verbose_name=_('product name'))

    # !
    PRDCategory = models.ForeignKey(
        'ProductCategory', on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('product category'))
    PRDbrand = models.ForeignKey(
        'settings.Brand', on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('product brand'))
    # !

    PRDdesc = models.TextField(
        max_length=300, verbose_name=_('product description'))
    PRDImg = models.ImageField(
        upload_to='product/', verbose_name=_('product image'), blank=True, null=True)
    PRDprice = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name=_('product price'))
    PRDdiscountprice = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name=_('discount price'), blank=True, null=True)
    PRDcost = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name=_('product cost'))
    created_date = models.DateTimeField(verbose_name=_('created at '))
    PRDslug = models.SlugField(
        blank=True, null=True, verbose_name=_('product slug'))
    PRDIsNew = models.BooleanField(
        default=True, verbose_name=_('product isNew'))
    PRDIsSeller = models.BooleanField(
        default=False, verbose_name=_('product isSeller'))

    def save(self, *args, **kwargs):
        if not self.PRDslug:
            self.PRDslug = slugify(self.PRDname)
        super(Product, self).save(*args, **kwargs)

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.PRDslug})

    def __str__(self):
        return self.PRDname


class ProductImage(models.Model):
    PRDIproductname = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name=_('product name'))
    PRDImg = models.ImageField(
        upload_to='product/', verbose_name=_('product image'))

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        return str(self.PRDIproductname)


class ProductCategory(models.Model):
    CATname = models.CharField(max_length=50, verbose_name=_('category name'))
    CATparent = models.ForeignKey('self', limit_choices_to={'CATparent__isnull': True}, on_delete=models.CASCADE, blank=True, null=True,
                                  verbose_name=_('category parent '))
    CATdesc = models.TextField(
        max_length=300, verbose_name=_('category description'))
    CATimage = models.ImageField(
        upload_to='category/', verbose_name=_('category image'))

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return str(self.CATname)


class ProductAlternative(models.Model):

    PRDALproduct = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='main_product', verbose_name=_('main product'))
    PRDALalternatives = models.ManyToManyField(
        Product, related_name='alternative_products', verbose_name=_('alternative product'))

    class Meta:

        verbose_name = 'ProductAlternative'
        verbose_name_plural = 'ProductAlternatives'

    def __str__(self):

        return str(self.PRDALproduct)


class ProductAccessories(models.Model):

    PRDACCproduct = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='mainAccessory_product', verbose_name=_('product accessory'))
    PRDACCalternatives = models.ManyToManyField(
        Product, related_name='Accessories_products', verbose_name=_('accessory alternative'))

    class Meta:

        verbose_name = 'Product Accessory'
        verbose_name_plural = 'Product Accessories'

    def __str__(self):

        return str(self.PRDACCproduct)
