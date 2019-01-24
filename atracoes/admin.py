from django.contrib import admin
from .models import Atracao


@admin.register(Atracao)
class AtracaoAdmin(admin.ModelAdmin):
    pass
