from django.contrib import admin
from .models import Product, Category,CoverImage
from .forms import ProductAdminForm
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ('name', 'price', 'old_price', 'created_at', 'updated_at',)
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['-created_at']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    exclude = ('created_at', 'updated_at',)
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Product, ProductAdmin)

	

    
class CategoryAdmin(admin.ModelAdmin):
	#sets up values for how admin site lists categories
	list_display = ('name', 'created_at', 'updated_at',)
	list_display_links = ('name',)
	list_per_page = 20
	ordering = ['name']
	search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
	exclude = ('created_at', 'updated_at',)
	# sets up slug to be generated from category name
	prepopulated_fields = {'slug' : ('name',)}


admin.site.register(Category, CategoryAdmin)

admin.site.register(CoverImage)