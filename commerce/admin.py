from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from commerce.models import Product,  ProductImage, Category, artist,  \
    Label


class InlineProductImage(admin.TabularInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    inlines = [InlineProductImage,]
    list_display = ('id', 'name', 'qty', 'description', 'cost', 'price', 'discounted_price')
    list_filter = ('category', 'label', 'artist')
    search_fields = ('name', 'qty', 'description', 'cost', 'price', 'discounted_price')

admin.site.register(Product ,ProductAdmin)
# admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(artist)
admin.site.register(Label)