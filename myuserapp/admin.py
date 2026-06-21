from django.contrib import admin
from django.shortcuts import render
from .models import Category, Product
from django.contrib.auth.decorators import login_required

admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price')
    list_filter = ('category',)
    search_fields = ('title',)

admin.site.site_header = "MyProject Admin"
admin.site.site_title = "MyProject Admin Portal"
admin.site.index_title = "Welcome to MyProject Admin Dashboard"

@login_required(login_url='/')
def home_view(request):
    return render(request, 'home.html')

