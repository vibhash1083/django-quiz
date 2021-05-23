from django.contrib import admin

from .models import PopulateData, Question, Choice, Test, TestResponses

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(PopulateData)
admin.site.register(Test)
admin.site.register(TestResponses)
