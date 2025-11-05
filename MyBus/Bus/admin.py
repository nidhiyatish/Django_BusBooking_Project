from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Bus)
admin.site.register(BusImage)
admin.site.register(Seat)
