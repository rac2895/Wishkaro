from django.conf.urls import *


urlpatterns = patterns('products.views',
	url(r'^$', "index"),
	url(r'^category/(?P<category_slug>[-\w]+)/$', 'show_category', {'template_name':'category.html'},'category_detail'),
	url(r'^product/(?P<product_slug>[-\w]+)/$', 'show_product', {'template_name':'product.html'},'product_detail'),
)