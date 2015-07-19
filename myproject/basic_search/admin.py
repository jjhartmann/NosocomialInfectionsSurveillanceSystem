from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Influenza_AA)
admin.site.register(Influenza_NA)
admin.site.register(Influenza_FAA)
admin.site.register(Influenza_FNA)