from django.contrib import admin
from .models import User, Order

admin.site.register([User, Order])
