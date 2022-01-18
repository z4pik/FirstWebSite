from django.contrib import admin
from .models import Order, StatusCrm, CommentCrm


# Register your models here.
class Comment(admin.StackedInline):
    '''Коммент в карточку'''
    model = CommentCrm
    fields = ('comment_dt', 'comment_text', )
    readonly_fields = ('comment_dt',)
    extra = 0


class OrderAdm(admin.ModelAdmin):
    '''Отображение в Админки'''
    list_display = ('id', 'order_status', 'order_name', 'order_phone', 'order_dt')
    list_display_links = ('id', 'order_name')  # кликабильность
    search_fields = ('id', 'order_name', 'order_phone', 'order_dt')  # Поиск виджет
    list_filter = ('order_status',)  # Фильтр
    list_editable = ('order_status', 'order_phone')  # Редактор данных
    list_per_page = 10
    list_max_show_all = 100
    fields = ('id', 'order_status', 'order_dt', 'order_name', 'order_phone')
    readonly_fields = ('id', 'order_dt')  # Только для чтение
    # Поле класса Comment
    inlines = [Comment,]


admin.site.register(Order, OrderAdm)
admin.site.register(StatusCrm)
admin.site.register(CommentCrm)
