from django.contrib import admin
from product import models
# Register your models here.
# class MediaInline(admin.StackedInline):
#     model = models.ProductMedia
#     extra = 1

# @admin.register(models.Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('title', 'price')
#     inlines = [
#         MediaInline
#     ]
    
# @admin.register(models.Category)
# class CategoryAdmin(admin.ModelAdmin):
#     '''Admin View for Category'''
#     list_display = ('title',)
#     prepopulated_fields = {'slug':('title',)}

# @admin.register(models.Size)
# class SizeAdmin(admin.ModelAdmin):
#     '''Admin View for Category'''
#     list_display = ('title',)
#     prepopulated_fields = {'slug':('title',)}
@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    '''Admin View for Author'''

    list_display = ('name','lastname','dateborth','bio')
    search_fields = ('name',)
    
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    '''Admin View for Product'''

    list_display = ('title','description','price',)
    list_filter = ('title',)
    search_fields = ('title',)
    
admin.site.register(models.Category)



# admin.site.register(models.Product)
# admin.site.register(models.Author)