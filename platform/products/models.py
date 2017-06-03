
from django.db import models
from django.db.models.signals import post_save
from django.core.urlresolvers import reverse



class Category(models.Model):
	name = models.CharField(max_length=50)
	slug = models.SlugField(max_length=50, unique=True)
	description = models.TextField()
	is_active = models.BooleanField(default=True)

	
	meta_description = models.CharField("Meta Description", max_length=255)
	meta_keywords = models.CharField(max_length=255, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	class Meta:
		db_table = 'categories'
		ordering = ['-created_at']
		verbose_name_plural = 'Categories'
	def __unicode__(self):
		return self.name


	@models.permalink
	def get_absolute_url(self):
		return ('category_detail', (), { 'category_slug': self.slug })	




class Product(models.Model):
    title = models.CharField(max_length=120,default='')
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    brand = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=9,decimal_places=2)
    old_price = models.DecimalField(max_digits=9,decimal_places=2, blank=True,default=0.00)
    image = models.ImageField(upload_to="images/products")
    is_active = models.BooleanField(default=True)
    is_bestseller = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    quantity = models.IntegerField()
    description = models.TextField()
    meta_keywords = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)
    class Meta:
        db_table = 'products'
        ordering = ['-created_at']


    def __unicode__(self):
        return self.name
    @models.permalink
    def get_absolute_url(self):
        return ('product_detail', (), { 'product_slug': self.slug })
    def sale_price(self):
        if self.old_price > self.price:
            return self.price
        else:
            return None








class VariationManager(models.Manager):
	def all(self):
		return super(VariationManager, self).filter(active=True)

	def sizes(self):
		return self.all().filter(category='size')

	def colors(self):
		return self.all().filter(category='color')


VAR_CATEGORIES = (
	('size', 'size'),
	('color', 'color'),
	)


class Variation(models.Model):
	product = models.ForeignKey(Product)
	category = models.CharField(max_length=120, choices=VAR_CATEGORIES, default='size')
	title = models.CharField(max_length=120)
	price = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)

	objects = VariationManager()

	def __unicode__(self):
		return self.title























class CoverImage(models.Model):
	image=models.ImageField(upload_to="images/ritu")

	



