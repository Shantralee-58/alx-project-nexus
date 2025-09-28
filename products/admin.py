from django.contrib import admin
from .models import Category, Product

# Register Category with a custom admin class
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Display these fields in the list view (only 'name' is available based on error)
    # The 'description' field is also available according to the error message.
    list_display = ['name']
    # Removed prepopulated_fields and 'slug' as the field is missing from the Category model.
    # prepopulated_fields = {'slug': ('name',)} 

# Register Product with a custom admin class
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ['name', 'price', 'stock', 'is_available', 'created_at', 'updated_at']
    # Allow filtering and searching
    list_filter = ['is_available', 'created_at', 'updated_at']
    list_editable = ['price', 'stock', 'is_available']
    search_fields = ['name', 'description']
    # Removed prepopulated_fields for 'slug' because the Product model is missing that field.
    # prepopulated_fields = {'slug': ('name',)} # <-- This line is removed/commented
