from django.contrib import admin

from .models import *

admin.site.register(Level)
admin.site.register(Questions)
admin.site.register(Answers)
admin.site.register(Category)
admin.site.register(PopulateData)

# Register your models here.
