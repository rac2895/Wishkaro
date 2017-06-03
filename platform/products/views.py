from django.shortcuts import get_object_or_404, render_to_response
from .models import Category, Product,CoverImage
from django.template import RequestContext
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from products.forms import ProductAddToCartForm
from cart.views import *
from django.db.models import Q


def home(request):
    return render_to_response("base.html",{},context_instance=RequestContext(request))

def index(request):
    images=CoverImage.objects.all()
    product=Product.objects.all()
    count=len(product)

    return render_to_response("index.html", {'product':product,'images':images,'count':count},context_instance=RequestContext(request))

def show_category(request, category_slug, template_name="category.html"):
    c = get_object_or_404(Category, slug=category_slug)
    products = c.product_set.all()
    page_title = c.name
    meta_keywords = c.meta_keywords
    meta_description = c.meta_description
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))


def show_product(request, product_slug, template_name="product.html"):
    product = get_object_or_404(Product, slug=product_slug)
    categories = product.categories.filter(is_active=True)
    page_title = product.name
    meta_keywords = product.meta_keywords
    meta_description = product.meta_description
    
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))



def search(request):
    try:
        q=request.GET.get('q')
    except:
        None
    if q:
        products=Product.objects.filter(Q(name__icontains=q) |Q(brand__icontains=q) | Q(categories__name__icontains=q))
        count=len(products)
        context={'query':q,'products':products,'count':count}
        template_name="search.html"
        return render_to_response(template_name,context)
    else:
        return HttpResponseRedirect('/')
    







