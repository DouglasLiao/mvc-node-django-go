from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class User(models.Model):
    """
    Model para representar um usuário no sistema.
    No Django, o Model é a camada que gerencia os dados e a lógica de negócio.
    """
    name = models.CharField(
        max_length=100, 
        verbose_name="Nome",
        help_text="Nome completo do usuário"
    )
    email = models.EmailField(
        unique=True,
        verbose_name="Email",
        help_text="Email único do usuário"
    )
    age = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(120)],
        verbose_name="Idade",
        help_text="Idade do usuário (1-120 anos)"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Data de Criação"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Data de Atualização"
    )

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ['name']

    def __str__(self):
        """Representação em string do objeto"""
        return f"{self.name} ({self.email})"

    def get_absolute_url(self):
        """URL canônica do objeto"""
        from django.urls import reverse
        return reverse('user_detail', kwargs={'pk': self.pk})
