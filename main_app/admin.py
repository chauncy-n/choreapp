from django.contrib import admin
from .models import Chore, Child, Reward

# Register your models here.
admin.site.register(Chore)
admin.site.register(Child)
admin.site.register(Reward)

