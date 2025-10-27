from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Configuração do admin para o modelo User.
    O Django Admin é uma interface automática de administração.
    """
    list_display = ('name', 'email', 'age', 'created_at', 'updated_at')
    list_filter = ('age', 'created_at')
    search_fields = ('name', 'email')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('name',)
    
    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('name', 'email', 'age')
        }),
        ('Datas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
