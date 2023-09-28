from django.contrib import admin
from .models import Case, CaseBlock, New

# class TestCase(admin.ModelAdmin):
#     description = ('date_started',),
#     titleForURL = ('date_started',)

admin.site.register(Case)
admin.site.register(CaseBlock)
admin.site.register(New)