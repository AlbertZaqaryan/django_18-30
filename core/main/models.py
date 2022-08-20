from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField('Category name', max_length=30)
    img = models.ImageField('Category Image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'



class Brand(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='catbrand')
    name = models.CharField('Brand name', max_length=30)
    img = models.ImageField('Brand Image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'


class Prod(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='prodbrand')
    name = models.CharField('Prod name', max_length=30)
    img = models.ImageField('Prod Image', upload_to='media')
    price = models.IntegerField('Prod price')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Prod'
        verbose_name_plural = 'Prods'