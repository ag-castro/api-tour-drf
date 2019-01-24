
def reprova_comentario(modeladmin, request, queryset):
    queryset.update(status=False)


def aprova_comentario(modeladmin, request, queryset):
    queryset.update(status=True)

reprova_comentario.short_description = 'Reprovar Comentários'
aprova_comentario.short_description = 'Publicar Comentários'