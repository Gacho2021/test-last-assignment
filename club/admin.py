from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import TechType, product, Review
# Register your models here.
admin.site.register(TechType)
admin.site.register(product)
admin.site.register(Review)
