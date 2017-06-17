from django.contrib import admin

# Register your models here.
from .models import UserStripe, EmailConfirmed,Product,CoverImage,Misc,MiscCoverImage


admin.site.register(UserStripe)
admin.site.register(Product)
admin.site.register(CoverImage)
admin.site.register(Misc)
admin.site.register(MiscCoverImage)

admin.site.register(EmailConfirmed)