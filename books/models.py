
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Books(models.Model):
    manufacturer = models.ForeignKey(User, on_delete=models.CASCADE, max_length=100, verbose_name='Производитель', blank=True,null=True)
    book = models.CharField(max_length=100, verbose_name='Книга')
    author = models.CharField(max_length=100, verbose_name='Автор')
    description = models.TextField(blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='img/', blank=True, verbose_name='Фото')
    year = models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')

    def __str__(self):
        return f"{self.book} ({self.year})"
    