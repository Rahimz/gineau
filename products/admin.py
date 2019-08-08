from django.contrib import admin
from .models import Product, Image, Email

# Register your models here.
admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Email)


# class ImageInline(admin.StackedInline):
#     model = Image
#     readonly_fields =('image1', 'image2')
#     extra = 0


# class ProductAdmin(admin.ModelAdmin):
#     model = Product
#     list_display = ('productName')
    
#     inlines = [ImageInline]

    
