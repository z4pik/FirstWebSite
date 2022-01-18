from django.db import models

# Create your models here.
class PriceCard(models.Model):
    '''Информация по услугам (краточки) '''
    pc_value = models.CharField(max_length=20, verbose_name='Цена')
    pc_description = models.CharField(max_length=200, verbose_name='Описание')

    def __str__(self): # Делаем строковое представление типов данных
        return self.pc_value

    class Meta:
        verbose_name = 'Цены'
        verbose_name_plural = 'Цены'

class PriceTable(models.Model):
    '''Цена по услугам (таблица) '''
    pt_title = models.CharField(max_length=20, verbose_name='Услуга')
    pt_old_price = models.CharField(max_length=20, verbose_name='Старая цена')
    pt_new_price = models.CharField(max_length=20, verbose_name='Новая цена')

    def __str__(self): # Делаем строковое представление типов данных
        return self.pt_title

    class Meta:
        verbose_name = 'Услугу'
        verbose_name_plural = 'Услуги'