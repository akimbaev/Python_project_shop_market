from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'category_slug': self.slug})

    def get_products(self):
        return Products.objects.filter(category__title=self.title)
def pre_save_category_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(instance.name)
        instance.slug = slug
pre_save.connect(pre_save_category_slug, sender=Category)

class Brand(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Status(models.Model):
    name = models.CharField(max_length=24)
    def __str__(self):
        return self.name

def image_folder(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[1]
    return "{0}/{1}".format(instance.slug, filename)

class ProductManager(models.Manager):
    def all(self, *args, **kwargs):
        return super(ProductManager, self).get_queryset().filter(available=True)

class Products(models.Model):
    category = models.ForeignKey(Category, on_delete='')
    brand = models.ForeignKey(Brand, on_delete='')
    image = models.ImageField(upload_to='profile_image', blank=True,)
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    available = models.BooleanField(default=True)
    objects =  ProductManager()
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'product_slug': self.slug})
