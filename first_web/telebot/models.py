from django.db import models


# Create your models here.
class TeleSettings(models.Model):
    tg_token = models.CharField(max_length=200, verbose_name='Токен')
    tg_chat = models.CharField(max_length=200, verbose_name='Чат_id')
    tg_message = models.TextField(verbose_name='Сообщение')

    def __str__(self):  # Делаем строковое представление типов данных
        return self.tg_chat

    class Meta:
        verbose_name = 'Настройку'
        verbose_name_plural = 'Настройки'
