from django.contrib import admin
from .models import Fish, Decoration, Feeding

# Register your models here.
admin.site.register(Fish)
admin.site.register(Feeding)
admin.site.register(Decoration)