from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=200)  # Поле для названия новости
    description = models.TextField()  # Поле для описания новости
    created_at = models.DateTimeField(auto_now_add=True)  # Поле для даты создания новости
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Поле для автора новости, связанное с моделью пользователя

    def __str__(self):
        return self.title
    

