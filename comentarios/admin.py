from django.contrib import admin
from .models import Comentario
from .actions import aprova_comentario, reprova_comentario


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'data', 'status']
    actions = [aprova_comentario, reprova_comentario]

