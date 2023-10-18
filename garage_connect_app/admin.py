from django.contrib import admin
from .models import FormData

# Register your models here.
@admin.register(FormData)
class FormDataAdmin(admin.ModelAdmin):
    list_display = ['kenteken', 'onderhoud', 'datum', 'opmerkingen']
