from django.contrib import admin
from .models import ContactMessage
from .models import Technique

admin.site.register(ContactMessage)
admin.site.register(Technique)
