from django.contrib import admin
from .models import Choice, Question

# Register your models here.
admin.site.register(Choice)
admin.site.register(Question)